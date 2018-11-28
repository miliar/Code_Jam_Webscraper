#include <iostream>
#include <cstdio>

using namespace std;

int t;
char field[4][4];

bool isFull() {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (field[i][j] == '.') return false;
	return true;
}

bool win(const int &fx, const int &fy, const int &sx, const int &sy, const char &c) {
	char check;
	for (int i = 4; i > 0; --i)
		if ((check = field[(fx * i + sx * (4 - i)) / 4][(fy * i + sy * (4 - i)) / 4]) != c 
			&& check != 'T')
			return false;
	return true;
}

int proc(const int &id) {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			scanf(" %c", &field[i][j]);
	printf("Case #%d: ", id);
	if (win(0, 0, 0, 4, 'X') || win(1, 0, 1, 4, 'X') 
		|| win(2, 0, 2, 4, 'X') || win(3, 0, 3, 4, 'X')
		|| win(0, 0, 4, 0, 'X') || win(0, 1, 4, 1, 'X')
		|| win(0, 2, 4, 2, 'X') || win(0, 3, 4, 3, 'X')
		|| win(0, 0, 4, 4, 'X') || win(0, 3, 4, 0, 'X'))
		printf("X won\n");
	else if (win(0, 0, 0, 4, 'O') || win(1, 0, 1, 4, 'O') 
		|| win(2, 0, 2, 4, 'O') || win(3, 0, 3, 4, 'O')
		|| win(0, 0, 4, 0, 'O') || win(0, 1, 4, 1, 'O')
		|| win(0, 2, 4, 2, 'O') || win(0, 3, 4, 3, 'O')
		|| win(0, 0, 4, 4, 'O') || win(0, 3, 4, 0, 'O'))
		printf("O won\n");
	else if (!isFull())	
		printf("Game has not completed\n");
	else
		printf("Draw\n");
	return 0;
}

int main() {
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		proc(i + 1);
	return 0;
}
