#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const double pi = acos(-1.0);
const int size = 10;

char field[size][size];
int ver[size], hor[size];
bool good[size][size];

bool haswon(char c) {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			good[i][j] = (field[i][j] == c || field[i][j] == 'T');
	for (int i = 0; i < 4; i++) {
		ver[i] = 0;
		hor[i] = 0;
	}

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			ver[i] += good[i][j];
			hor[j] += good[i][j];

			if (ver[i] == 4 || hor[j] == 4)
				return true;
		}
	if (good[0][0] && good[1][1] && good[2][2] && good[3][3])
		return true;
	if (good[0][3] && good[1][2] && good[2][1] && good[3][0])
		return true;

	return false;
}

int main() {
	int tc;

	freopen("problem_a.in", "r", stdin);
	freopen("problem_a.out", "w", stdout);
	
	scanf("%d", &tc);
	for (int tnum = 0; tnum < tc; tnum++) {
		for (int i = 0; i < 4; i++)
			scanf("%s", field[i]);

		bool flag1 = haswon('X');
		bool flag2 = haswon('O');
		bool flag = false;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				flag = flag || (field[i][j] == '.');

		assert(!flag1 || !flag2);
		printf("Case #%d: ", tnum + 1);
		if (flag1)
			printf("X won\n");
		else
			if (flag2)
				printf("O won\n");
			else
				if (flag)
					printf("Game has not completed\n");
				else
					printf("Draw\n");
	}

	return 0;
}