//#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	int C;
	char board[4][4];
	ifstream fin("A-large.in",ios_base::in);
	ofstream fout("A-large.out",ios_base::out);
	fin>>C;
	for(int i=0;i<C;i++)
	{
		bool dot=false;
		char winner;
		for (int j=0;j<4;j++)
		{
			for (int k=0;k<4;k++)
			{
				fin>>board[j][k];
				if (!dot && board[j][k]=='.')
				{
					dot=true;
				}
				//cout<<board[j][k];
			}
			//cout<<endl;
		}
		bool win=false;
		for(int j=0;j<4;j++)
		{
			int ch = (board[j][0]=='T') ? 1 :0;
			if (board[j][ch]=='.') continue;
			win=true;
			for(int k=0;k<4;k++)
			{
				if (board[j][ch]!=board[j][k] && board[j][k]!='T')
				{
					win=false;
					break;
				}
				
			}
			if (win)
			{
				winner=board[j][ch];
				break;
			}
		}
		for(int j=0;!win && j<4;j++)
		{
			int ch = (board[0][j]=='T') ? 1 :0;
			if (board[ch][j]=='.') continue;
			win=true;
			for(int k=0;k<4;k++)
			{
				if (board[ch][j]!=board[k][j] && board[k][j]!='T')
				{
					win=false;
					break;
				}

			}
			if (win)
			{
				winner=board[ch][j];
				break;
			}
		}
		if (!win)
		{
			int ch = (board[0][0]=='T') ? 1 :0;
			win=true;
			if (board[ch][ch]=='.')
				win=false;
			else
			{
				for(int j=0;j<4;j++)
				{
					if (board[ch][ch]!=board[j][j] && board[j][j]!='T')
					{
						win=false;
						break;
					}
				}
			}
			if (win)
			{
				winner=board[ch][ch];
			}
			else
			{
				int ch = (board[0][3]=='T') ? 3 :0;
				win=true;
				if (board[ch][3-ch]=='.')
					win=false;
				else
				{
					for(int j=0,k=3;j<4;j++,k--)
					{
						if (board[ch][3-ch]!=board[j][k] && board[j][k]!='T')
						{
							win=false;
							break;
						}
					}
				}
				if (win)
				{
					winner=board[ch][3-ch];
				}
			}
		}
		if (win)
		{
			fout<<"Case #"<<i+1<<": "<<winner<<" won"<<endl;
		} 
		else
		{
			if (dot)
			{
				fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
			} 
			else
			{
				fout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
			}
		}
	}
	fin.close();
	fout.close();
	//getchar();
}