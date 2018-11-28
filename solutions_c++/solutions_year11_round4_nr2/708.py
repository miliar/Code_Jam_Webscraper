#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
using namespace std;

#define _(a,b) memset(a,b,sizeof(a))
#define f(a,b,c) for(int a=b; a<c; a++)
#define esp 1e-9

int T, w[500][500], R, C, D, mk, k, ma[500][500];

bool chk(int a, int b, int p){
	double rx, ry, x=0, y=0, mass=0, ex, ey;
	for(int i=a; i<a+p; i++){
		for(int j=b; j<b+p; j++){
			if(!((i==a&&j==b)||(i==a&&j==b+p-1)||(i==a+p-1&&j==b)||(i==a+p-1&&j==b+p-1))){
				mass+=w[i][j];
				x+=w[i][j]*j;
				y+=w[i][j]*i;
			}
		}
	}
	rx=(double)x/mass;
	ry=(double)y/mass;
	ex=b+(p-1)/2.0;
	ey=a+(p-1)/2.0;
	if(fabs(rx-ex)<esp&&fabs(ry-ey)<esp) return true;
	return false;
}

int main(void){
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%d%d%d", &R, &C, &D);
		bool flag=false;
		for(int i=0; i<R; i++){
			getchar();
			for(int j=0; j<C; j++){
				w[i][j]=getchar()-'0';
				w[i][j]+=D;
			}
		}
		memset(ma, 0, sizeof(ma));
		for(int i=0; i<R-2; i++)
			for(int j=0; j<C-2; j++){
				for(int m=min(R-i,C-j); m>=3; m--) if(chk(i,j,m)){ma[i][j]=m; break;}
			}
		k=0;
		for(int i=0; i<R-2; i++)
			for(int j=0; j<C-2; j++){
				k=max(k, ma[i][j]);
			}
		printf("Case #%d: ", cas);
		if(k){
			printf("%d\n", k);
		} else{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
