#include <iostream> 
#include <fstream>
using namespace std;
char a[4][4];
int judgestate(char (&a)[4][4])
{
	bool flag;
	for (int i=0; i<4; i++)
	{
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (!((a[i][j] == 'X') || (a[i][j] == 'T')))
			{
				flag = false;
				break;
			}
		}
		if (flag) return 1;
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (!((a[j][i] == 'X') || (a[j][i] == 'T')))
			{
				flag = false;
				break;
			}
		}
		if (flag) return 1;
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (!((a[i][j] == 'O') || (a[i][j] == 'T')))
			{
				flag = false;
				break;
			}
		}
		if (flag) return 2;
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (!((a[j][i] == 'O') || (a[j][i] == 'T')))
			{
				flag = false;
				break;
			}
		}
		if (flag) return 2;
	}
	flag = true;
	for (int i=0; i<4; i++)
	{
		if (!((a[i][i] == 'X') || (a[i][i] == 'T')))
		{
			flag = false;
			break;
		}
	}
	if (flag) return 1;
	flag = true;	
	for (int i=0; i<4; i++)
	{
		if (!((a[i][3-i] == 'X') || (a[i][3-i] == 'T')))
		{
			flag = false;
			break;
		}
	}
	if (flag) return 1;
	flag = true;
	for (int i=0; i<4; i++)
	{
		if (!((a[i][i] == 'O') || (a[i][i] == 'T')))
		{
			flag = false;
			break;
		}
	}
	if (flag) return 2;
	flag = true;	
	for (int i=0; i<4; i++)
	{
		if (!((a[i][3-i] == 'O') || (a[i][3-i] == 'T')))
		{
			flag = false;
			break;
		}
	}
	if (flag) return 2;
	flag = true;
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			if (a[i][j] == '.')
			{
				flag = false;
				break;
			}
		}
	}
	if (!flag) return 4;
	if (flag) return 3;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for (int i=0; i<t; i++)
	{
		fout << "Case #" << i+1;
		fout << ": ";
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
				fin >> a[j][k];
		switch (judgestate(a))
		{
			case 1: fout << "X won" << endl;
					break;
			case 2: fout << "O won" << endl;
					break;
			case 3: fout << "Draw" << endl; 
					break;
			case 4: fout << "Game has not completed" << endl;
					break;
			default: break;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
