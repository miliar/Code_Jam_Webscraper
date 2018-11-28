#include<stdio.h>
#include<algorithm>
using namespace std;

long long w[501][501], wx[501][501], wy[501][501];
long long sumw[501][501];
long long sumwx[501][501], sumwy[501][501];

long long inline calcSum(long long sum[501][501], long long ele[501][501], int x1, int y1, int x2, int y2) {
	return sum[x2][y2]-sum[x2][y1-1]-sum[x1-1][y2]+sum[x1-1][y1-1]-ele[x1][y1]-ele[x1][y2]-ele[x2][y1]-ele[x2][y2];
}

bool check(int x1, int y1, int x2, int y2, int cx, int cy, bool c) {
	long long sw=calcSum(sumw, w, x1, y1, x2, y2);
	long long swx=calcSum(sumwx, wx, x1, y1, x2, y2);
	long long swy=calcSum(sumwy, wy, x1, y1, x2, y2);
	if(c&&(sw%2!=0)) return false;
	if(c) {
		swx-=cx*sw+sw/2;
		swy-=cy*sw+sw/2;
	} else {
		swx-=cx*sw;
		swy-=cy*sw;
	}
	return swx==0&&swy==0;
}

int solve() {
	int R, C, D;
	scanf("%d%d%d", &R, &C, &D);
	for(int i=1;i<=R;i++) {
		char str[512];
		scanf("%s", str+1);
		for(int j=1;j<=C;j++) {
			w[i][j]=str[j]-'0';
		}
	}
	memset(sumw, 0, sizeof(sumw));
	memset(sumwx, 0, sizeof(sumwx));
	memset(sumwy, 0, sizeof(sumwy));
	for(int i=1;i<=R;i++) {
		for(int j=1;j<=C;j++) {
			wx[i][j]=w[i][j]*i;
			wy[i][j]=w[i][j]*j;

			sumw[i][j]=sumw[i-1][j]+sumw[i][j-1]-sumw[i-1][j-1]+w[i][j];
			sumwx[i][j]=sumwx[i-1][j]+sumwx[i][j-1]-sumwx[i-1][j-1]+w[i][j]*i;
			sumwy[i][j]=sumwy[i-1][j]+sumwy[i][j-1]-sumwy[i-1][j-1]+w[i][j]*j;
		}
	}
	int best=2;
	for(int i=1;i<=R;i++) {
		for(int j=1;j<=C;j++) {
			for(int d=(best+1)/2;i-d>0&&j-d>0&&i+d<=R&&j+d<=C;d++) {
				if(check(i-d, j-d, i+d, j+d, i, j, false)) {
					best=d*2+1;
				}
			}
			for(int d=(best+2)/2;i-d+1>0&&j-d+1>0&&i+d<=R&&j+d<=C;d++) {
				if(check(i-d+1, j-d+1, i+d, j+d, i, j, true)) {
					best=d*2;
				}
			}
		}
	}
	return best==2?-1:best;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int c=1;c<=t;c++) {
		int r=solve();
		if(r==-1) {
			printf("Case #%d: IMPOSSIBLE\n", c);
		} else {
			printf("Case #%d: %d\n", c, r);
		}
	}
}