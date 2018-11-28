#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int rule[8][2] = {{0, 1}, {0, -1}, {1, 0}, { -1, 0}, {1, 1}, {1, -1}, { -1, 1}, { -1, -1}};

char s[500][600], t[500][600];
int n, m;

void falldown(char s[500][600])
{
	for (int j = 0; j < n; j++) {
		int i = 0;
		for (int k = 0; k < n; k++)
			if (s[k][j] != '.') {
				swap(s[i][j], s[k][j]);
				i++;
			}
	}
}

bool check(char s[500][600], char c)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < 8; k++) {
				int x = i, y = j;
				for (int l = 0; l <= m; l++) {
					if (l == m) {
						return 1;
					}
					if (x >= 0 && x<n && y >= 0 && y < n && s[x][y] == c) {
						x += rule[k][0];
						y += rule[k][1];
					} else
						break;
				}
			}
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt, phuck = 0;
	scanf("%d", &tt);
	while (tt--) {
		printf("Case #%d: ", ++phuck);
		memset(t, 0, sizeof(t));
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				t[n-j-1][i] = s[i][j];
		falldown(t);
		bool R = check(t, 'R');
		bool B = check(t, 'B');
		if (R && B)
			puts("Both");
		else if (R)
			puts("Red");
		else if (B)
			puts("Blue");
		else
			puts("Neither");
	}
}
