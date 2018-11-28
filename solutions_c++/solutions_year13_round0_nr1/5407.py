#include <iostream>
#include <fstream>

using namespace std;

char chkRow(char **a, int r)
{
	char k = a[r][0];
	if (k == 'T') k = a[r][1];
	for (int i = 1; i < 4; ++i)
	{
		if (a[r][i] != k && a[r][i] != 'T') return '.';
	}
	return k;
}

char chkCol(char **a, int c)
{
	char k = a[0][c];
	if (k == 'T') k = a[1][c];
	for (int i = 1; i < 4; ++i)
	{
		if (a[i][c] != k && a[i][c] != 'T') return '.';
	}
	return k;
}

char chkCross(char **a)
{
	bool ret = true;
	char k = a[0][0];
	if (k == 'T') k = a[1][1];
	for (int i = 1; i < 4; ++i)
	{
		if (a[i][i] != k && a[i][i] != 'T')
		{
			ret = false;
			break;
		}
	}
	if (ret) return k;
	ret = true;
	k = a[0][3];
	if (k == 'T') k = a[1][2];
	for (int i = 1; i < 4; ++i)
	{
		if (a[i][3 - i] != k && a[i][3 - i] != 'T')
		{
			return '.';
		}
	}
	return k;
}

int main()
{
	int t;
	ifstream fi;
	ofstream fo;
	fi.open("F:\\t\\in");
	fo.open("F:\\t\\out", ios::trunc);
	fi >> t;
	for (int q = 1; q <= t; ++q)
	{
		fo << "Case #" << q << ": ";
		bool cp = true;
		char **a = new char *[4];
		for (int i = 0; i < 4; ++i)
		{
			a[i] = new char[4];
			for (int j = 0; j < 4; ++j)
			{
				fi >> a[i][j];
				if (a[i][j] == '.') cp = false;
			}
		}

		char k;
		for (int i = 0; i < 4; ++i)
		{
			k = chkRow(a, i);
			if (k != '.')
			{
				fo << k << " won";
				goto next;
			}
			k = chkCol(a, i);
			if (k != '.')
			{
				fo << k << " won";
				goto next;
			}
		}
		k = chkCross(a);
		if (k != '.')
		{
			fo << k << " won";
			goto next;
		}
		if (cp)
		{
			fo << "Draw";
		}
		else
		{
			fo << "Game has not completed";
		}
next:
		fo << endl;
	}
	fi.close();
	fo.close();
	return 0;
}