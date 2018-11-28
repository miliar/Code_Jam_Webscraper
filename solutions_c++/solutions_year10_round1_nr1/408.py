#include <stdio.h>

int N,K;
int Tcase;
char board[55][55];
int d[8][2]={{-1,0},{0,1},{1,0},{0,-1},{-1,1},{1,1},{1,-1},{-1,-1}};

bool check(char color)
{
	int i,j;
	int cnt=0;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if (board[i][j]!=color) continue;
			if (K==1) return true;
			int t;
			for (t=0;t<8;t++)
			{
				cnt=1;
				int x=i+d[t][0],y=j+d[t][1];
				while (x>=0&&x<N&&y>=0&&y<N&&board[x][y]==color)
				{
					cnt++;
					if (cnt==K) return true;
					x=x+d[t][0];
					y=y+d[t][1];
				}
			}
		}
	}
	return false;
}

int main()
{
	freopen("d:\\A-large.in","r",stdin);
	freopen("d:\\output.txt","w",stdout);
	scanf("%d",&Tcase);
	int tcase;
	for(tcase=1;tcase<=Tcase;tcase++)
	{
		scanf("%d %d",&N,&K);
		int i,j;
		for(i=0;i<N;i++)
			for(j=0;j<N;j++)
				scanf(" %c",&board[i][j]);
		
		for(i=0;i<N;i++)
		{
			int s;
			for(s=N-1;s>=0&&board[i][s]!='.';s--);
			
			j=s-1;
			while(j>=0)
			{
				if (board[i][j]!='.')
				{
					board[i][s]=board[i][j];
					board[i][j]='.';
					s--;
				}
				j--;
			}
		}
/*
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
				printf("%c",board[i][j]);
			puts("");
		}
*/
		bool winB=check('B');
		bool winR=check('R');
		printf("Case #%d: ",tcase);
		if (winB&&winR)
			puts("Both");
		else if (!winB&&!winR)
			puts("Neither");
		else if (winB&&!winR)
			puts("Blue");
		else 
			puts("Red");
	}

	return 0;
}