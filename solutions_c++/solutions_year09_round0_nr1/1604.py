#include <cstdio>
#include <cstring>

int L,D,N;
char w[5100][20];
char s[600][800];

void init()
{
	int i;
	
	scanf("%d%d%d",&L,&D,&N);
	for (i=0;i<D;i++)
	{
		scanf("%s",&w[i]);
	}
	for (i=0;i<N;i++)
	{
		scanf("%s",&s[i]);
	}
}

void work()
{
	int i,j,ps,k,tot;
	int y[20][32];
	int non_match[600];
	
	for (i=0;i<N;i++)
	{
		memset(y,0,sizeof(y));
		memset(non_match,0,sizeof(non_match));
		ps=0;
		for (j=0;j<L;j++)
		{
			if (s[i][ps]=='(')
			{
				ps++;
				while (s[i][ps]!=')')
				{
					y[j][ s[i][ps] - 'a' ] = 1;
					ps++;
				}
				ps++;
			}
			else
			{
				y[j][ s[i][ps] - 'a' ] = 1;
				ps++;
			}
		}
		
		for (j=0;j<L;j++)
		{
			for (k=0;k<D;k++)
			{
				if (!y[j][ w[k][j] - 'a' ])
					non_match[k]=1;
			}
		}
		
		tot=0;
		for (j=0;j<D;j++)
		{
			if (non_match[j]==0)
				tot++;
		}
		
		printf("Case #%d: %d\n",i+1,tot);
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	init();
	work();
	
	return 0;
}
