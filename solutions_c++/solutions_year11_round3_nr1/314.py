#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int main() {
	int t,C;
	scanf("%d",&t);
	for (C=1;C<=t;++C) {
		int r,c;
		scanf("%d%d ",&r,&c);
		char f[r+3][c+3];
		memset(f,'.',sizeof(f));
		for (int i=1;i<=r;i++) {
			scanf("%s", &f[i][1]);
			f[i][c+1]='.';
		}
		
// 		for (int i=0;i<=r+1;i++) {
// 			for (int j=0;j<=c+1;j++)
// 				putchar(f[i][j]);
// 			putchar('\n');
// 		}

		char fail=0;
		for (int i=1;i<=r;i++) {
			for (int j=1;j<=c;++j) {
				if (f[i][j]=='#') {
					if (f[i][j+1]=='#' &&
						f[i+1][j]=='#' &&
						f[i+1][j+1]=='#') {
						f[i][j]='/';
						f[i][j+1]='\\';
						f[i+1][j]='\\';
						f[i+1][j+1]='/';
					} else {
						fail=1;
						goto end;
					}
				}
			}
		}
end:
		printf("Case #%d:\n",C);
		if (fail) {
			printf("Impossible\n");
		} else {
			for (int i=1;i<=r;i++) {
				for (int j=1;j<=c;++j)
					putchar(f[i][j]);
				putchar('\n');
			}
		}
	}
	return 0;
}
