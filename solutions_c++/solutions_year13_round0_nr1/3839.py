#include <cstdio>

int c[16];

inline bool check(int ch)
{
	int i;
	for (i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; ++j) {
			if (c[(i<<2)+j] != ch && c[(i<<2)+j] != 'T')
				break;
		}
		if (j == 4)
			return true;
		for (j = 0; j < 4; ++j) {
			if (c[(j<<2)+i] != ch && c[(j<<2)+i] != 'T')
				break;
		}
		if (j == 4)
			return true;
	}
	for (i = 0; i < 4; ++i) {
		if (c[(i<<2)+i] != ch && c[(i<<2)+i] != 'T')
			break;
	}
	if (i == 4)
		return true;
	for (i = 0; i < 4; ++i) {
		if (c[(i<<2)+3-i] != ch && c[(i<<2)+3-i] != 'T')
			break;
	}
	return i == 4;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int t = 1; t <= cases; ++t) {
		printf("Case #%d: ", t);
		bool filled = true;
		for (int i = 0; i < 16; ++i) {
			while ((c[i] = getchar()) == ' ' || c[i] == '\n')
				;
			if (c[i] == '.')
				filled = false;
			
		}
		int res = (check('X')<<1)+check('O');
		switch(res) {
			case 0:
				if (filled)
					printf("Draw\n");
				else
					printf("Game has not completed\n");
				break;
			case 1:
				printf("O won\n");
				break;
			case 2:
				printf("X won\n");
				break;
			case 3:
				printf("Draw\n");
		}
		getchar();
	}
	return 0;
}
