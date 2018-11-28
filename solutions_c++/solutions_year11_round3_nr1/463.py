#include <stdio.h>
#define MAX 100

int main()
{
	char paint[MAX][MAX];
	int done[MAX][MAX];
	int n,m;

	int i,j,k;

	int t,ccnt;

	scanf("%d",&t);
	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;++i)
			scanf("%s",paint[i]);

		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				done[i][j]=0;
		for(i=0;i<n-1;++i)
			for(j=0;j<m-1;++j)
			{
				if(done[i][j] || paint[i][j]=='.')
					continue;

				if(paint[i+1][j]=='.' ||
				   paint[i][j+1]=='.' ||
				   paint[i+1][j+1]=='.')
					continue;
				if(done[i+1][j] ||
				   done[i][j+1] ||
				   done[i+1][j+1])
					continue;

				done[i][j]=done[i+1][j+1]=1;
				done[i+1][j]=done[i][j+1]=2;
			}

		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				if(paint[i][j]=='#' && !done[i][j])
					goto  fim;

fim:
		printf("Case #%d:\n",ccnt);
		if(i==n && j==m)
		{
			for(i=0;i<n;++i)
			{
				for(j=0;j<m;++j)
					if(paint[i][j]=='.')
						printf(".");
					else
						printf("%c",(done[i][j])==1?'/':'\\');
				printf("\n");
			}

		}
		else
			printf("Impossible\n");
	}
	return 0;
}


