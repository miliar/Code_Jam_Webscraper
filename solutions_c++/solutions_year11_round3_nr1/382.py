#include<stdio.h>
#include<string.h>
main()
{
	int abc,ab,i,j,n,m,k,ans,no;
	char map[70][70];
	bool used[70][70];
	freopen("LA.in","r",stdin);
	freopen("LA.out","w",stdout);
	scanf("%d",&abc);
	for(ab=1;ab<=abc;ab++)
	{
		no=0;
		memset(map,0,sizeof(map));
		scanf("%d %d",&m,&n);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				scanf(" %c",&map[i][j]);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				if(map[i][j]=='#')
					if(map[i][j+1]=='#'&&map[i+1][j]=='#'&&map[i+1][j+1]=='#')
					{
						map[i][j]='/';
						map[i][j+1]='\\';
						map[i+1][j]='\\';
						map[i+1][j+1]='/';
					}
					else
					{
						no=1;
						break;
					}
		printf("Case #%d:\n",ab);			
		if(no==0)
		{
			for(i=0;i<m;i++)
			{
				for(j=0;j<n;j++)
					printf("%c",map[i][j]);
				puts("");
			}
		}
		else printf("Impossible\n");
	}
}
