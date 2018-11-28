#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define MN 100
using namespace std;
int n;
int d[MN][MN];
bool f(int x, int y)
{return 0<=x&&x<n&&0<=y&&y<n?d[x][y]:0;}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, k, i, j;
	int R, x1, y1, x2, y2;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		memset(d,0,sizeof(d));
		n = 0;
		for (scanf("%d",&R);R--;) {
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (i = y1-1; i <= y2-1; i++) {
				for (j = x1-1; j <= x2-1; j++)
					d[i][j] = 1;
			}
			n = max(n,max(x2,y2));
		}
		for (k = 1;;k++) {
			for (i = n-1; i >= 0; i--) {
				for (j = n-1; j >= 0; j--)
					if (f(i-1,j)==f(i,j-1)&&f(i-1,j)!=d[i][j]) d[i][j] = 1-d[i][j];
			}
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					if (d[i][j]) break;
				}
				if (j < n) break;
			}
			if (i >= n) break;
		}
		printf("%d\n",k);
	}
	return 0;
}