#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define NM 10

char b[NM][NM];

int checkwon(char c)
{
	int answer = 0, won = 0;	

	// check main diagonal
	won = 1;
	for (int i = 0; i < 4; ++i) 
		if (b[i][i] != c && b[i][i] != 'T') won = 0;
	answer = answer | won;

	// check secondary diagonal
	won = 1;
	for (int i = 0; i < 4; ++i)
		if (b[i][4-i-1] != c && b[i][4-i-1] != 'T') won = 0;
	answer = answer | won;

	// check rows
	for (int i = 0; i < 4; ++i)
	{
		won = 1;
		for (int j = 0; j < 4; ++j)
			if (b[i][j] != c && b[i][j] != 'T') won = 0;	
		answer = answer | won;
	}		

	// check columns
	for (int j = 0; j < 4; ++j)
	{
		won = 1;
		for (int i = 0; i < 4; ++i)
			if (b[i][j] != c && b[i][j] != 'T') won = 0;
		answer = answer | won;	
	}

	return answer;
}

int completed()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (b[i][j] == '.') return 0;

	return 1;	
}

int main()
{
	freopen ("tests.in", "r", stdin);
	freopen ("tests.out", "w", stdout);

	int T;
	scanf ("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		for (int i = 0; i < 4; ++i)
			scanf ("%s", b[i]);

		if (checkwon('X')) printf ("Case #%d: X won\n", t);
		else if (checkwon('O')) printf ("Case #%d: O won\n", t);		
		else if (completed()) printf ("Case #%d: Draw\n", t);
		else printf ("Case #%d: Game has not completed\n", t);	
	}

	return 0;
}
