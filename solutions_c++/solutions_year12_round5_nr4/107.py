#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int maxL = 10000 + 10;
int map[36][36];
int din[36], dou[36], k;
char s[maxL];

int c(int x)
{
	if (x == 'o'-'a') return 26+0;
	if (x == 'i'-'a') return 26+1;
	if (x == 'e'-'a') return 26+3;
	if (x == 'a'-'a') return 26+4;
	if (x == 's'-'a') return 26+5;
	if (x == 't'-'a') return 26+7;
	if (x == 'b'-'a') return 26+8;
	if (x == 'g'-'a') return 26+9;
	return x;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int TextN, TT = 0;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d", &k);
		scanf("%s", s);
		memset(din, 0, sizeof(din));
		memset(dou, 0, sizeof(dou));
		memset(map, 0, sizeof(map));
		int x, y;
		for (int i = 0; i < strlen(s)-1; i++) {
			x = s[i] - 'a';
			y = s[i+1] - 'a';
			map[x][y] = 1;
			map[c(x)][y] = 1;
			map[x][c(y)] = 1;
			map[c(x)][c(y)] = 1;
		}
		int Ans = 0;
		for (int i = 0; i < 36; i++)
			for (int j = 0; j < 36; j++) {
					if (map[i][j]) ++Ans;
					din[i] += map[j][i];
					dou[i] += map[i][j];
				}
		int tmp = 0;
		for (int i = 0; i < 36; i++)
			if (din[i] > dou[i]) tmp += din[i] - dou[i];
		if (tmp == 0) tmp = 1;
		printf("Case #%d: %d\n", ++TT, Ans + tmp);
	}
	return 0;
}