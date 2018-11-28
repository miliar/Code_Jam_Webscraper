#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int maxn = 110;

struct tpos{
	int s,e,side;
	bool operator <(tpos a) const{
		if (s!=a.s) return s<a.s;
		if (e!=a.e) return e<a.e;
		return side<a.side;
	}
};

int n,m,t;

tpos a[maxn*2];
bool was[maxn*2];

#define nul(a) memset(a,0,sizeof(a))

int yk = 0;

void init(){
	scanf("%d%d%d\n",&t,&n,&m);
	t*=60;
	int i;
	yk = 0;
	nul(was);
	int hs,ms,he,me;
	for (i = 0 ; i<n ; i++){
		scanf("%d:%d %d:%d\n",&hs,&ms,&he,&me);
		a[yk].s = hs*3600+ms*60;
		a[yk].e = he*3600+me*60;
		a[yk++].side = 0;
	}
	for (i = 0 ; i<m ; i++){
		scanf("%d:%d %d:%d\n",&hs,&ms,&he,&me);
		a[yk].s = hs*3600+ms*60;
		a[yk].e = he*3600+me*60;
		a[yk++].side = 1;
	}
}

void solve(){
	sort(a,a+yk);
	int i;
	int res[2];
	nul(res);
	for (i = 0 ; i<yk ; i++){
		if (!was[i]){
			int tekside = 1-a[i].side;
			was[i] = true;
			int tt = a[i].e+t;
			res[a[i].side]++;
			int j;
			for (j = i+1 ; j<yk ; j++){
				if (!was[j] && tt<=a[j].s && a[j].side==tekside){
					was[j] = true;
					tt = a[j].e+t;
					tekside = 1-tekside;
				}
			}
		}
	}
	printf("%d %d",res[0],res[1]);
}


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for (i = 1 ; i<=t ; i++){
		printf("Case #%d: ",i);
		init();
		solve();
		printf("\n");
	}
	return 0;
}