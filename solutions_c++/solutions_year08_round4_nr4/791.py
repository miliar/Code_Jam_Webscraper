#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

const int MAXN = 1024;

char str[MAXN];

int better(int a, int b)
{
	if (a < 0) return b;
	if (b < 0) return a;
	return min(a, b);
}

int go(string str)
{
	char last = -1;
	int ret = 0;
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] != last) {
			last = str[i];
			++ret;
		}
	}
	return ret;
}

void run(int t)
{
	int k;
	scanf("%d %s", &k, str);
	int sz = strlen(str);
	int tt = sz / k;
	int dp[26];
	int arr[5] = {0, 1, 2, 3, 4};
	int best = 1000000;
	do {
		string s;
		for (int i = 0; i < tt; ++i) {
			for (int j = 0; j < k; ++j) {
				s += str[i * k + arr[j]];
			}
		}
		best = min(best, go(s));
	}
	while (next_permutation(arr, arr + k));
	printf("Case #%d: %d\n", t, best);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		run(i);
	}
	return 0;
}