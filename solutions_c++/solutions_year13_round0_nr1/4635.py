#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tc=0;
	char res[4][40] = {"X won" , "O won" , "Draw" , "Game has not completed"};
	while(tc++,t--)
	{
		int fg=-1;
		string board[4];
		for(int i=0;i<4;i++)
			cin>>board[i];
		int isdot=0;
		for(int i=0;i<4;i++)
		{
			int xc=0;
			int oc=0;
			int tcnt=0;
			for(int j=0;j<4;j++)
			{
				if(board[i][j]=='.')
					isdot=1;
				if(board[i][j]=='X')
					xc++;
				else if(board[i][j]=='O')
					oc++;
				else if(board[i][j]=='T')
					tcnt++;
			}
			if(xc==4||(xc==3&&tcnt==1))
			{
				fg=0;
				break;
			}
			if(oc==4||(oc==3&&tcnt==1))
			{
				fg=1;
				break;
			}
		}
		for(int i=0;i<4;i++)
		{
			int xc=0;
			int oc=0;
			int tcnt=0;
			for(int j=0;j<4;j++)
			{
					if(board[j][i]=='.')
					isdot=1;

				if(board[j][i]=='X')
					xc++;
				else if(board[j][i]=='O')
					oc++;
				else if(board[j][i]=='T')
					tcnt++;
			}
			if(xc==4||(xc==3&&tcnt==1))
			{
				fg=0;
				break;
			}
			if(oc==4||(oc==3&&tcnt==1))
			{
				fg=1;
				break;
			}
		}
		int xc=0,oc=0,tcnt=0;
		for(int i=0;i<4;i++)
		{
				if(board[i][i]=='.')
					isdot=1;

				if(board[i][i]=='X')
					xc++;
				else if(board[i][i]=='O')
					oc++;
				else if(board[i][i]=='T')
					tcnt++;
		}
			if(xc==4||(xc==3&&tcnt==1))
			{
				fg=0;
				
			}

				
		if(oc==4||(oc==3&&tcnt==1))
			{
				fg=1;
			
			}
	

			xc=oc=tcnt=0;
		for(int i=0;i<4;i++)
		{
				if(board[i][3-i]=='.')
					isdot=1;

				if(board[i][3-i]=='X')
					xc++;
				else if(board[i][3-i]=='O')
					oc++;
				else if(board[i][3-i]=='T')
					tcnt++;
		}
			if(xc==4||(xc==3&&tcnt==1))
			{
				fg=0;
				
			}
		if(oc==4||(oc==3&&tcnt==1))
			{
				fg=1;
			
			}
		if((fg!=0&&fg!=1))
		{
			if(isdot)
				fg=3;
			else fg=2;
		}
		
		cout<<"Case #"<<tc<<": "<<res[fg]<<endl;
	







		



	}
	return 0;
}
