#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
	int N;
	char pan[4][1000];
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin>>N;
	for(int i=0;i<N;i++)
	{
		memset(pan,0,sizeof(pan));
		for(int j=0;j<4;j++)
		{
			fin>>pan[j];
		}
		char code=0;
		bool flag=true;
		for(int j=0;j<4;j++)
		{
			if((pan[j][0]=='X'||pan[j][0]=='T')&&(pan[j][1]=='X'||pan[j][1]=='T')
				&&(pan[j][2]=='X'||pan[j][2]=='T')&&(pan[j][3]=='X'||pan[j][3]=='T'))
			{
				code='X';
			}
			else if((pan[j][0]=='O'||pan[j][0]=='T')&&(pan[j][1]=='O'||pan[j][1]=='T')
				&&(pan[j][2]=='O'||pan[j][2]=='T')&&(pan[j][3]=='O'||pan[j][3]=='T'))
			{
				code='O';
			}
			for(int k=0;k<4;k++)
			{
				if(pan[j][k]=='.')
					flag=false;
			}
		}
		for(int j=0;j<4;j++)
		{
			if((pan[0][j]=='X'||pan[0][j]=='T')&&(pan[1][j]=='X'||pan[1][j]=='T')
				&&(pan[2][j]=='X'||pan[2][j]=='T')&&(pan[3][j]=='X'||pan[3][j]=='T'))
			{
				code='X';
			}
			else if((pan[0][j]=='O'||pan[0][j]=='T')&&(pan[1][j]=='O'||pan[1][j]=='T')
				&&(pan[2][j]=='O'||pan[2][j]=='T')&&(pan[3][j]=='O'||pan[3][j]=='T'))
			{
				code='O';
			}
		}
		if((pan[0][0]=='X'||pan[0][0]=='T')&&(pan[1][1]=='X'||pan[1][1]=='T')
				&&(pan[2][2]=='X'||pan[2][2]=='T')&&(pan[3][3]=='X'||pan[3][3]=='T'))
		{
			code='X';
		}
		if((pan[0][0]=='O'||pan[0][0]=='T')&&(pan[1][1]=='O'||pan[1][1]=='T')
				&&(pan[2][2]=='O'||pan[2][2]=='T')&&(pan[3][3]=='O'||pan[3][3]=='T'))
		{
			code='O';
		}
		if((pan[0][3]=='X'||pan[0][3]=='T')&&(pan[1][2]=='X'||pan[1][2]=='T')
				&&(pan[2][1]=='X'||pan[2][1]=='T')&&(pan[3][0]=='X'||pan[3][0]=='T'))
		{
			code='X';
		}
		if((pan[0][3]=='O'||pan[0][3]=='T')&&(pan[1][2]=='O'||pan[1][2]=='T')
				&&(pan[2][1]=='O'||pan[2][1]=='T')&&(pan[3][0]=='O'||pan[3][0]=='T'))
		{
			code='O';
		}
		if(code=='X')
		{
			fout<<"Case #"<<i+1<<": X won"<<endl;
		}
		else if(code=='O')
		{
			fout<<"Case #"<<i+1<<": O won"<<endl;
		}
		else if(flag)
		{
			fout<<"Case #"<<i+1<<": Draw"<<endl;
		}
		else
		{
			fout<<"Case #"<<i+1<<": Game has not completed"<<endl;
		}
	}
	return 0;
}