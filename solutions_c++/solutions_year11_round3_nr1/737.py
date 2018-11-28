#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>

typedef std::pair<int, int> pos_t;

char consistentChar(char c, char top, char left, bool* ok)
{
	*ok = true;	
	if (top >= '1' && top <= '4') {
		if (top == left) {
			*ok = false;
			return '@';
		}
	}
	if (c == '.') {
		if (top == '1' || top == '2' || left == '1' || left == '3') {
			*ok = false;
			return '@';
		}
		return '.';
	}

	if (top == '1')
		return '3';
	if (top == '2')
		return '4';
	if (left == '1')
		return '2';
	if (left == '3')
		return '4';
	return '1';
}

bool validChar(char c)
{
	return c == '.' || c == '#';
}

char pretty(char c)
{
	switch (c) {
		case '1':
		case '4':
			return '/';
		case '2':
		case '3':
			return '\\';
		default:
			return c;
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	
	for (int k = 0; k < t; ++k) {
		int r, c;
		scanf("%d %d", &r, &c);
		
		char* grid = new char[(r + 2) * (c + 2)];
		memset(grid, '.', (r + 2) * (c + 2));
		for (int i = 1; i <= r; ++i) {
			for (int j = 1; j <= c; ++j) {
				do
				{
					scanf("%c", &grid[i * (c + 2) + j]);
				} while (!validChar(grid[i * (c + 2) + j]));
			}
		}
		
		bool ok = true;
		for (int i = 0; i < r + 2; ++i) {
			for (int j = 0; j < c + 2; ++j) {
				char ch = grid[i * (c + 2) + j];
				char top = i > 0 ? grid[(i - 1) * (c + 2) + j] : '.';
				char left = j > 0 ? grid[i * (c + 2) + j - 1] : '.';

				ch = consistentChar(ch, top, left, &ok);
				if (!ok)
					break;
				
				grid[i * (c + 2) + j] = ch;
			}
			
			if (!ok)
				break;
		}
		
		printf("Case #%d:\n", k + 1);
		
		if (!ok) {
			printf("Impossible\n");
		} else {
			for (int i = 1; i <= r; ++i) {
				for (int j = 1; j <= c; ++j)
					printf("%c", pretty(grid[i * (c + 2) + j]));
				printf("\n");
			}
		}
		
		delete [] grid;
	}

	return 0;
}

