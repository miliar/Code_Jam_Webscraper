#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
	ifstream fin ("input.txt");
	ofstream fout ("output.txt");
	int num;
	char c[4][4];
	int i,j;
	int draw;
	fin >> num;
	int xwon=0, owon = 0;
	int flagx, flago;
	for (int k=1;k<num+1;k++)
	{
		xwon=0;
		owon=0;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				fin >> c[i][j];
	
		for (i=0;i<4;i++)
		{
			flagx = 1;
			flago = 1;
			for (j=0;j<4;j++)
			{
				if (c[i][j]=='X' || c[i][j]=='.')
					flago = 0;
				if (c[i][j] == 'O' || c[i][j]=='.')
					flagx = 0;
			}
			if (flagx)
			{
				xwon = 1;
				break;
			}
			if (flago)
			{
				owon = 1;
				break;
			}
		}
		if (!xwon && !owon)
		{
			for (j=0;j<4;j++)
			{
				flagx = 1;
				flago = 1;
				for (i=0;i<4;i++)
				{
					if (c[i][j]=='X' || c[i][j]=='.')
						flago = 0;
					if (c[i][j] == 'O' || c[i][j]=='.')
						flagx = 0;
				}
				if (flagx)
				{
					xwon = 1;
					break;
				}
				if (flago)
				{
					owon = 1;
					break;
				}
			}
		}
		if (!xwon && !owon)
		{
			flagx = 1;
			flago = 1;
			for (i=0;i<4;i++)
			{
				if (c[i][i]=='X' || c[i][i]=='.')
					flago = 0;
				if (c[i][i] == 'O' || c[i][i]=='.')
					flagx = 0;
			}

			if (flagx)
			{
				xwon = 1;
			}
			if (flago)
			{
				owon = 1;
			}
		}

		if (!xwon && !owon)
		{
			flagx = 1;
			flago = 1;
			for (i=0;i<4;i++)
			{
				if (c[i][3-i]=='X' || c[i][3-i]=='.')
					flago = 0;
				if (c[i][3-i] == 'O' || c[i][3-i]=='.')
					flagx = 0;
			}

			if (flagx)
			{
				xwon = 1;
			}
			if (flago)
			{
				owon = 1;
			}
		}

		if (xwon)
			fout << "Case #" << k << ": X won" << endl;
		else if (owon)
			fout << "Case #" << k << ": O won" << endl;
		else
		{
			draw=1;
			for (i=0;i<4;i++)
				for (j=0;j<4;j++)
					if (c[i][j] == '.')
						draw=0;
			if (draw)
				fout << "Case #" << k << ": Draw" << endl;
			else
				fout << "Case #" << k << ": Game has not completed" << endl;
		}
	}
  
  
  

	fin.close();
	fout.close();
	system("pause");

	return 0;
}