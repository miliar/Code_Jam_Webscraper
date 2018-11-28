#include<stdio.h>

char map[55][55];

bool flag;
int n,m;
void work(int a,int b)
{
	if(map[a][b]=='#' && map[a][b+1]=='#'&&	map[a+1][b]=='#' && map[a+1][b+1]=='#')
	{
		map[a][b]='/';
		map[a][b+1]='\\';
		map[a+1][b]='\\';
		map[a+1][b+1]='/';
	}else
	 flag=false;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ct;
	int tt=0;
	int i,j;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d%d",&n,&m);
		getchar();
		for(i=0;i<n;i++)
				gets(map[i]);
		flag=true;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(map[i][j]=='#')
					work(i,j);
				if(flag==false)break;
			}
			if(flag==false)break;
		}
		printf("Case #%d:\n",++tt);
		if(flag==false)printf("Impossible\n");
		else
		{
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
					printf("%c",map[i][j]);
				printf("\n");
			}			
		}
	}
	return 0;
}