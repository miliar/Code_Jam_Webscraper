#include<cmath>
#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const double EPS=1e-9;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int r,c,d; scanf("%d%d%d ",&r,&c,&d);
		static int w[500][500];
		rep(y,r){
			rep(x,c){
				char dgt; scanf("%c",&dgt);
				w[y][x]=dgt-'0';
			}
			getchar();
		}

		int k;
		for(k=min(r,c);k>=3;k--){
			rep(i,r-k+1) rep(j,c-k+1) {
				double cy=i+(k-1.0)/2,cx=j+(k-1.0)/2,gy=0,gx=0;
				for(int y=i;y<i+k;y++) for(int x=j;x<j+k;x++) {
					if((y==i     && x==j) || (y==i     && x==j+k-1)
					|| (y==i+k-1 && x==j) || (y==i+k-1 && x==j+k-1)) continue;
					gy+=w[y][x]*(y-cy);
					gx+=w[y][x]*(x-cx);
				}
				if(abs(gy)<EPS && abs(gx)<EPS) goto FOUND;
			}
		}
		FOUND:;

		if(k<3) printf("Case #%d: IMPOSSIBLE\n",T);
		else    printf("Case #%d: %d\n",T,k);
	}

	return 0;
}
