#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-s.out", ios::out);
	int T;
	infile >> T;
	int testcase;
	for (testcase = 1;testcase <= T;testcase++)
	{
		char m[4][4];
		int i, j;
		for (i = 0;i < 4;i++)
		{
			for (j = 0;j < 4;j++)
			{
				infile >> m[i][j];
			}
		}

		bool flagx = false, flago = false;
		int cntx, cntt, cnto, cntall = 0;
		for (i = 0;i < 4;i++)
		{
			cntx = 0;
			cntt = 0;
			cnto = 0;
			for (j = 0;j < 4;j++)
			{
				if (m[i][j] != '.')
				{
					cntall ++;
					if (m[i][j] == 'X')
						cntx++;
					if (m[i][j] == 'O')
						cnto++;
					if (m[i][j] == 'T')
						cntt++;
				}
			}
			if (cntx + cntt == 4)
			{
				flagx = true;
				break;
			}
			if (cnto + cntt == 4)
			{
				flago = true;
				break;
			}
		}

		for (j = 0;j < 4;j++)
		{
			cntx = 0;
			cntt = 0;
			cnto = 0;
			for (i = 0;i < 4;i++)
			{
				if (m[i][j] != '.')
				{
					//cntall ++;
					if (m[i][j] == 'X')
						cntx++;
					if (m[i][j] == 'O')
						cnto++;
					if (m[i][j] == 'T')
						cntt++;
				}
			}
			if (cntx + cntt == 4)
			{
				flagx = true;
				break;
			}
			if (cnto + cntt == 4)
			{
				flago = true;
				break;
			}
		}

		cntx = 0;
		cntt = 0;
		cnto = 0;
		for (i = 0;i < 4;i++)
		{
			if (m[i][i] != '.')
			{
				//cntall ++;
				if (m[i][i] == 'X')
					cntx++;
				if (m[i][i] == 'O')
					cnto++;
				if (m[i][i] == 'T')
					cntt++;
			}

			if (cntx + cntt == 4)
			{
				flagx = true;
				break;
			}
			if (cnto + cntt == 4)
			{
				flago = true;
				break;
			}
		}

		cntx = 0;
		cntt = 0;
		cnto = 0;
		for (i = 0;i < 4;i++)
		{
			if (m[i][3-i] != '.')
			{
				//cntall ++;
				if (m[i][3-i] == 'X')
					cntx++;
				if (m[i][3-i] == 'O')
					cnto++;
				if (m[i][3-i] == 'T')
					cntt++;
			}

			if (cntx + cntt == 4)
			{
				flagx = true;
				break;
			}
			if (cnto + cntt == 4)
			{
				flago = true;
				break;
			}
		}

		outfile << "Case #" << testcase << ": ";
		if (flagx)
			outfile << "X won";
		else
		{
			if (flago)
				outfile << "O won";
			else
			{
				if (cntall == 16)
					outfile << "Draw";
				else
					outfile << "Game has not completed";
			}
		}
		outfile << endl;
	}
	return 0;
}