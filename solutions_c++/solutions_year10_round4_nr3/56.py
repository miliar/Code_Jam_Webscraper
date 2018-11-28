#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

bool has[128][128];
bool temp[128][128];

bool go()
{
	memcpy(temp, has, sizeof(has));
	memset(has, false, sizeof(has));
	bool flag = false;
	for (int i = 0; i <= 100; ++i) {
		for (int j = 0; j <= 100; ++j) {
			if (temp[i][j]) {
				if (temp[i - 1][j] || temp[i][j - 1]) {
					flag = true;
					has[i][j] = true;
				}
			}
			else {
				if (temp[i - 1][j] && temp[i][j - 1]) {
					flag = true;
					has[i][j] = true;
				}
			}
		}
	}
	return flag;
}

int run()
{
	memset(has, false, sizeof(has));
	int r;
	scanf("%d", &r);
	for (int i = 0; i < r; ++i) {
		int x1, x2, y1, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; ++x) {
			for (int y = y1; y <= y2; ++y) {
				has[x][y] = true;
			}
		}
	}
	int t = 1;
	while (go()) {
		++t;
	}
	return t;
}

int main()
{
	freopen("C1.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}