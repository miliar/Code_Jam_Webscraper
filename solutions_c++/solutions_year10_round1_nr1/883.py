#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,K,CASE=0;
	int i,j,k;
	int a,b,c;
	int red,blue;
	int count;
	string s1,s2,s3;
	vector<string> board;
	vector<string> b2;
	char buf[100];

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0..out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d",&N,&K);

		board.clear();
		red = 0;
		blue = 0;

		for(i=0; i<N; i++)
		{
			scanf("%s",&buf);
			s1 = buf;
			for(j=N-1; j>=0; j--)
			{
				if(s1[j] != '.')
				{
					for(k=j+1; k<=N-1 && s1[k]=='.'; k++)
					{
						s1[k] = s1[k-1];
						s1[k-1] = '.';
					}
				}
			}
			board.push_back(s1);
		}

		for(i=0; i<N; i++)
			for(j=0; j<N; j++)
				if(board[i][j] != '.')
				{
					if(board[i][j] == 'R' && red == 1)
						continue;
					if(board[i][j] == 'B' && blue == 1)
						continue;

					for(count=1,a=j+1; a<=N-1 && board[i][a]==board[i][j] && count!=K; a++,count++);
					if(count != K)
						for(count=1,a=i+1; a<=N-1 && board[a][j]==board[i][j] && count!=K; a++,count++);
					if(count != K)
						for(count=1,a=i+1,b=j+1; a<=N-1 && b<=N-1 && board[a][b]==board[i][j] && count!=K; a++,b++,count++);
					if(count != K)
						for(count=1,a=i-1,b=j+1; a>=0 && b<=N-1 && board[a][b]==board[i][j] && count!=K; a--,b++,count++);

					if(count == K)
					{
						if(board[i][j] == 'R')
							red = 1;
						else if(board[i][j] == 'B')
							blue = 1;
					}
				}




		if(red && blue)
			printf("Case #%d: Both\n",CASE);
		else if(red)
			printf("Case #%d: Red\n",CASE);
		else if(blue)
			printf("Case #%d: Blue\n",CASE);
		else
			printf("Case #%d: Neither\n",CASE);



	}




}