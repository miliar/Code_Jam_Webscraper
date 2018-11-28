#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("data.in");
	ofstream outfile;
	outfile.open("data.out");

	int T;
	infile>>T;

	for (int caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		char a[5][5];
		string answer = "";
		bool thereisdot = false;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				infile>>a[i][j];
				if (a[i][j] == '.')
				{
					thereisdot = true;
				}
			}
		}
		
		//rowx
		for (int row = 1; row <= 4; row++)
		{
			int numX = 0;
			int numO = 0;
			for (int col = 1; col <= 4;col++)
			{
				if (a[row][col] == 'X' || a[row][col] == 'T')
				{
					numX++;
				}
				if (a[row][col] == 'O' || a[row][col] == 'T')
				{
					numO++;
				}
			}
			if (numX == 4)
			{
				answer = "X won";
				break;
			}
			if (numO == 4)
			{
				answer = "O won";
				break;
			}

		}

		//col
		for (int col = 1; col <= 4; col++)
		{
			int numX = 0;
			int numO = 0;
			for (int row = 1; row <= 4;row++)
			{
				if (a[row][col] == 'X' || a[row][col] == 'T')
				{
					numX++;
				}
				if (a[row][col] == 'O' || a[row][col] == 'T')
				{
					numO++;
				}
			}
			if (numX == 4)
			{
				answer = "X won";
				break;
			}
			if (numO == 4)
			{
				answer = "O won";
				break;
			}

		}

		//dig
		int numX = 0;
		int numO = 0;
		for (int col = 1; col <= 4; col++)
		{
			
			if (a[col][col] == 'X' || a[col][col] == 'T')
			{
				numX++;
			}
			if (a[col][col] == 'O' || a[col][col] == 'T')
			{
				numO++;
			}
		}

			if (numX == 4)
			{
				answer = "X won";

			}
			if (numO == 4)
			{
				answer = "O won";

			}

			numX = 0;
			numO = 0;
			for (int col = 1; col <= 4; col++)
		{
			
			if (a[col][5-col] == 'X' || a[col][5-col] == 'T')
			{
				numX++;
			}
			if (a[col][5-col] == 'O' || a[col][5-col] == 'T')
			{
				numO++;
			}
		}

			if (numX == 4)
			{
				answer = "X won";

			}
			if (numO == 4)
			{
				answer = "O won";

			}





			if (answer == "")
			{
				if (thereisdot)
				{
					answer = "Game has not completed";
				}
				else
				{
					answer = "Draw";
				}
			}

			outfile<<"Case #"<<caseIndex<<": "<<answer<<endl;
		
		

	}

	infile.close();
	outfile.close();
	return 0;
}