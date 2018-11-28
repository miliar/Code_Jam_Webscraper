#include<stdio.h>
#include<string.h>
#define inf 999999999

int g[110][110];
char s[110][110], pos='a';
int aa[4]={-1,0,0,1}, bb[4]={0,-1,1,0};
char dfs(int, int);
int main()
{
	/*freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);*/
	int t, kk=0;
	scanf("%d", &t);

	while(t--){
		int h, w;
		pos='a';
		scanf("%d%d", &h, &w);
		memset(s, 0, sizeof(s));
		for(int i=1; i<=h; i++){
			for(int j=1; j<=w; j++){
				scanf("%d", &g[i][j]);
			}
		}
		for(int i=0; i<=h+1; i++) g[i][0]=g[i][w+1]=inf;
		for(int i=0; i<=w+1; i++) g[0][i]=g[h+1][i]=inf;

		for(int i=1; i<=h; i++){
			for(int j=1; j<=w; j++){
				if(!s[i][j])	s[i][j]=dfs(i, j);
			}
		}
		printf("Case #%d:\n", ++kk);
		for(int i=1; i<=h; i++){
			putchar(s[i][1]);
			for(int j=2; j<=w; j++){
				printf(" %c", s[i][j]);
			}
			putchar(10);
		}
	}
	return 0;
}

char dfs(int a, int b)
{
	if(s[a][b]) return s[a][b];
	int Mina=a, Minb=b, c, d;
	for(int k=0; k<4; k++){
		c=a+aa[k], d=b+bb[k];
		if(g[Mina][Minb]>g[c][d]) Mina=c, Minb=d;
	}
	if(Mina==a&&Minb==b){
		s[a][b]=pos++;
	}
	else s[a][b]=dfs(Mina, Minb);
	return s[a][b];
}