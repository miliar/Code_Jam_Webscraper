#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for(int i=1;i<=T;++i)
	{
		string temp;
		getline(fin,temp);
		string str[4];
		for(int j=0;j<4;++j)
			getline(fin,str[j]);
		bool xWin = false,oWin = false,draw = false;
		for(int k=0;k<4;++k)
		{
			if((str[k][0] == 'X' || str[k][0] == 'T') && (str[k][1] == 'X' || str[k][1] == 'T') && (str[k][2] == 'X' || str[k][2] == 'T') && (str[k][3] == 'X' || str[k][3] == 'T')) 
			{
				xWin = true;
				break;
			}
			if((str[k][0] == 'O' || str[k][0] == 'T') && (str[k][1] == 'O' || str[k][1] == 'T') && (str[k][2] == 'O' || str[k][2] == 'T') && (str[k][3] == 'O' || str[k][3] == 'T')) 
			{
				oWin = true;
				break;
			}
		}
		if(!xWin && !oWin)
		{
			for(int k=0;k<4;++k)
			{
				if((str[0][k] == 'X' || str[0][k] == 'T') && (str[1][k] == 'X' || str[1][k] == 'T') && (str[2][k] == 'X' || str[2][k] == 'T') && (str[3][k] == 'X' || str[3][k] == 'T')) 
				{
					xWin = true;
					break;
				}
				if((str[0][k] == 'O' || str[0][k] == 'T') && (str[1][k] == 'O' || str[1][k] == 'T') && (str[2][k] == 'O' || str[2][k] == 'T') && (str[3][k] == 'O' || str[3][k] == 'T')) 
				{
					oWin = true;
					break;
				}
			}
		}
		if(!xWin && !oWin)
		{
			if((str[0][0] == 'X' || str[0][0] == 'T') && (str[1][1] == 'X' || str[1][1] == 'T') && (str[2][2] == 'X' || str[2][2] == 'T') && (str[3][3] == 'X' || str[3][3] == 'T')) 
			{
				xWin = true;
			}
			if((str[0][0] == 'O' || str[0][0] == 'T') && (str[1][1] == 'O' || str[1][1] == 'T') && (str[2][2] == 'O' || str[2][2] == 'T') && (str[3][3] == 'O' || str[3][3] == 'T')) 
			{
				oWin = true;
			}
			if((str[3][0] == 'X' || str[3][0] == 'T') && (str[2][1] == 'X' || str[2][1] == 'T') && (str[1][2] == 'X' || str[1][2] == 'T') && (str[0][3] == 'X' || str[0][3] == 'T')) 
			{
				xWin = true;
			}
			if((str[3][0] == 'O' || str[3][0] == 'T') && (str[2][1] == 'O' || str[2][1] == 'T') && (str[1][2] == 'O' || str[1][2] == 'T') && (str[0][3] == 'O' || str[0][3] == 'T')) 
			{
				oWin = true;
			}
		}
		if(!xWin && !oWin)
		{
			int j=0,k=0;
			for(j=0;j<4;++j)
				for(k=0;k<4;++k)
				{
					if(str[j][k] == '.')
					{
						break;
					}
				}
			if(j== 4 && k == 4)
				draw = true;
		}
		if(xWin)
			fout<<"Case #"<<i<<": X won"<<endl;
		else if(oWin)
			fout<<"Case #"<<i<<": O won"<<endl;
		else if(draw)
			fout<<"Case #"<<i<<": Draw"<<endl;
		else
			fout<<"Case #"<<i<<": Game has not completed"<<endl;
	}
}