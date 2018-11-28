#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	vector<string> v;

	for (int u = 1; u <= t; u++) {
		string s;
		for (int i = 0; i < 4; i++) {
			cin >> s;
			v.push_back(s);
		}
		int c = 0;
		int p = 0;
		int w = 0;
		int xx[4];
		int xo[4];
		int yx[4];
		int yo[4];
		for (int i = 0; i < 4; i++) {
			xx[i] = 0;
			xo[i] = 0;
			yx[i] = 0;
			yo[i] = 0;
		}
		
		int d1x = 0;
		int d1o = 0;
		int d2x = 0;
		int d2o = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (v[i][j] == 'X' || v[i][j] == 'T') {
					xx[i]++;			
				}
				if (v[i][j] == 'O' || v[i][j] == 'T') {
					xo[i]++;
				}
				if (v[i][j] == '.') {
					p++;
				}
			}
			if (xx[i] == 4) {
				printf("Case #%d: X won\n", u);
				w = 1;
				break;
			}
			if (xo[i] == 4) {
				printf("Case #%d: O won\n", u);
				w = 1;
				break;
			}
		}

		if (w == 0) {
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (v[j][i] == 'X' || v[j][i] == 'T') {
						yx[i]++;
					} 
					if (v[j][i] == 'O' || v[j][i] == 'T') {
						yo[i]++;
					}
				}
		
				if (yx[i] == 4) {
					printf("Case #%d: X won\n", u);
					w = 1;
					break;
				}
				if (yo[i] == 4) {
					printf("Case #%d: O won\n", u);
					w = 1;
					break;
				}
			}
		}

		if (w == 0) {
			for (int i = 0; i < 4; i++) {
				if (v[i][i] == 'X' || v[i][i] == 'T') {
					d1x++;
				}
				if (v[i][i] == 'O' || v[i][i] == 'T') {
					d1o++;
				}
			}
			if (d1x == 4) {
				printf("Case #%d: X won\n", u);
				w = 1;
			}
			if (d1o == 4) {
				printf("Case #%d: O won\n", u);
				w = 1;
			}
		}
	
		if (w == 0) {
			for (int i = 0; i < 4; i++) {
				if (v[i][3 - i] == 'X' || v[i][3 - i] == 'T') {
					d2x++;
				}
				if (v[i][3 - i] == 'O' || v[i][3 - i] == 'T') {
					d2o++;
				}
			}
			if (d2x == 4) {
				printf("Case #%d: X won\n", u);
				w = 1;
			}
			if (d2o == 4) {
				printf("Case #%d: O won\n", u);
				w = 1;
			}
		}
	
		if (w == 0) {
			if (p == 0) {
				printf("Case #%d: Draw\n", u);
				w = 1;
			} else {
				printf("Case #%d: Game has not completed\n", u);
				w = 1;
			}
		}
		v.clear();
		printf("\n");
	}

	return 0;
}
	
