#include<cstdio>
int main()
{
	int test,t=0;
	scanf("%d",&test);
	while(test--)	
	{
		int row,col,flag=0;
		char ch[100][100];
		scanf("%d%d",&row,&col);
		for(int i=0;i<row;i++)
			scanf("%s",ch[i]);
	 	for(int i=0;i<row;i++)
		{
			for(int j=0;j<col;j++)
			{
				if(ch[i][j]=='#' && ch[i][j+1]=='#' && ch[i+1][j]=='#' && ch[i+1][j+1]=='#')
				{	
					ch[i][j]='/';
					ch[i][j+1]='\\';
					ch[i+1][j]='\\';
					ch[i+1][j+1]='/';
				}
				else if(ch[i][j]=='#'){
					flag=1;
					break;
				}
			}
			if(flag==1)
				break;
		}
		printf("Case #%d: \n",++t);
		if(flag==1)
			printf("Impossible\n");
		else
		{
			for(int i=0;i<row;i++)
				printf("%s\n",ch[i]);
		}
	}
	return 0;
}
