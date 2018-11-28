#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

char str[1024];

int main()
{
	map<string, int> dict;
	int T;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		dict.clear();
		int n; scanf("%d%*c", &n);
		FOR(i, 0, n) {
			gets(str);
			dict[str] = i;
		}
		int s[1024], m;
		scanf("%d%*c", &m);
		FOR(i, 0, m) {
			gets(str);
			s[i] = dict[str];
		}
		int dp[128] = { 0 }, tmp[128];
		FOR(i, 0, n)
			if(i != s[0]) dp[i] = 0;
			else dp[i] = 1<<20;
		FOR(i, 1, m) {
			FOR(j, 0, n) tmp[j] = 1<<20;
			FOR(j, 0, n) if(j != s[i]) tmp[j] <?= dp[j];
			FOR(j, 0, n) if(j != s[i]) tmp[j] <?= dp[s[i]]+1;
			memcpy(dp, tmp, sizeof(dp));
		}
		int res = 1<<20;
		FOR(i, 0, n) res <?= dp[i];
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
