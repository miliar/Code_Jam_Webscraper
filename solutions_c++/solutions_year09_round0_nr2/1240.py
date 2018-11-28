#include <cstdio>
#include <cctype>
#include <cstring>

int T, H, W, K;
int a[105][105], ret[105][105];

inline bool valid(int i, int j) {
	return (i>=0 && i<H && j>=0 && j<W);
}
int dfs(int i, int j) {
	int mn = a[i][j], mi=i, mj=j;
	if (valid(i-1,j) && a[i-1][j]<mn) mn=a[i-1][j], mi=i-1, mj=j;
	if (valid(i,j-1) && a[i][j-1]<mn) mn=a[i][j-1], mi=i, mj=j-1;
	if (valid(i,j+1) && a[i][j+1]<mn) mn=a[i][j+1], mi=i, mj=j+1;
	if (valid(i+1,j) && a[i+1][j]<mn) mn=a[i+1][j], mi=i+1, mj=j;
	if (ret[mi][mj]!=-1) { return ret[i][j]=ret[mi][mj]; }
	if (mi==i&&mj==j) return ret[i][j]=K++;
	return ret[i][j]=dfs(mi, mj);
}
void solv() {
	for (int i=0;i<H;i++) 
		for (int j=0;j<W;j++) 
			if (ret[i][j]==-1) dfs(i, j);
}

int main () {
	scanf("%d", &T);
	for (int i=0;i<T;i++) {
		memset(ret, -1, sizeof(ret)); K=0;
		scanf("%d%d", &H, &W);
		for (int h=0;h<H;h++)
			for (int w=0;w<W;w++)
				scanf("%d", &a[h][w]);
		solv();
		printf("Case #%d:\n", i+1);
		for (int h=0;h<H;h++)
			for (int w=0;w<W;w++)
				printf(w==W-1?"%c\n":"%c ", 'a'+ret[h][w]);
	}
	return 0;
}
