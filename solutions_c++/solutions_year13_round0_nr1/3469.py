#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin("data.in");
ofstream fout("result.out");

char check_win(string map[])
{
	for(int i=0;i<4;++i)
	{
		bool is_x=true;
		for(int j=0;j<4;++j)
			if(map[i][j]!='X'&&map[i][j]!='T')
			{
				is_x=false;
				break;
			}
		if(is_x)
			return 'X';
		
		bool is_o=true;
		for(int j=0;j<4;++j)
			if(map[i][j]!='O'&&map[i][j]!='T')
			{
				is_o=false;
				break;
			}
		if(is_o)
			return 'O';
	}

	for(int j=0;j<4;++j)
	{
		bool is_x=true;
		for(int i=0;i<4;++i)
			if(map[i][j]!='X'&&map[i][j]!='T')
			{
				is_x=false;
				break;
			}
		if(is_x)
			return 'X';
		
		bool is_o=true;
		for(int i=0;i<4;++i)
			if(map[i][j]!='O'&&map[i][j]!='T')
			{
				is_o=false;
				break;
			}
		if(is_o)
			return 'O';
	}

	bool is_x=true;
	for(int i=0;i<4;++i)
		if(map[i][i]!='X'&&map[i][i]!='T')
		{
			is_x=false;
			break;
		}
	if(is_x)
		return 'X';

	bool is_o=true;
	for(int i=0;i<4;++i)
		if(map[i][i]!='O'&&map[i][i]!='T')
		{
			is_o=false;
			break;
		}
	if(is_o)
		return 'O';

	is_x=true;
	for(int i=0;i<4;++i)
		if(map[i][3-i]!='X'&&map[i][3-i]!='T')
		{
			is_x=false;
			break;
		}
	if(is_x)
		return 'X';

	is_o=true;
	for(int i=0;i<4;++i)
		if(map[i][3-i]!='O'&&map[i][3-i]!='T')
		{
			is_o=false;
			break;
		}
	if(is_o)
		return 'O';

	return '.';
}

int main()
{
	int t;
	fin>>t;
	for(int case_no=1;case_no<=t;++case_no)
	{
		fout<<"Case #"<<case_no<<": ";
		string map[4];
		for(int i=0;i<4;++i)
			fin>>map[i];
		char result=check_win(map);
		if(result=='X'||result=='O')
		{
			fout<<result<<" won"<<endl;
		}
		else
		{
			bool is_draw=true;
			for(int i=0;i<4;++i)
				for(int j=0;j<4;++j)
					if(map[i][j]=='.')
					{
						is_draw=false;
						break;
					}
			if(is_draw)
				fout<<"Draw"<<endl;
			else
				fout<<"Game has not completed"<<endl;
		}
	}
}