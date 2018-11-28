#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		int R, C; scanf("%d%d\n", &R, &C);
		char Mapa[50][50];
		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) scanf("%c", &Mapa[i][j]);
			scanf("\n");
		}
		for(int i=0; i<R-1; i++) {
			for(int j=0; j<C-1; j++) {
				if(Mapa[i][j]=='#') {
					if(Mapa[i+1][j]=='.' || Mapa[i+1][j+1]=='.' || Mapa[i][j+1]=='.') goto nelze;
					Mapa[i][j]=47; Mapa[i][j+1]=92;
					Mapa[i+1][j]=92; Mapa[i+1][j+1]=47;
				}
			}
		}
		for(int i=0; i<R; i++) for(int j=0; j<C; j++) if(Mapa[i][j]=='#') goto nelze;
		printf("Case #%d:\n", test);
		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) printf("%c", Mapa[i][j]);
			printf("\n");
		}
		goto lze;
		nelze:
		printf("Case #%d:\nImpossible\n", test);
		lze:
		;
	}

	return 0;
}
