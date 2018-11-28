#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
	ifstream inData;
	ofstream outData;
	inData.open("A-large.in.txt");
	outData.open("output.txt");
	
	int T, j, k, ret, blank;
	inData >> T;
	int B[5][5];
	char temp;
	for (int i = 0; i < T; i++)
		{
		blank = 0;
		ret = -1;
		memset(B, 0, sizeof(B));
		for (j = 0; j < 4; j++)
			for (k = 0; k < 4; k++)
				{
				inData >> temp;
				if (temp == 'X') B[j][k] = 1;
				else if (temp == 'O') B[j][k] = -1;
				else if (temp == 'T') B[j][k] = 10;
				else blank = 1;
				}
		for (j = 0; j < 4; j++)
			{
			temp = 0;
			for (k = 0; k < 4; k++)
				{
				temp += B[j][k];
				}
			if (temp == 4 || temp == 13)
				{
				outData << "Case #" << i + 1 << ": X won" << endl;
				goto done;
				}
			if (temp == -4 || temp == 7)
				{
				outData << "Case #" << i + 1 << ": O won" << endl;
				goto done;
				}
			}
		for (j = 0; j < 4; j++)
			{
			temp = 0;
			for (k = 0; k < 4; k++)
				{
				temp += B[k][j];
				}
			if (temp == 4 || temp == 13)
				{
				outData << "Case #" << i + 1 << ": X won" << endl;
				goto done;
				}
			if (temp == -4 || temp == 7)
				{
				outData << "Case #" << i + 1 << ": O won" << endl;
				goto done;
				}
			}
		temp = 0;
		for (j = 0; j < 4; j++)
			{
			temp += B[j][j];
			}
		if (temp == 4 || temp == 13)
			{
			outData << "Case #" << i + 1 << ": X won" << endl;
			goto done;
			}
		if (temp == -4 || temp == 7)
			{
			outData << "Case #" << i + 1 << ": O won" << endl;
			goto done;
			}
		temp = B[0][3] + B[1][2] + B[2][1] + B[3][0];
		if (temp == 4 || temp == 13)
			{
			outData << "Case #" << i + 1 << ": X won" << endl;
			goto done;
			}
		if (temp == -4 || temp == 7)
			{
			outData << "Case #" << i + 1 << ": O won" << endl;
			goto done;
			}
		
		if (blank != 1) outData << "Case #" << i + 1 << ": Draw"  << endl;
		else outData << "Case #" << i + 1 << ": Game has not completed"  << endl;
		done:;
		}
	
	inData.close();
	outData.close();
}





