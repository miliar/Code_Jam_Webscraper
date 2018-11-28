
#include<stdio.h>
#include<string.h>

char graph[60][60];
char ans[60][60];
int r,c;
bool isOk(int i,int j)
{
	if(i<r&&j<c&&graph[i][j]=='#')
		return true;
	
	return false;
}
int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		
		scanf("%d%d",&r,&c);
		int i,j;
		for(i=0;i<r;i++)
		{
			scanf("%s",graph[i]);
		}

		bool can = true;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(graph[i][j]=='#')
				{
					if(isOk(i,j+1)&&isOk(i+1,j+1)&&isOk(i+1,j))
					{
						graph[i][j]='//';
						graph[i][j+1]='\\';
					    graph[i+1][j]='\\';
						graph[i+1][j+1]='//';
					}
	               else
					can = false;
				}
			
				if(can==false)
					break;
			}
			if(can==false)break;
		}

		printf("Case #%d:\n",cases);
		if(can==false)
		{
			printf("Impossible\n");
		}
		else
		{
            for(i=0;i<r;i++)
				printf("%s\n",graph[i]);
		}
		//printf("Case #%d: %.6lf\n",cases,double(ans));
      
	}
	return 0;
}