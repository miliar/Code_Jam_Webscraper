#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define MN 500
using namespace std;
int n;
int d[MN][MN], c[MN][MN];
bool process(int k)
{
	int a, b, i, j;

	for (a = 0; a+n-1 < k; a++) {
		for (b = 0; b+n-1 < k; b++) {
			memset(c,255,sizeof(c));
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++)
					c[a+i][b+j] = d[i][j];
			}
			for (i = 0; i < k; i++) {
				for (j = 0; j < i; j++) {
					if (c[i][j] == -1 || c[j][i] == -1) continue;
					if (c[i][j] != c[j][i]) break;
				}
				if (j < i) break;
			}
			if (i < k) continue;
			for (i = 0; i < k; i++) {
				for (j = 0; j < k-1-i; j++) {
					if (c[i][j] == -1 || c[k-1-j][k-1-i] == -1) continue;
					if (c[i][j] != c[k-1-j][k-1-i]) break;
				}
				if (j < k-1-i) break;
			}
			if (i >= k) return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i, j;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for (i = 0; i < n; i++) {
			for (j = 0; j < i+1; j++)
				scanf("%d",&d[i-j][j]);
		}
		for (i = 0; i < n-1; i++) {
			for (j = 0; j < n-1-i; j++)
				scanf("%d",&d[n-1-j][i+j+1]);
		}
		for (i = n;; i++) {
			if (process(i)) break;
		}
		printf("%d\n",i*i-n*n);
	}		
	return 0;
}