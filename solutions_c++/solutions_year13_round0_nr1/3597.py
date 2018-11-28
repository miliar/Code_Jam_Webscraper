#include <cstdio>
#include <cstring>

bool Xd1, Xd2, Od1, Od2, dot, Xr, Or, Xc[4], Oc[4];
int win;
int cases, casei;
char st[10];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		Xd1 = true; Xd2 = true;
		Od1 = true; Od2 = true;
		dot = false;
		memset(Xc, true, sizeof Xc);
		memset(Oc, true, sizeof Oc);
		win = 0;
		for (int i = 0; i < 4; ++i) {
			scanf(" %s", &st);
			Xr = true;
			Or = true;
			for (int j = 0; j < 4; ++j) {
				if (st[j] == 'X') {
					Or = false;
					Oc[j] = false;
					if (i == j) Od1 = false;
					if (i + j == 3) Od2 = false;
				}
				else if (st[j] == 'O') {
					Xr = false;
					Xc[j] = false;
					if (i == j) Xd1 = false;
					if (i + j == 3) Xd2 = false;
				}
				else if (st[j] == '.') {
					Xr = false; Xc[j] = false;
					Or = false; Oc[j] = false;
					dot = true;
					if (i == j) {
						Od1 = false;
						Xd1 = false;
					}
					if (i + j == 3) {
						Od2 = false;
						Xd2 = false;
					}
				}
			}
			if (Xr) win = 1;
			if (Or) win = 2;
		}
		if (Xd1 || Xd2) win = 1;
		if (Od1 || Od2) win = 2;
		if (win == 0) {
			for (int i = 0; i < 4; ++i) if (Xc[i]) win = 1;
			for (int i = 0; i < 4; ++i) if (Oc[i]) win = 2;
		}
		switch (win) {
			case 1: 
				printf("Case #%d: X won\n", casei);
				break;
			case 2: 
				printf("Case #%d: O won\n", casei);
				break;
			default: 
				if (dot) printf("Case #%d: Game has not completed\n", casei);
				else printf("Case #%d: Draw\n", casei);
				break;
		}
	}

	return 0;
}
