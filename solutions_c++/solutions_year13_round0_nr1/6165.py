#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)

const int n = 4;

int main()
{
	ifstream in("A-small-attempt2.in");
	ofstream out("A-small-attempt2.out");

	int tst, arrX[4], arrO[4], arrT[4], x, o, t, gt = 0, GdiagX, GdiagO, GdiagT, PdiagX, PdiagO, PdiagT, win = 0, empt;
	char c;
	string s;

	in >> tst;

	while (gt < tst)
	{
		forn(i, n)
			arrX[i] = arrO[i] = arrT[i] = 0;

		win = empt = GdiagX = GdiagO = GdiagT = PdiagX = PdiagO = PdiagT = 0;
		forn(i, n)
		{
			getline(in, s);
			x = o = t = 0;
			forn(j, n)
			{
				in >> c;
				switch (c)
				{
				case 'X':
					x++;
					arrX[j]++;
					if (i == j)
						GdiagX++;
					if (j == n - i)
						PdiagX++;
					break;
				case 'O':
					o++;
					arrO[j]++;
					if (i == j)
						GdiagO++;
					if (j == n - i - 1)
						PdiagO++;
					break;
				case 'T':
					t++;
					arrT[j]++;
					if (i == j)
						GdiagT++;
					if (j == n - i - 1)
						PdiagT++;
					break;
				case '.':
					empt++;
				}
			}
			if (x + t == n)
				win = 1;
			if (o + t == n)
				win = 2;
		}

		if (GdiagX + GdiagT == n)
			win = 1;
		if (GdiagO + GdiagT == n)
			win = 2;

		if (PdiagX + PdiagT == n)
			win = 1;
		if(PdiagO + PdiagT == n)
			win = 2;

		forn (i, n)
		{
			if (arrX[i] + arrT[i] == n)
				win = 1;
			if (arrO[i] + arrT[i] == n)
				win = 2;
		}

		if (win == 0 && empt > 0)
			out << "Case #" << gt + 1 << ": Game has not completed" << endl;

		if (win == 0 && empt == 0)
			out << "Case #" << gt + 1 << ": Draw" << endl;

		if (win == 1)
			out << "Case #" << gt + 1 << ": X won" << endl;

		if (win == 2)
			out << "Case #" << gt + 1 << ": O won" << endl;

		gt++;
	}
		

	return 0;
}