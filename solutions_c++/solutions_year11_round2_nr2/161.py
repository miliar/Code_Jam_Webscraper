#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int n,d;
int c[1000005],ind=0;

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		ind=0;
		int ok=1;
		scanf("%d%d",&n,&d);
		for (int i=0; i<n; i++) {
			int tc,tot;
			scanf("%d%d",&tc,&tot);
			for (int j=0; j<tot; j++) {
				c[ind]=tc; ind++;
			}
		}
		double mi=0,mx=1e15,mid,cur;
		while (mi+1e-3<mx) {
			mid=(mi+mx)/2;
			//printf("%f\n",mid); fflush(stdout);
			ok=1;
			cur=c[0]-mid;
			for (int i=1; i<ind; i++) {
				if (c[i]+mid<cur+d) { ok=0; break; }
				if (c[i]-mid<cur+d) cur=cur+d;
				else cur=c[i]-mid;
			}
			if (ok==0) mi=mid;
			else mx=mid;
		}
		printf("Case #%d: %.1f\n",T,mid);
	}
}
