#include<iostream>
using namespace std;
const int N=55;

int row,col;
char input[N][N];
bool ans;

void DFS()
{
	int i,j;
	bool result=false;
	for(i=0;i<row-1;i++)
	{
		for(j=0;j<col-1;j++)
		{
			if(input[i][j]=='#'&&input[i][j+1]=='#'&&input[i+1][j]=='#'&&input[i+1][j+1]=='#')
			{				
				input[i][j]='/';
				input[i][j+1]='\\';
				input[i+1][j]='\\';
				input[i+1][j+1]='/';				
			}
		}
	}	
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			if(input[i][j]=='#')
			{
				ans=false;
				return ;
			}
		}
	}	
	ans=true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int cas,tot_cas;
	int i,j;
	scanf("%d",&tot_cas);
	cas=1;	
	while(cas<=tot_cas)
	{
		memset(input,0,sizeof(input));		
		scanf("%d%d",&row,&col);
		for(i=0;i<row;i++)
			scanf(" %s",input+i);
		DFS();
		printf("Case #%d:\n",cas);
		if(ans==false)
			printf("Impossible\n");
		else
		{
			for(i=0;i<row;i++)
			{				
				printf("%s\n",input[i]);
			}
		}
		cas++;
	}
	return 0;
}