#include <iostream>
#include <algorithm>
#include "stdio.h"
using namespace std;

//#define DBGOUT printf
void DBGOUT(...) { } 

int N, K;
char map[100][100];
char map2[100][100];
int state[100][100];


int rotateMap()
{
	int i, j, k,l;

	l = 0;
	for (i = N - 1; i >= 0; i--) {
		k = N-1;
		for (j = N - 1; j>=0; j--) {
			if (map[i][j] != '.')
				map2[k--][l] = map[i][j];
		}
		l++;
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++)
			DBGOUT("%c", map2[i][j]);
		DBGOUT("\n");
	}

	return 0;
}

int getState(char piece)
{
	int ret = 0;
	int i, j;

	memset(state, 0, sizeof(int)*100*100);

	// horizontal
	for (i = 0; i < N; i++) {
		for (j = 0; j < N-1; j++) {
			if (map2[i][j] == piece && map2[i][j+1] == piece)
			{
				state[i][j+1] = state[i][j]+1;
				DBGOUT("state %d %d=%d\n", i, j+1, state[i][j+1]);
				if (state[i][j+1] == K-1)
					return 1;
			}
		}
	}

	memset(state, 0, sizeof(int)*100*100);

	// vertical
	for (i = 0; i < N-1; i++) {
		for (j = 0; j < N; j++) {
			if (map2[i][j] == piece && map2[i+1][j] == piece)
			{
				state[i+1][j] = state[i][j]+1;
				DBGOUT("state %d %d=%d\n", i+1, j, state[i+1][j]);
				if (state[i+1][j] == K-1)
					return 1;
			}
		}
	}

	memset(state, 0, sizeof(int)*100*100);

	// diagonal
	for (i = 0; i < N-1; i++) {
		for (j = 0; j < N-1; j++) {
			if (map2[i][j] == piece && map2[i+1][j+1] == piece)
			{
				state[i+1][j+1] = state[i][j]+1;
				DBGOUT("state %d %d=%d\n", i+1, j+1, state[i+1][j+1]);
				if (state[i+1][j+1] == K-1)
					return 1;
			}
		}
	}

	memset(state, 0, sizeof(int)*100*100);

	// reverse diagonal
	for (i = 0; i < N-1; i++) {
		for (j = 1; j < N; j++) {
			if (map2[i][j] == piece && map2[i+1][j-1] == piece)
			{
				state[i+1][j-1] = state[i][j]+1;
				DBGOUT("state %d %d=%d\n", i+1, j-1, state[i+1][j-1]);
				if (state[i+1][j-1] == K-1)
					return 1;
			}
		}
	}

	return 0;
}


int main()
{
	int case_cnt;
	int ret = 0;

	cin >> case_cnt;

	for (int i = 0; i < case_cnt; i++) 
	{
		cin >> N;
		cin >> K;

		DBGOUT("N=%d\nK=%d\n", N,K);

		memset(map, '.', 100*100);
		memset(map2, 0, 100*100);
		memset(state, 0, sizeof(int)*100*100);


		for (int j = 0; j < N; j++) {
			scanf("%s", map[j]);
		}
/*
	for (int a = 0; a < N; a++) {
		for (int b = 0; b < N; b++)
			DBGOUT("%c", map[a][b]);
		DBGOUT("\n");
	}
*/
		rotateMap();

		ret = getState('R');
		ret |= getState('B') * 2;

		cout << "Case #" << i + 1 << ": " ;
		switch(ret) {
			case 0: cout << "Neither"; break;
			case 1: cout << "Red"; break;
			case 2: cout << "Blue"; break;
			case 3: cout << "Both"; break;
		}
		cout << endl;
	}
}

