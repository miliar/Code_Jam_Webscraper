#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		char array[4][4];
		bool oflag = false;
		bool xflag = false;
		int ocount, xcount;
		int tflag;
		int vacant = 0;

		// Scan and Rows check
		for (int j = 0; j < 4; j++)
		{
			ocount = xcount = 0;
			tflag = false;
			for (int k = 0; k < 4; k++)
			{
				cin >> array[j][k];
				switch (array[j][k])
				{
					case 'X':
						xcount++;
						break;
						
					case 'O':
						ocount++;
						break;

					case 'T':
						tflag = true;
						break;

					case '.':
						vacant++;
						break;
				}
			}
			if (xcount == 4 || (xcount == 3 && tflag))
			{
				xflag = true;
			} 
			else if (ocount == 4 || (ocount == 3 && tflag))
			{
				oflag = true;
			}
		}

		// Columns check
		if (!xflag && !oflag)
		{
			for (int j = 0; j < 4; j++)
			{
				ocount = xcount = 0;
				tflag = false;
				for (int k = 0; k < 4; k++)
				{
					switch (array[k][j])
					{
						case 'X':
							xcount++;
							break;

						case 'O':
							ocount++;
							break;

						case 'T':
							tflag = true;
							break;
					}
				}
				if (xcount == 4 || (xcount == 3 && tflag))
				{
					xflag = true;
				} 
				else if (ocount == 4 || (ocount == 3 && tflag))
				{
					oflag = true;
				}
			}
		}

		// Diagonal check
		if (!xflag && !oflag)
		{
			ocount = xcount = 0;
			tflag = false;
			for (int j = 0; j < 4; j++)
			{
				switch (array[j][j])
				{
					case 'X':
						xcount++;
						break;

					case 'O':
						ocount++;
						break;

					case 'T':
						tflag = true;
						break;
				}
			}
			if (xcount == 4 || (xcount == 3 && tflag))
			{
				xflag = true;
			} 
			else if (ocount == 4 || (ocount == 3 && tflag))
			{
				oflag = true;
			}
		}

		if (!xflag && !oflag)
		{
			ocount = xcount = 0;
			tflag = false;
			for (int j = 0; j < 4; j++)
			{
				switch (array[j][3 - j])
				{
					case 'X':
						xcount++;
						break;

					case 'O':
						ocount++;
						break;

					case 'T':
						tflag = true;
						break;
				}
			}
			if (xcount == 4 || (xcount == 3 && tflag))
			{
				xflag = true;
			} 
			else if (ocount == 4 || (ocount == 3 && tflag))
			{
				oflag = true;
			}
		}

		cout << "Case #" << (i + 1) << ": ";
		if (xflag)
		{
			cout << "X won";
		}
		else if (oflag)
		{
			cout << "O won";
		}
		else if (vacant == 0)
		{
			cout << "Draw";
		}
		else
		{
			cout << "Game has not completed";
		}
		cout << endl;
	}
}
