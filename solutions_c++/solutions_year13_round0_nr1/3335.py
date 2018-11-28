#include <cstdio>
using namespace std;

const int Maxn = 4;

int t;
char B[Maxn][Maxn];

bool Owns(char a, char b) { return a == b || a == 'T'; }

bool Wins(char x)
{
	return Owns(B[0][0], x) && Owns(B[0][1], x) && Owns(B[0][2], x) && Owns(B[0][3], x) ||
		   Owns(B[1][0], x) && Owns(B[1][1], x) && Owns(B[1][2], x) && Owns(B[1][3], x) ||
		   Owns(B[2][0], x) && Owns(B[2][1], x) && Owns(B[2][2], x) && Owns(B[2][3], x) ||
		   Owns(B[3][0], x) && Owns(B[3][1], x) && Owns(B[3][2], x) && Owns(B[3][3], x) ||

		   Owns(B[0][0], x) && Owns(B[1][0], x) && Owns(B[2][0], x) && Owns(B[3][0], x) ||
		   Owns(B[0][1], x) && Owns(B[1][1], x) && Owns(B[2][1], x) && Owns(B[3][1], x) ||
		   Owns(B[0][2], x) && Owns(B[1][2], x) && Owns(B[2][2], x) && Owns(B[3][2], x) ||
		   Owns(B[0][3], x) && Owns(B[1][3], x) && Owns(B[2][3], x) && Owns(B[3][3], x) ||

		   Owns(B[0][0], x) && Owns(B[1][1], x) && Owns(B[2][2], x) && Owns(B[3][3], x) ||
		   Owns(B[0][3], x) && Owns(B[1][2], x) && Owns(B[2][1], x) && Owns(B[3][0], x);
}

bool Finish()
{
	for (int i = 0; i < Maxn; i++)
		for (int j = 0; j < Maxn; j++)
			if (B[i][j] == '.') return false;
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		for (int i = 0; i < Maxn; i++)
			for (int j = 0; j < Maxn; j++)
				scanf(" %c", &B[i][j]);
		printf("Case #%d: ", tc);
		if (Wins('X')) printf("X won\n");
		else if (Wins('O')) printf("O won\n");
		else if (Finish()) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}