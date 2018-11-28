#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char a[5][5];

void readdata()
{
	for (int i = 0; i < 4; ++i)
		gets(a[i]);
	scanf("\n");
}

string solve() {
	int x = 0, o = 0, t = 0;
	for (int i = 0; i < 4; ++i)
		if (a[i][i] == 'X') x++;
		else if (a[i][i] == 'O') o++;
		else if (a[i][i] == 'T') t++;

	if (x+t == 4) return "X won";	
	else if (o+t == 4) return "O won";

	x = o = t = 0;
	for (int i = 0; i < 4; ++i)
		if (a[4-i-1][i] == 'X') x++;
		else if (a[4-i-1][i] == 'O') o++;
		else if (a[4-i-1][i] == 'T') t++;

	if (x+t == 4) return "X won";	
	else if (o+t == 4) return "O won";

	for (int i = 0; i < 4; ++i) {
		x = o = t = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[i][j] == 'X') x++;
			else if (a[i][j] == 'O') o++;
			else if (a[i][j] == 'T') t++;
		}
		if (x+t == 4) return "X won";	
		else if (o+t == 4) return "O won";
	}

	for (int i = 0; i < 4; ++i) {
		x = o = t = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[j][i] == 'X') x++;
			else if (a[j][i] == 'O') o++;
			else if (a[j][i] == 'T') t++;
		}
		if (x+t == 4) return "X won";	
		else if (o+t == 4) return "O won";
	}

	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (a[i][j] == '.') return "Game has not completed";

	return "Draw";
}

int main()
{
	freopen("input", "r", stdin);
//	freopen("output", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		readdata();
		printf("Case #%d: %s\n", t, solve().data());
	}


	return 0;
}
