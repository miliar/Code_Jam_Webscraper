#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;
	char tmp;
	int mask[10] = {0xf, 0xf0, 0xf00, 0xf000, 0x1111, 0x2222, 0x4444, 0x8888, 0x1248, 0x8421};
	for (int n = 1 ; n <= N ; n ++)
	{
		bool hasEmpty = 0, xWin = 0, oWin = 0;
		int xSum = 0, oSum = 0;
		for (int i = 0 ; i < 4 ; i ++)
			for (int j = 0 ; j < 4 ; j ++)
			{
				cin >> tmp;
				if (tmp == '.')
					hasEmpty = 1;
				else if (tmp == 'X')
					xSum += (1 << (4*i+j));
				else if (tmp == 'O')
					oSum += (1 << (4*i+j));
				else
				{
					xSum += (1 << (4*i+j));
					oSum += (1 << (4*i+j));
				}
			}
		
		cout << "Case #" << n << ": ";
		for (int k = 0 ; k < 10 ; k ++)
		{
			if ((xSum & mask[k]) == mask[k])
				xWin = 1;
			if ((oSum & mask[k]) == mask[k])
				oWin = 1;
		}
		if (xWin)
			cout << "X won" << endl;
		else if (oWin)
			cout << "O won" << endl;
		else if (hasEmpty)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
	return 0;
}
