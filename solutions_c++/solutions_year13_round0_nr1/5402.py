#include<algorithm>
#include<iostream>
#include<vector>
#include<stdio.h>
#include<fstream>
char tictac[4][4];
using namespace std;
int main()
{
	fstream fin("tictac.txt");
	fstream fout("out.txt", ios::out);
	int T;
	fin>>T;

	for(int round=1;round<=T;round++)
	{
			bool iscomplete=true;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>tictac[i][j];
				if(tictac[i][j]=='.')
				{
					iscomplete=false;
				}
			}
		}
			bool win=true;
			char winplayer;
		for(int i=0;i<4;i++)
		{
			win=true;
			
			for(int j=0;j<3;j++)
			{
				if(tictac[i][0]=='.')
				{
				win=false;
				break;
				}
				if(tictac[i][j]==tictac[i][j+1]||tictac[i][j]=='T'||tictac[i][j+1]=='T')
				{
					if(tictac[i][j]!='T')
					{
						winplayer=tictac[i][j];
					}
					else
					{
						winplayer=tictac[i][j+1];
					}
				}
				else
				{
					win=false;
					break;
				}
			}
			if(win)
			{
				break;
			}
		}
		if(win&&winplayer!='.')
		{
			fout<<"Case #"<<round<<": "<<winplayer<<" won"<<endl;
			continue;
		}
		for(int j=0;j<4;j++)
		{
			win=true;
			for(int i=0;i<3;i++)
			{
				if(tictac[0][j]=='.')
				{
				win=false;
				break;
				}
				if(tictac[i][j]==tictac[i+1][j]||tictac[i][j]=='T'||tictac[i+1][j]=='T')
				{
					if(tictac[i][j]!='T')
					{
						winplayer=tictac[i][j];
					}
					else
					{
						winplayer=tictac[i+1][j];
					}
				}
				else
				{
					win=false;
					break;
				}
			}
			if(win)
			{
				break;
			}
		}
		if(win&&winplayer!='.')
		{
			fout<<"Case #"<<round<<": "<<winplayer<<" won"<<endl;
			continue;
		}
		win=true;
		for(int i=0;i<3;i++)
		{
				if(tictac[0][0]=='.')
			{
				win=false;
				break;
			}
			if(tictac[i][i]==tictac[i+1][i+1]||tictac[i][i]=='T'||tictac[i+1][i+1]=='T')
				{
					if(tictac[i][i]!='T')
					{
						winplayer=tictac[i][i];
					}
					else
					{
						winplayer=tictac[i+1][i+1];
					}
				}
				else
				{
					win=false;
					break;
				}
		}
		if(win&&winplayer!='.')
		{
			fout<<"Case #"<<round<<": "<<winplayer<<" won"<<endl;
			continue;
		}
		win=true;
		for(int i=0;i<3;i++)
		{
			if(tictac[0][3]=='.')
			{
				win=false;
				break;
			}
			if(tictac[i][3-i]==tictac[i+1][2-i]||tictac[i][3-i]=='T'||tictac[i+1][2-i]=='T')
				{
					if(tictac[i][3-i]!='T')
					{
						winplayer=tictac[i][3-i];
					}
					else
					{
						winplayer=tictac[i+1][2-i];
					}
				}
				else
				{
					win=false;
					break;
				}
		}
		if(win&&winplayer!='.')
		{
			fout<<"Case #"<<round<<": "<<winplayer<<" won"<<endl;
			continue;
		}
		if(iscomplete)
		{
			fout<<"Case #"<<round<<": Draw"<<endl;
		}
		else
		{
			fout<<"Case #"<<round<<": Game has not completed"<<endl;
		}
	}
}
