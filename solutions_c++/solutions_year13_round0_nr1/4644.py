#include <iostream>

using namespace std;

bool rowCheck()
{
	
}

int main()
{
	int tc,casei,i,j,won,draw,notComp,proceed,hasDot;
	string board[5];
	cin>>tc;
	char player,wonPlayer;
	
	for(casei=1;casei<=tc;casei++)
	{
		proceed=1;
		won=draw=notComp=hasDot=0;
		wonPlayer=player='Q';

		for(i=0;i<4;i++)
		{
			cin>>board[i];
		}
	
		//cout<<"****board****\n";		
		hasDot=0;
		for(i=0;i<4&&!hasDot;i++)
		{
			for(j=0;j<4&&!hasDot;j++)
			//cout<<board[i][j];
			//cout<<"\n";
				if(board[i][j]=='.') hasDot=1;
		}
		
	
		while(proceed)
		{

			for(i=0;i<4 && proceed;i++)
			{
				player =  board[i][0];
				if(player == 'T') player = board[i][1];

				if(player!='.') 
				{

				if((board[i][1]==player || board[i][1]== 'T') && 
				   (board[i][2]==player || board[i][2]== 'T') &&
				   (board[i][3]==player || board[i][3]== 'T'))
				{
					won=1;
					wonPlayer=player;
					proceed=0;
				}
				}
			}

			//if(!proceed) continue;
			
			for(j=0;j<4 && proceed;j++)
			{
				player =  board[0][j];
				if(player == 'T') player = board[1][j];
				
				if(player!='.') 
				{
				if((board[1][j]==player || board[1][j]== 'T') && 
				   (board[2][j]==player || board[2][j]== 'T') &&
				   (board[3][j]==player || board[3][j]== 'T'))
				{
					won=1;
					wonPlayer=player;
					proceed=0;
				}
				}
			}

			if(proceed)
			{
				player =  board[0][0];
				if(player == 'T') player = board[1][1];

				if(player!='.') 
				{
				if((board[1][1]==player || board[1][1]== 'T') && 
				   (board[2][2]==player || board[2][2]== 'T') &&
				   (board[3][3]==player || board[3][3]== 'T'))
				{
					won=1;
					wonPlayer=player;
					proceed=0;
				}
				}
			}

			if(proceed)
			{
				player =  board[0][3];
				if(player == 'T') player = board[1][2];
				
				if(player!='.') 
				{
				if((board[1][2]==player || board[1][2]== 'T') && 
				   (board[2][1]==player || board[2][1]== 'T') &&
				   (board[3][0]==player || board[3][0]== 'T'))
				{
					won=1;
					wonPlayer=player;
					proceed=0;
				}
				}
			}
			
			proceed=0;

		}

		cout<<"Case #"<<casei<<": ";

		if(won)  cout<<wonPlayer<<" won"<<"\n";
		else if(hasDot) cout<<"Game has not completed\n";
		else cout<<"Draw\n";


	}

return 0;
}
