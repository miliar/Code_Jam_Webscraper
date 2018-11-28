#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int T;
int R;
int C;
std::vector<string> Table;
std::vector<string> Result;
bool Flag;

bool Safe[50][50];

int IniSafe()
{
	int sum = 0;
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			if(Table[i][j] == '#')
			{
				Safe[i][j] = true;
				sum++;
			}
			else
			{
				Safe[i][j] = false;
			}
		}
	}
	return sum;
}

bool JudgeTable(int NN)
{
	if(NN == 0)
		return true;
	for(int i = 0; i < R - 1; i++)
	{
		for(int j = 0; j < C - 1; j++)
		{
			if(Table[i][j] == '#')
			{
				if(Table[i + 1][j] == '#' && Table[i][j + 1] == '#' && Table[i + 1][j + 1] == '#')
				{
					Table[i][j] = '/';
					Table[i+1][j] = '\\';
					Table[i][j+1] = '\\';
					Table[i+1][j+1] = '/';
					return JudgeTable(NN - 1);
				}
				else 
				{
					return false;
				}
			}
		}
	}
	return true;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large-ans.out");
	int sum = 0;
	fin>>T;
	for(int i = 0; i < T; i++)
	{
		fin>>R>>C;
		Table.clear();
		Table.resize(R);
		Result.clear();
		Result.resize(R);
		Flag = false;
		sum  = 0;
		for(int j = 0; j < R; j++)
		{
			fin>>Table[j];
			Result[j] = Table[j];
		}
		sum = IniSafe();
		if(sum % 4 != 0)
		{
			Flag = false;
		}
		else
		{
			Flag = JudgeTable(sum/4);
		}
		fout<<"Case #"<<i+1<<":\n";
		if(Flag == true)
		{
			for(int r = 0; r < R; r++)
			{
				for(int c = 0; c < C; c++)
				{
					fout<<Table[r][c];
				}
				fout<<"\n";
			}
		}
		else
		{
			fout<<"Impossible\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}
