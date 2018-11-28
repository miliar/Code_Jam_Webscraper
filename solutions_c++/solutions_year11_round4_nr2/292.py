#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define N 10
using namespace std;

char map[N][N];

int main(){
	int T, time=0, i, j, a, b, k, r, c, d, f;
	double cx, cy, dx, dy;
	scanf("%d", &T);
	while(T--){
		f=0;
		scanf("%d%d%d", &r, &c, &d);
		for(i=0; i<r; i++)
			scanf(" %s", &map[i]);
		for(k=min(r, c); !f&&k>=3; k--){
			//printf("-----k=%d-----\n", k);
			for(i=0; !f&&i+k<=r; i++)
				for(j=0; !f&&j+k<=c; j++){
					cx=i+(double)(k-1)/2;
					cy=j+(double)(k-1)/2;
					dx=dy=0;
					//printf("now cx=%f, cy=%f\n", cx, cy);
					for(a=i; a<i+k; a++){
						for(b=j; b<j+k; b++){
							if(a==i&&b==j) continue;
							else if(a==i&&b==j+k-1) continue;
							else if(a==i+k-1&&b==j) continue;
							else if(a==i+k-1&&b==j+k-1) continue;
							dx+=((double)a-cx)*(d+map[a][b]-'0');
							dy+=((double)b-cy)*(d+map[a][b]-'0');
						}
					}
					if(dx==0.0&&dy==0.0) f=1;
					//printf("dx=%f, dy=%f\n", dx, dy);
				}
			if(f) break;
		}
		if(f) printf("Case #%d: %d\n", ++time, k);
		else printf("Case #%d: IMPOSSIBLE\n", ++time);
	}
	return 0;
}
