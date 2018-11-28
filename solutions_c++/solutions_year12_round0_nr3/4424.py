#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <list>
#include <map>
using namespace std;

int num[1000][8] = {0};
int digit[10];
int a, b;

void solve(int t)
{
	int tmp = t;
	memset(digit, 0, sizeof(digit));
	int cnt = 0;
	while (tmp > 0) {
		digit[cnt++] = tmp % 10;
		tmp /= 10;
	}
	reverse(digit, digit + cnt);
	num[t][0] = 0;
	for (int i = 1; i < cnt; ++i) {
		int tmp = 0;
		for (int j = 0; j < cnt; ++j) {
			tmp += digit[(i + j) % cnt] * (int)pow(10.0, cnt - j - 1);
		}
		if (tmp <= 1000 && tmp > t) {
			num[t][++num[t][0]] = tmp;
		}
	}
}

void prepare()
{
	for (int i = 1; i <= 1000; ++i) {
		solve(i);
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	prepare();
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int ans = 0;
		scanf("%d%d", &a, &b);
		for (int j = a; j <= b; ++j) {
			for (int k = 1; k <= num[j][0]; ++k) {
				if (num[j][k] >= a && num[j][k] <= b) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}