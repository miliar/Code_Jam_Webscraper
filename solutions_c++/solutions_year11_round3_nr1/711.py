#include<cstdio>
int tc;
int r,c;
char ar[100][100];
int main(){ 
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		scanf("%d %d\n",&r,&c);
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				scanf("%c",&ar[i][j]);
			}
			scanf("\n");
		}	
		
		for (int i = 0; i < r-1; i++) {
			for (int j = 0; j < c-1; j++) {
				if ((ar[i][j] == '.') || (ar[i][j] == '/') || (ar[i][j] == '\\')) continue;
				if ((ar[i][j] == '#') && (ar[i][j+1] == '#') && (ar[i+1][j] == '#') && (ar[i+1][j+1] == '#')) {
					ar[i][j] = '/'; ar[i][j+1] = '\\'; ar[i+1][j] = '\\'; ar[i+1][j+1] = '/';
				}
			}
		}
		bool imp = false;
		for (int i = 0; i < r; i++) {
			for (int j =0; j < c; j++) {
				if ((ar[i][j] =='#')) imp = true;
			}
		}
		printf("Case #%d:\n",ti);
		if (imp) printf("Impossible\n");
		else {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) printf("%c",ar[i][j]);
				printf("\n");
			}
		}
	
	}
}