#include<algorithm>
#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<deque>
#include<string>
#include<map>
#include<cstring>
#include<sstream>
#include<cmath>
using namespace std;

int main()
{
	FILE *fp = fopen ("input", "r");
	FILE *fp1 = fopen ("output", "w");
	int T;
	fscanf (fp, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		char arr[4][5];
		fgets (arr[0], 6, fp); //Dummy
		for (int i = 0; i < 4; i++)
			fgets (arr[i], 6, fp);
		int result = 0;
		int cX = 0, cO = 0, cT = 0, cD = 0;
		//Check rows
		for (int i = 0; i < 4; i++)
		{
			cX = 0, cO = 0, cT = 0;
			for (int j = 0; j < 4; j++)
			{
				if (arr[i][j] == 'X')
					cX++;
				else if (arr[i][j] == 'O')
					cO++;
				else if (arr[i][j] == 'T')
					cT++;
				else
					cD++;
				if (cX+cT == 4)
				{
					result = 1;
					break;
				}
				if (cO+cT == 4)
				{
					result = 2;
					break;
				}
			}
		}
		if (result != 0)
			goto done;
		//Check columns
		for (int j = 0; j < 4; j++)
		{
			cX = 0, cO = 0, cT = 0;
			for (int i = 0; i < 4; i++)
			{
				if (arr[i][j] == 'X')
					cX++;
				else if (arr[i][j] == 'O')
					cO++;
				else if (arr[i][j] == 'T')
					cT++;
				else
					cD++;
				if (cX+cT == 4)
				{
					result = 1;
					break;
				}
				if (cO+cT == 4)
				{
					result = 2;
					break;
				}
			}
		}
		if (result != 0)
			goto done;
		//Check diagonals
		cX = 0, cO = 0, cT = 0;
		for (int i = 0; i < 4; i++)
		{
			if (arr[i][i] == 'X')
				cX++;
			else if (arr[i][i] == 'O')
				cO++;
			else if (arr[i][i] == 'T')
				cT++;
			else
				cD++;
			if (cX+cT == 4)
			{
				result = 1;
				break;
			}
			if (cO+cT == 4)
			{
				result = 2;
				break;
			}
		}
		if (result != 0)
			goto done;
		cX = 0, cO = 0, cT = 0;
		for (int i = 0; i < 4; i++)
		{
			if (arr[i][3-i] == 'X')
				cX++;
			else if (arr[i][3-i] == 'O')
				cO++;
			else if (arr[i][3-i] == 'T')
				cT++;
			else
				cD++;
			if (cX+cT == 4)
			{
				result = 1;
				break;
			}
			if (cO+cT == 4)
			{
				result = 2;
				break;
			}
		}
		done:
		if (result == 1)
			fprintf (fp1, "Case #%d: X won\n", (t+1));
		else if (result == 2)
			fprintf (fp1, "Case #%d: O won\n", (t+1));
		else
		{
			if (cD == 0)
				fprintf (fp1, "Case #%d: Draw\n", (t+1));
			else
				fprintf (fp1, "Case #%d: Game has not completed\n", (t+1));
		}
	}
	return 0;
}
