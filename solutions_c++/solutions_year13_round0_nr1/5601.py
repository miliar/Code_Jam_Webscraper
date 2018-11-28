#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

string s[4];
bool first_flag, second_flag;

inline void invoke(char c1, char c2, char c3, char c4)
{
	char base = (c1 == 'T' ? c2 : c1);
	if (base == '.')
		return;
	if ((c1 == base || c1 == 'T') && (c2 == base || c2 == 'T') && (c3 == base || c3 == 'T') && (c4 == base || c4 == 'T'))
	{
		if (base == 'X')
			first_flag = true;
		else second_flag = true;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		printf("Case #%d: ", test);
		for (int i = 0; i <= 3; i++)
			cin >> s[i];
		first_flag = second_flag = false;
		for (int x = 0; x <= 3; x++)
			invoke(s[x][0], s[x][1], s[x][2], s[x][3]);
		for (int y = 0; y <= 3; y++)
			invoke(s[0][y], s[1][y], s[2][y], s[3][y]);
		invoke(s[0][0], s[1][1], s[2][2], s[3][3]);
		invoke(s[0][3], s[1][2], s[2][1], s[3][0]);
		assert((!first_flag) || (!second_flag));
		if (first_flag)
			printf("X won\n");
		else if (second_flag)
			printf("O won\n");
		else
		{
			bool dot_found = false;
			for (int i = 0; i <= 3; i++)
				for (int j = 0; j <= 3; j++)
					if (s[i][j] == '.')
						dot_found = true;
			if (dot_found)
				printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
}