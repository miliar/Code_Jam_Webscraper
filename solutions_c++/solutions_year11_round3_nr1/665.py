#include<stdio.h>
int T, N, M;
char map[100][100];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d",&T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d %d",&N,&M);
		int i, j;
		for(i=1; i<=N; i++) scanf("%s", &map[i][1]);
		for(i=1; i<N; i++) for(j=1; j<M; j++)
		{
			if(map[i][j] == '.') continue;
			if(map[i][j] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#'){
				map[i][j] = '/'; map[i][j+1] = '\\'; map[i+1][j] = '\\'; map[i+1][j+1] = '/';
			}
		}
		int c=0;
		for(i=1; i<=N; i++) for(j=1; j<=M; j++) if(map[i][j] == '#') c++;
		if(c) printf("Case #%d:\nImpossible\n", t);
		else{
			printf("Case #%d:\n",t );
			for(i=1; i<=N; i++) printf("%s\n",&map[i][1]);
		}
	}
	return 0;
}