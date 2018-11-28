#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <deque>

using namespace std;

int whowon(int matrix[4][4])
{
	bool fini = true;
	int sum = 0;
	for (int i = 0; i < 4; i += 1)
	{
		sum = 0;
		for (int j = 0; j < 4; j += 1)
		{
			if (matrix[i][j] == 0)
			{
				fini = false;
			}
			sum += matrix[i][j];
		}
		if (sum == 4)
		{
			return 1;
		}if (sum == -4)
		{
			return -1;
		}
	}
		for (int i = 0; i < 4; i += 1)
	{
		sum = 0;
		for (int j = 0; j < 4; j += 1)
		{
			if (matrix[j][i] == 0)
			{
				fini = false;
			}
			sum += matrix[j][i];
		}
		if (sum == 4)
		{
			return 1;
		}if (sum == -4)
		{
			return -1;
		}
	}
	int sum1 = 0;
	int sum2 = 0;
	for (int i = 0; i < 4; i += 1)
	{
		sum1 += matrix[i][i];
		sum2 += matrix[3-i][i];
	}
	if (sum1 == 4 or sum2 == 4)
	{
		return 1;
	}
	if (sum1 == -4 or sum2 == -4)
	{
		return -1;
	}
	if (fini)
	return 0;
	else
	return 2;
}

int main (int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
		int matrix[4][4];
		int ti = -1;
		int tj = -1;
		for (int i = 0; i < 4; i += 1)
		{
			for (int j = 0; j < 4; j += 1)
			{
				char temp;
				cin >> temp;
				if (temp == 'X')
				{
					matrix[i][j] = 1;
				}
				if (temp == 'O')
				{
					matrix[i][j] = -1;
				}
				if (temp == '.')
				{
					matrix[i][j] = 0;
				}
				if (temp == 'T')
				{
					ti = i; tj = j;
					matrix[i][j] = 1;
				}
			}
		}
		int g1 = whowon(matrix);
		if (ti != -1)
		{
			matrix[ti][tj] = -1;
		}
		int g2 = whowon(matrix);
		cout << "Case #" << t+1 << ": " ;
		if (g1 == 1 or g2 == 1)
		{
			cout << "X won" << endl;
		} else if (g1 == -1 or g2 == -1)
		{
			cout << "O won" << endl;
		}else if (g1 == 0 && g2 == 0)
		{
			cout << "Draw" << endl;
		}
		else if (g1 == 2)
		{
			cout << "Game has not completed" << endl;
		}
	}
	return 0;
}
