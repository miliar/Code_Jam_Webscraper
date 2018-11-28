#include <stdio.h>
#include <string.h>
char map[110][110];
char after[110][110];
int N, K;
int red, blue;
int main() {
	int i, j, k;
	int ca, cases = 0;
	scanf("%d", &ca);
	while (ca--) {
		printf("Case #%d: ", ++cases);
		scanf("%d%d", &N, &K);
		for (i=0;i<N;++i) {
			scanf("%s", map[i]);			
		}
		for (i=N-1;i>=0;--i) {
			k=0;
			for (j=N-1;j>=0;--j) {
				if (map[i][j] != '.') {
					after[i][k++] = map[i][j];
				}
			}
			for (j=k;j<N;++j) after[i][j] = '.';
			after[i][j] = 0;
		}
		red = blue = 0;
		for (i=0;i<N;++i) {
			for(j=0;j<N;++j) {
				if (after[i][j]=='.') continue;
				for(k=0;k<K;++k) {
					if (i+k >= N || after[i+k][j] != after[i][j]) break;
				}
				if (k>=K) {
					if (after[i][j]=='R') red = 1; else blue = 1;
				}
				for(k=0;k<K;++k) {
					if (j+k >= N || after[i][j+k] != after[i][j]) break;
				}
				if (k>=K) {
					if (after[i][j]=='R') red = 1; else blue = 1;
				}
				for(k=0;k<K;++k) {
					if (i+k >= N || j + k >= N || after[i+k][j+k] != after[i][j]) break;
				}
				if (k>=K) {
					if (after[i][j]=='R') red = 1; else blue = 1;
				}
				for(k=0;k<K;++k) {
					if (i-k < 0 || j + k >= N || after[i-k][j+k] != after[i][j]) break;
				}
				if (k>=K) {
					if (after[i][j]=='R') red = 1; else blue = 1;
				}
			}
		}
		if (red && blue ) puts("Both"); else
		if (!red && !blue) puts("Neither"); else
		if (red) puts("Red"); else
			puts("Blue");
	}
	return 0;
}
