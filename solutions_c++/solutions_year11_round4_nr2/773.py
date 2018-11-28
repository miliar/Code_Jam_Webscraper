#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define eps 1e-6
#define oo 1e9


using namespace std;


int T, m, n, q, w, mi, ma, fi, cc, e,  z, an, r, c, d;
char a[20][20], temp[10];
int b[20][20];
double sx, sy, cnt;

void sum(int x, int y, int q, int w){
//	printf("%d %d %d %d\n", x, y, q, w);
	sx = 0, sy = 0; cnt = 0;
	for (int i=x; i<q; i++)
		for (int j=y; j<w; j++){
			sx += b[i][j]*((double)i+0.5);
			sy += b[i][j]*((double)j+0.5);
			cnt += b[i][j];
		}
	sx -= (b[x][y] * ((double)x + 0.5));
	sy -= (b[x][y] * ((double)y + 0.5));
	sx -= (b[q-1][y] * ((double)q - 1 + 0.5));
	sy -= (b[q-1][y] * ((double)y + 0.5));
	sx -= (b[q-1][w-1] * ((double)q - 1 + 0.5));
	sy -= (b[q-1][w-1] * ((double)w - 1 + 0.5));
	sx -= (b[x][w-1] * ((double)x + 0.5));
	sy -= (b[x][w-1] * ((double)w - 1 + 0.5));
	cnt -= b[x][y]; cnt -= b[q-1][y]; cnt -= b[x][w-1]; cnt -= b[q-1][w-1];
//	sx -= b[(q+x-1)/2][(w+y-1)/2]*((double)((q+x-1)/2)+0.5);
//	sy -= b[(q+x-1)/2][(w+y-1)/2]*((double)((w+y-1)/2)+0.5);
//	cnt -= b[(q+x-1)/2][(w+y-1)/2];
	sx /= cnt;
	sy /= cnt;
//	printf("%f %f\n", sx, sy);
}

bool feq(double x, double y){
	return (fabs(x - y) <= eps);
}

int main(){
	scanf("%d", &T);
	for (int rr=1; rr<=T; rr++){
		printf("Case #%d: ", rr);
		scanf("%d%d%d", &r, &c, &d);
		gets(temp);
		for (int i=0; i<r; i++){
			gets(a[i]);
		}
		for (int i=0; i<r; i++){
			for (int j=0; j<c; j++){
				b[i][j] = (a[i][j] - '0') + d;
			}
		}
		an = 0; fi = 0;
		for (int i=min(r, c); i>=3; i--){
			for (int j=0; j+i<=r; j++)
				for (int k=0; k+i<=c; k++){
					sum(j, k, j+i, k+i);
					if (feq(sx,((double)j+j+i)/2.0) && feq(sy, ((double)k+k+i)/2.0)){
						an = i;
						fi = 1;
						break;
					}
					if (fi == 1)
						break;
				}
				if (fi == 1)
					break;
		}
		if (an != 0)
			printf("%d\n", an);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
