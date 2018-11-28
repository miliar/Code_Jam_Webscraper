#include<cstdio>
#include<cstdlib>

char s[5][5];

bool check(char X)
{
	for(int i=0; i<4; i++) {
		int sum = 0;
		for(int j=0; j<4; j++)
			if (s[i][j] == 'T' || s[i][j] == X) sum++;
		if (sum == 4) return true;
	}
	for(int i=0; i<4; i++) {
		int sum = 0;
		for(int j=0; j<4; j++)
			if (s[j][i] == 'T' || s[j][i] == X) sum++;
		if (sum == 4) return true;
	}
	for(int i=0; i<1; i++) {
		int sum = 0;
		for(int j=0; j<4; j++)
			if (s[j][j] == 'T' || s[j][j] == X) sum++;
		if (sum == 4) return true;
	}
	for(int i=0; i<1; i++) {
		int sum = 0;
		for(int j=0; j<4; j++)
			if (s[j][3-j] == 'T' || s[j][3-j] == X) sum++;
		if (sum == 4) return true;
	}
	return false;
}


bool check_draw()
{
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++) if (s[i][j] == '.') return false;
	return true;
}


int main()
{
	freopen("A-large.in", "r",stdin);
	freopen("A.out", "w",stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		for(int i=0; i<4; i++) scanf("%s", s[i]);
		if (check('X')) {
			printf("Case #%d: X won\n", t);
		}
		else if (check('O')) {
			printf("Case #%d: O won\n", t);
		}
		else if (check_draw()) {
			printf("Case #%d: Draw\n", t);
		}
		else {
			printf("Case #%d: Game has not completed\n", t);
		}
	}
	return 0;
}
