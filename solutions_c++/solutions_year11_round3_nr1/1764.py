#include "codejam.h"

void R1C_A()
{
	int T;
	cin >> T;

	for (int testCase = 1; testCase <= T; testCase++)
	{
		int R, C;

		cin >> R;
		cin >> C;

		char* picture = new char[R*C];	

		int pos = 0;
		for (int i = 1; i <= R; i++)
		{
			char* line = new char[C];
			cin >> line;
			stringCopy(line, picture, pos);
			pos += C;
		}

		bool blueFound = true;
		bool impossible = false;

		while (blueFound && !impossible)
		{
			blueFound = false;
			for (int i = 0; i < R; i++)
			{
				for (int j = 0; j < C; j++)
				{
					if (picture[i*C+j] == '#')
					{
						blueFound = true;
						if (i+1 < R && j+1 < C)
						{
							if (picture[i*C+j] != '.')
							{
								picture[i*C+j] = '/';
							}
							else
							{
								impossible = true;
							}

							if (picture[i*C+j+1] != '.')
							{
								picture[i*C+j+1] = '\\';
							}
							else
							{
								impossible = true;
							}
							
							if (picture[(i+1)*C+j] != '.')
							{
								picture[(i+1)*C+j] = '\\';
							}
							else
							{
								impossible = true;
							}

							if (picture[(i+1)*C+j+1] != '.')
							{
								picture[(i+1)*C+j+1] = '/';
							}
							else
							{
								impossible = true;
							}							
						}
						else
						{
							impossible = true;
						}
					}
				}
			}
		}

		cout << "Case #" << testCase << ":\n";
		if (impossible)
		{
			cout << "Impossible\n";
		}
		else
		{
			for (int i = 0; i < R; i++)
			{
				for (int j = 0; j < C; j++)
				{
					cout << picture[i*C+j];
				}
				cout << "\n";
			}
		}
	}

}