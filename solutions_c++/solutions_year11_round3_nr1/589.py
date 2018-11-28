#include<cstdio>
char M[52][52];
int main(){
	int T, R, C;
	scanf("%d", &T);
	for (int iT = 1; iT <= T; iT++){
		printf("Case #%d:\n", iT);
		scanf("%d%d", &R, &C);
		for (int i=0; i<R; i++)
			scanf("%s", M+i);
		bool fail = false;
		for (int i=0; !fail && i<R; i++)
			for (int j=0; !fail && j<C; j++)
				if (M[i][j] == '#'){
					M[i][j] = '/';
					if (j+1 < C && M[i][j+1] == '#')
						M[i][j+1] = '\\';
					else{
						fail = true;
						break;
					}
					if (i+1 < R && M[i+1][j] == '#')
						M[i+1][j] = '\\';
					else{
						fail = true;
						break;
					}
					if (M[i+1][j+1] == '#')
						M[i+1][j+1] = '/';
					else{
						fail = true;
						break;
					}
				}
		if (fail)
			puts("Impossible");
		else
			for (int i=0; i<R; i++)
				puts(M[i]);
	}
	return 0;
}
