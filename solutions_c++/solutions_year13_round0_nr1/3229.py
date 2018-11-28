#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	ifstream fin("A\\A-large.in");
	int cnt;
	fin >> cnt;

	char *final[4] = {
		"X won",
		"O won",
		"Draw",
		"Game has not completed"
	};

	int ofield[2][5];
	int xfield[2][5];
	bool bHasEmpty;
	char in;
	int res = 0;

	int dia = 0;
	ofstream fout("output.txt");
	for(int i=0; i<cnt; i++)
	{
		memset(ofield, 0, sizeof(ofield));
		memset(xfield, 0, sizeof(xfield));
		bHasEmpty = false;

		for(int j=0; j<4; j++)
		{
			for(int k = 0; k<4; k++)
			{
				fin >> in;

				if(j==k)
				{
					dia = 0;
				}
				else if( j+k == 3)
				{
					dia = 1;
				}
				else
				{
					dia = -1;
				}

				switch(in)
				{
				case '.':
					bHasEmpty = true;
					break;
				case 'X':
					//xfield[j][k] = 'X';
					xfield[0][k]++;
					xfield[1][j]++;
					if(dia >= 0)
						xfield[dia][4]++;
					break;
				case 'O':
					ofield[0][k]++;
					ofield[1][j]++;
					if(dia >= 0)
						ofield[dia][4]++;
					break;
				case 'T':
					xfield[0][k]++;
					xfield[1][j]++;
					ofield[0][k]++;
					ofield[1][j]++;
					if(dia >= 0)
					{
							xfield[dia][4]++;
							ofield[dia][4]++;
					}

					break;
				}
			}
		}


		res = -1;
		for(int j = 0; j<5; j++)
		{
			if( (xfield[0][j] == 4) || (xfield[1][j] == 4))
			{
				res = 0;
			}
			else if( (ofield[0][j] == 4) || (ofield[1][j] == 4))
			{
				res = 1;
			}
		}

		if(res <0)
		{
			if(!bHasEmpty)
			{
				res = 2;
			}
			else
			{
				res = 3;
			}
		}


		fout << "Case #" << i+1 << ": " << final[res] << endl;

	}

}