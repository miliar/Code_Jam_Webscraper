#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char a[55][55];
int N, K;
int d[8][2] = {{1, 1}, -1, -1, 1, 0, -1, 0, 0, 1, 0, -1, 1, -1, -1, 1};

bool f(int x, int y) {
	for (int i=0;i<8;++i) {
		bool f = 1;
		for (int j=1;j<K && f;++j) {
			int xx = x+j*d[i][0], yy = y+j*d[i][1];
			if (xx<0 || xx>N-1 || yy<0 || yy>N-1) {f=0; break;}
			f &= (a[xx][yy]==a[x][y]);
		}
		if (f) return 1;
	}
	return 0;
}

int main() {
	int T; scanf("%d", &T); char s[100];
	for (int cas=1; cas<=T; ++cas) {
		memset(a, 0, sizeof(a));
		scanf("%d%d", &N, &K); gets(s);
		for (int i=0;i<N;++i) {
			for (int j=0;j<N;++j)
				scanf("%c", &a[j][N-1-i]);
			gets(s);
		}
		for (int j=0;j<N;++j) {
			for (int i=N-1;i>=0;--i) {
				if (a[i][j]=='.') continue;
				int k;
				for (k=i;k+1<N&&a[k+1][j]=='.';++k);
				swap(a[k][j], a[i][j]);
			}
		}
		//for (int i=0;i<N;++i) puts(a[i]); puts("");
		bool r=0, b=0;
		for (int i=0;i<N;++i)
			for (int j=0;j<N;++j) {
				if (a[i][j]=='.') continue;
				if (f(i,j)==1) {
					if (a[i][j]=='B') b=1;
					if (a[i][j]=='R') r=1;
				}
			}
		printf("Case #%d: ", cas);
		if (b&&r) puts("Both");
		else if (b) puts("Blue");
		else if (r) puts("Red");
		else puts("Neither");
	}
	return 0;
}
