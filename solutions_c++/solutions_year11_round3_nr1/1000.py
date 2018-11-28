#include<iostream>
#include<string.h>
using namespace std;
char board[52][52];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1-large.txt","w",stdout);
	int T,i,j,cases,R,C;
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&R,&C);
		memset(board,0,sizeof(board));
		for(i=1;i<=R;i++)
			scanf("%s",board[i]+1);
		for(i=1;i<=R;i++)
			for(j=1;j<=C;j++)
				if(board[i][j]=='#' && board[i][j+1]=='#' && board[i+1][j]=='#' && board[i+1][j+1]=='#')
				{
					board[i][j]='/';
					board[i][j+1]='\\';
					board[i+1][j]='\\';
					board[i+1][j+1]='/';
				}
		for(i=1;i<=R;i++)
		{
			for(j=1;j<=C;j++)
				if(board[i][j]=='#')
					break;
			if(j<=C)
				break;
		}
		printf("Case #%d:\n",cases);
		if(i<=R)
			printf("Impossible\n");
		else
		{
			for(i=1;i<=R;i++)
				printf("%s\n",board[i]+1);
		}
	}
	return 0;
}
