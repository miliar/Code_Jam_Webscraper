// P_A.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

void test(int n)
{
	int A[4][4];
	char c;
	bool empty = false;

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin >> c;
			switch(c)
			{
			case 'X':
				A[i][j] = 100;
				break;
			case 'O':
				A[i][j] = 500;
				break;
			case '.':
				A[i][j] = 10000;
				empty = true;
				break;
			case 'T':
				A[i][j] = 0;
				break;
			}
		}
	}

	for (int i=0;i<4;i++)
	{
		int s = A[i][0] + A[i][1] + A[i][2] + A[i][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	for (int i=0;i<4;i++)
	{
		int s = A[0][i] + A[1][i] + A[2][i] + A[3][i];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	{
		int s = A[0][0] + A[1][1] + A[2][2] + A[3][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	{
		int s = A[3][0] + A[2][1] + A[1][2] + A[0][3];
		if (s == 400 || s == 300)
			goto X_WIN;
		if (s == 1500 || s == 2000)
			goto Y_WIN;
	}

	if (empty)
		goto NOT_COMPLETE;

	goto DRAW;

	return;
X_WIN:
	printf("Case #%d: X won\n", n+1);
	return;
Y_WIN:
	printf("Case #%d: O won\n", n+1);
	return;
DRAW:
	printf("Case #%d: Draw\n", n+1);
	return;
NOT_COMPLETE:
	printf("Case #%d: Game has not completed\n", n+1);
	return;


}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	for(int i=0;i<t;i++)
	{
		test(i);
	}

	return 0;
}

