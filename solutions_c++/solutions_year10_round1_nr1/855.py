#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	ifstream fin("A.in", ios_base::in);
	ofstream fout("A.out", ios_base::out);

	int t, n, k;

	fin >> t;
	for (int count = 0; count != t; ++count)
	{
		fin >> n >> k;
		char table[n][n];

		for (int i = 0; i != n; ++i)
		{
			for (int j = 0; j != n; ++j)
				fin >> table[i][j];
		}

		// rotate
		for (int i = n - 1; i >= 0; --i)
		{
			int pos = n - 1;
			for (int j = n - 1; j >= 0; --j)
			{
				if (table[i][j] != '.')
				{
					table[i][pos] = table[i][j];
					if (j != pos) table[i][j] = '.';
					--pos;
				}
			}
		}

		// find winner
		bool winner[2] = {false, false};
		for (int i = n - 1; i >= 0; --i)
		{
			for (int j = n - 1; j >= 0; --j)
			{
				if (table[i][j] == '.') break;
				bool rf = true;
				bool cf = true;
				bool df = true;
				bool d2f = true;
				for (int h = 1; h != k; ++h)
				{
					if (j - h < 0) rf = df = d2f = false;
					if (i - h < 0) cf = df = false;
					if (i + h >= n) d2f = false;
					if (rf && (j - h >= 0) && table[i][j - h] != table[i][j]) rf = false;
					if (cf && (i - h >= 0) && table[i - h][j] != table[i][j]) cf = false;
					if (df && (i - h >= 0) && (j - h >= 0) && table[i - h][j - h] != table[i][j]) df = false;
					if (d2f && (i + h >= 0) && (j - h < n) && table[i + h][j - h] != table[i][j]) d2f = false;
				}
				if (rf || cf || df || d2f) winner[table[i][j] == 'R'] = true;
			}
		}

		// output
		fout << "Case #" << (count + 1) << ": ";
		if (winner[0] && winner[1]) fout << "Both";
		else if (winner[0] && !winner[1]) fout << "Blue";
		else if (!winner[0] && winner[1]) fout << "Red";
		else fout << "Neither";
		fout << endl;

	}

	fin.close();
	fout.close();

	return 0;
}

