// A_Tic-Tac-Toe-Tomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	fin>>t;
	for(int n=0;n<t;n++)
	{
		char arr[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>arr[i][j];
			}
		}
		int count=0;
		bool end=false;

		//------------------------------------------------------------------------------------------
		int c_x=0,c_o=0;
		for(int i=0;i<4 && !end;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[i][j]=='T' || arr[i][j]=='O') c_o++;
				if(arr[i][j]=='T' || arr[i][j]=='X') c_x++;
			}
			if(c_o==4)
			{
				fout<<"Case #"<<n+1<<": O won"<<endl;
				end=true;
			}
			else if(c_x==4)
			{
				fout<<"Case #"<<n+1<<": X won"<<endl;
				end=true;
			}
			c_o=0;
			c_x=0;
		}
		//------------------------------------------------------------------------------------------
		for(int j=0;j<4 && !end;j++)
		{
			for(int i=0;i<4;i++)
			{
				if(arr[i][j]=='T' || arr[i][j]=='O') c_o++;
				if(arr[i][j]=='T' || arr[i][j]=='X') c_x++;
			}
			if(c_o==4)
			{
				fout<<"Case #"<<n+1<<": O won"<<endl;
				end=true;
			}
			else if(c_x==4)
			{
				fout<<"Case #"<<n+1<<": X won"<<endl;
				end=true;
			}
			c_o=0;
			c_x=0;
		}
		//------------------------------------------------------------------------------------------
		for(int i=0,j=0;i<4 && !end;i++,j++)
		{
			if(arr[i][j]=='T' || arr[i][j]=='O') c_o++;
			if(arr[i][j]=='T' || arr[i][j]=='X') c_x++;
			}
			if(c_o==4)
			{
				fout<<"Case #"<<n+1<<": O won"<<endl;
				end=true;
			}
			else if(c_x==4)
			{
				fout<<"Case #"<<n+1<<": X won"<<endl;
				end=true;
			}
			c_o=0;
			c_x=0;
		//-------------------------------------------------------------------------------------------
		for(int i=3,j=0;j<4 && !end;i--,j++)
		{
			if(arr[i][j]=='T' || arr[i][j]=='O') c_o++;
				if(arr[i][j]=='T' || arr[i][j]=='X') c_x++;
			}
			if(c_o==4)
			{
				fout<<"Case #"<<n+1<<": O won"<<endl;
				end=true;
			}
			else if(c_x==4)
			{
				fout<<"Case #"<<n+1<<": X won"<<endl;
				end=true;
			}
			c_o=0;
			c_x=0;
		//-------------------------------------------------------------------------------------------
		if(!end)
		{
			bool b=false;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					if(arr[i][j]=='.')
					{
						b=true;
					}
				}
			} 
			if(b)
				fout<<"Case #"<<n+1<<": "<<"Game has not completed"<<endl;
			else 
				fout<<"Case #"<<n+1<<": "<<"Draw"<<endl;

			b=false;
			end=true;
		}

		//-------------------------------------------------------------------------------------------
	}
	return 0;
}

