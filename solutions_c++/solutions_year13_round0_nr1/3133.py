#include<cstdio>
#include<iostream>

using namespace std;
int board[4][4];
int check();

void main()
{
	freopen("A-large.in","r",stdin);
	freopen("a_large.out","w",stdout);
	
	int T,result;
	char temp;
	cin>>T;
	for(int i=0;i!=T;++i)
	{
		memset(board,0,sizeof(board));
		for(int j=0;j!=4;++j)
		{
			for(int k=0;k!=4;++k)
			{
				cin>>temp;
				if(temp=='X') 
					board[j][k]=1;
				if(temp=='O')
					board[j][k]=2;
				if(temp=='T')
					board[j][k]=3;
			}
		}
		result=check();
		cout<<"Case #"<<i+1<<": ";
		if(result == 1)
			cout<<"X won"<<endl;
		else if(result == 2)
			cout<<"O won"<<endl;
		else if(result == 3)
			cout<<"Draw"<<endl;
		else
			cout<<"Game has not completed"<<endl;
	}
}
int check()
{
	int count1_x,count1_y,count2_x,count2_y;
	for(int i=0;i!=4;++i)
	{
		count1_x=0;
		count1_y=0;
		count2_x=0;
		count2_y=0;
		for(int j=0;j!=4;++j)
		{
			if(board[i][j]==1 || board[i][j]==3)
			{
	
					++count1_x;
					if(count1_x==4)
						return 1;		
			}
			if(board[j][i]==1 || board[j][i]==3)
			{
					++count1_y;
					if(count1_y==4)
						return 1;
				}

			if(board[i][j]==2 || board[i][j]==3)
			{
					++count2_x;
					if(count2_x==4)
						return 2;	
			}
			if(board[j][i]==2 || board[j][i]==3)
			{
					++count2_y;
					if(count2_y==4)
						return 2;
			}
		}
	}
	count1_x=0;
	count1_y=0;
	count2_x=0;
	count2_y=0;
	for(int j=0;j!=4;++j)
	{
		if(board[j][j]==1 || board[j][j]==3)
		{
				++count1_x;
				if(count1_x==4)
					return 1;
		}
		if(board[j][j]==2 || board[j][j]==3)
		{
				++count2_x;
				if(count2_x==4)
					return 2;
		}
		if(board[3-j][j]==1 || board[3-j][j]==3)
		{
				++count1_y;
				if(count1_y==4)
					return 1;
		}
		if(board[3-j][j]==2 || board[3-j][j]==3)
		{
				++count2_y;
				if(count2_y==4)
					return 2;
		}

	}

	for(i=0;i!=4;++i)
		for(j=0;j!=4;++j)
		{
			if(board[i][j]==0)
				return 4;
		}
	return 3;
}