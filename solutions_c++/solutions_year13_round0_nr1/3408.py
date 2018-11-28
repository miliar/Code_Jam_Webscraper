#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

bool is_win(int res)
{
	int masks[] = {0xF000, 0x0F00, 0x00F0, 0x000F, 0x8888, 0x4444, 0x2222, 0x1111, 0x8421, 0x1248};
	for (int i = 0; i < sizeof(masks) / sizeof(masks[0]); i++)
		if ((res & masks[i]) == masks[i])
			return true;
	return false;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	char s[MAX_PATH];
	cin.getline(s, sizeof(s));

	int nCount, numCase = 1;
	nCount = atoi(s);

	while (numCase <= nCount)
	{
		char s[5][16];
		cin.getline(s[0], 16);
		cin.getline(s[1], 16);
		cin.getline(s[2], 16);
		cin.getline(s[3], 16);
		cin.getline(s[4], 16);

		int pX = 0, pO = 0;
		bool bEmpty = false;
		for (int j = 0; j < 4; j++)
		{
			for (int i = 0; i < 4; i++)
			{
				char c = s[j][i];
				pX <<= 1;
				pO <<= 1;
				if (c == 'X')
					pX |= 1;
				else if (c == 'O')
					pO |= 1;
				else if (c == 'T')
				{
					pX |= 1;
					pO |= 1;
				}
				else
					bEmpty = true;
			}
		}

		cout << "Case #" << numCase << ": ";

		if (is_win(pX))
			cout << "X won";
		else if (is_win(pO))
			cout << "O won";
		else if (!bEmpty)
			cout << "Draw";
		else
			cout << "Game has not completed";

		cout << "\n";

		numCase++;
	}
	return 0;
}
