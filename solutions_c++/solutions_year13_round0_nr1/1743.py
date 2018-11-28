#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool tmp;
int ca, ans;
char s[5][5];

int main()
{
	freopen("a.out", "w", stdout);
	scanf("%d", &ca);
	for (int t = 1; t <= ca; t++) {
		ans = 0;
		for (int i = 0; i < 4; i++) {
			scanf("%s", s[i]);
			for (int j = 0; j < 4; j++) if (s[i][j] == '.') ans = 2;
		}
		for (int i = 0; i < 4; i++) {
			tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[i][j] == '.') {tmp = false;}
				if (s[i][j] == 'O') {tmp = false;}
			}
			if (tmp) {
				ans = 1; break;
			} else tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[i][j] == '.') {tmp = false;}
				if (s[i][j] == 'X') {tmp = false;}
			}
			if (tmp) {
				ans = -1; break;
			} else tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[j][i] == '.') {tmp = false;}
				if (s[j][i] == 'O') {tmp = false;}
			}
			if (tmp) {
				ans = 1; break;
			} else tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[j][i] == '.') {tmp = false;}
				if (s[j][i] == 'X') {tmp = false;}
			}
			if (tmp) {
				ans = -1; break;
			} else tmp = true;
		}
		tmp = true;
		for (int j = 0; j < 4; j++) {
			if (s[j][j] == '.') {tmp = false;}
			if (s[j][j] == 'O') {tmp = false;}
		}
		if (tmp) ans = 1; else {
			tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[j][j] == '.') {tmp = false;}
				if (s[j][j] == 'X') {tmp = false;}
			}
			if (tmp) ans = -1;
		}
		tmp = true;
		for (int j = 0; j < 4; j++) {
			if (s[j][3-j] == '.') {tmp = false;}
			if (s[j][3-j] == 'O') {tmp = false;}
		}
		if (tmp) ans = 1; else {
			tmp = true;
			for (int j = 0; j < 4; j++) {
				if (s[j][3-j] == '.') {tmp = false;}
				if (s[j][3-j] == 'X') {tmp = false;}
			}
			if (tmp) ans = -1;
		}
		if (ans == -1) printf("Case #%d: O won\n", t);
		if (ans == 1) printf("Case #%d: X won\n", t);
		if (ans == 2) printf("Case #%d: Game has not completed\n", t);
		if (ans == 0) printf("Case #%d: Draw\n", t);
	}
	return 0;
}

