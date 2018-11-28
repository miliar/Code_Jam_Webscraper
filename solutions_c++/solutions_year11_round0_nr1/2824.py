// Robots.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cassert>

class Task
{
public:
	int P;
	char R;
};

int FindNext(Task lst[], int N, int n, char r);

bool RobotMove(Task lst[], int N, int n, char r, int &pos, int &next);

int _tmain(int argc, _TCHAR* argv[])
{
	int T, N;
	int nextO;
	int nextB;
	int posO;
	int posB;
	Task lst[100];

	scanf("%d", &T);

	for (int c = 1; c <= T; c++)
	{
		scanf("%d", &N);

		for (int n = 0; n < N; n++)
		{
			char str[10];
			scanf("%s", str);
			char ch = str[0];
			assert((ch == 'O') || (ch == 'B'));
			lst[n].R = str[0];
			scanf("%d", &lst[n].P);
		}

		int t = 0;
		posO = 1;
		posB = 1;

		int n = 0;

		nextO = FindNext(lst, N, n, 'O');		
		nextB = FindNext(lst, N, n, 'B');

		while (n < N)
		{
			bool advance = false;

//			printf("t %d n %d nextO %d nextB %d\n", t, n, nextO, nextB);
			assert((n == nextO) || (n == nextB));

			advance |= RobotMove(lst, N, n, 'O', posO, nextO);
			advance |= RobotMove(lst, N, n, 'B', posB, nextB);

			if (advance)
				n++;
			t++;
		}

		printf("Case #%d: %d\n", c, t);
	}

	

	return 0;
}

bool RobotMove(Task lst[], int N, int n, char r, int &pos, int &next)
{
	if (next == -1)
		return false;

	int goal = lst[next].P;

	if ((pos == goal) && (n == next))
	{
		next = FindNext(lst, N, n+1, r);
		return true;
	}

	if (pos < goal)
		pos++;
	else if (pos > goal)
		pos--;

    return false;
}

int FindNext(Task lst[], int N, int n, char r)
{
	while (n < N)
	{
//		printf("%d %c=%c?\n", n, lst[n].R, r);
		if (lst[n].R == r)
			return n;
		n++;
	}

	return -1;
}