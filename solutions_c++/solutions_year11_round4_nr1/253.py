#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

struct walk {
	int s,d;
} w[1005];

int tc;
int tot,sa,sb,t,n;

int cmp (walk a,walk b) {
	return a.s<b.s;
}


int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d%d%d%d%d",&tot,&sa,&sb,&t,&n);
		sb-=sa;
		double ret=0.0;
		int non=0,last=0;;
		for (int i=0; i<n; i++) {
			int wa,wb;
			scanf("%d%d%d",&wa,&wb,&w[i].s);
			w[i].s+=sa;
			w[i].d=wb-wa;
			non+=wa-last;
			last=wb;
		}
		non+=tot-last;
		w[n].d=non; w[n].s=sa;
		n++;
		sort(w,w+n,cmp);
		double now=0;
		for (int i=0; i<n; i++) {
			double allr=w[i].d*1.0/(w[i].s+sb);
			if (now+allr<t) {
				ret+=allr;
				now+=allr;
				continue;
			}
			if (now<t) {
				ret+=t-now;
				ret+=(w[i].d-(t-now)*(w[i].s+sb))/w[i].s;
				now=t+1;
				continue;
			}
			ret+=w[i].d*1.0/w[i].s;
		}
		printf("Case #%d: %.8f\n",T,ret);
			
	}
}
