#include<cstdio>

char s[4][5];

const char * solve() {
	for(int i = 0; i < 4; ++i) {
		int cx = 0, co = 0, ct = 0;
		for(int j = 0; j < 4; ++j) {
			if(s[i][j] == 'X') ++cx;
			if(s[i][j] == 'O') ++co;
			if(s[i][j] == 'T') ++ct;
		}
		if(cx + ct == 4) return "X won";
		if(co + ct == 4) return "O won";
	}
	for(int j = 0; j < 4; ++j) {
		int cx = 0, co = 0, ct = 0;
		for(int i = 0; i < 4; ++i) {
			if(s[i][j] == 'X') ++cx;
			if(s[i][j] == 'O') ++co;
			if(s[i][j] == 'T') ++ct;
		}
		if(cx + ct == 4) return "X won";
		if(co + ct == 4) return "O won";
	}
	int cx = 0, co = 0, ct = 0;
	for(int i = 0; i < 4; ++i) {
		if(s[i][i] == 'X') ++cx;
		if(s[i][i] == 'O') ++co;
		if(s[i][i] == 'T') ++ct;
	}
	if(cx + ct == 4) return "X won";
	if(co + ct == 4) return "O won";
	cx = co = ct = 0;
	for(int i = 0; i < 4; ++i) {
		if(s[i][3-i] == 'X') ++cx;
		if(s[i][3-i] == 'O') ++co;
		if(s[i][3-i] == 'T') ++ct;
	}
	if(cx + ct == 4) return "X won";
	if(co + ct == 4) return "O won";
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(s[i][j] == '.') return "Game has not completed";
	return "Draw";
}

int main() {
	int tc; scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t) {
		for(int i = 0; i < 4; ++i) scanf("%s", s[i]);
		printf("Case #%d: %s\n", t, solve());
	}
	return 0;
}
