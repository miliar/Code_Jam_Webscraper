#include <iostream>
#include <fstream>

using namespace std;

const int emptyStr = -1;
const int diffStr = -2;
const char *sres[] = {"X won", "O won", "Draw", "Game has not completed"};

int check (ofstream *fout, char dat[4], int Cn)
{
	int i;
	for (i = 0; i < 3; ++i)
	{
		if (dat[i] == '.')
		{
			return emptyStr;
		}

		if (dat[i] == 'T')
		{
			dat[i] = dat[i+1];
		}
		if (dat[i+1] == 'T')
		{
			dat[i+1] = dat[i];
		}


		if (dat[i] != dat[i+1])
			return diffStr;
	}

	if (dat[0] == 'X')
	{
		*fout << "Case #" << Cn << ": " << sres[0] << endl;
	}
	if (dat[0] == 'O')
	{
		*fout << "Case #" << Cn << ": " << sres[1] << endl;
	}
	return 0;
}

void getVline (char vline[4], char dat[4][4], int hidx)
{
	for (int i = 0; i < 4; ++i)
	{
		vline[i] = dat[i][hidx];
	}
}

void getHline (char hline[4], char dat[4][4], int vidx)
{
	for (int i = 0; i < 4; ++i)
	{
		hline[i] = dat[vidx][i];
	}
}

void getSline (char sline[4], char dat[4][4])
{
	for (int i = 0; i < 4; ++i)
	{
		sline[i] = dat[i][3-i];
	}
}

void getBline (char bline[4], char dat[4][4])
{
	for (int i = 0; i < 4; ++i)
	{
		bline[i] = dat[i][i];
	}
}

void acase (ofstream *fout, char dat[4][4], int Cn)
{
	char line[4];
	int i, r;
	bool hasEmpty = false;

	for (i = 0; i < 4; ++i)
	{
		getVline (line, dat, i);
		r = check (fout, line, Cn);
		if (r == 0)
			return;
		if (r == emptyStr)
			hasEmpty = true;
	}

	for (i = 0; i < 4; ++i)
	{
		getHline (line, dat, i);
		r = check (fout, line, Cn);
		if (r == 0)
			return;
		if (r == emptyStr)
			hasEmpty = true;
	}

	getSline (line, dat);
	r = check (fout, line, Cn);
	if (r == 0)
		return;
	if (r == emptyStr)
		hasEmpty = true;

	getBline (line, dat);
	r = check (fout, line, Cn);
	if (r == 0)
		return;
	if (r == emptyStr)
		hasEmpty = true;

	if (hasEmpty)
		*fout << "Case #" << Cn << ": " << sres[3] << endl;
	else
		*fout << "Case #" << Cn << ": " << sres[2] << endl;
}

void pdat (char dat[4][4])
{
	for (int v = 0; v < 4; ++v)
	{
		for (int h = 0; h < 4; ++h)
		{
			cout << dat[v][h] << " ";
		}
		cout << endl;
	}
}

int main ()
{
	int tn;
	char dat[4][4];
	ifstream fin("testcase.txt");
	ofstream fout("result.txt");

	fin >> tn;
	for (int i = 0; i < tn; ++i)
	{
		for (int v = 0; v < 4; ++v)
		{
			for (int h = 0; h < 4; ++h)
			{
				fin >> dat[v][h];
			}
		}

		pdat (dat);
		acase (&fout, dat, i+1);
	}

	fin.close();
	fout.close();
	getchar();
	return 0;
}
