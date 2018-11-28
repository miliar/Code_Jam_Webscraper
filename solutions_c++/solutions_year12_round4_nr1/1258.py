#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <set>
#include <map>
using namespace std;

#define FILE ""

int n, d[100005], l[100005], dp[10005], D;

void Load()
{
	cin >> n;

	for (int i = 0;i < n;i++) {
	 	cin >> d[i] >> l[i];
	}
	cin >> D;
}

void Solve()
{
	memset (dp, -1, sizeof (dp));
	dp[0] = min (d[0], l[0]);

	for (int i = 0;i < n;i++) {
	 	if (dp[i] == -1) {
	 		continue;
	 	}

	 	int j;
	 	for (j = i + 1;j < n && d[j] - d[i] <= dp[i];j++) {
	 		dp[j] = max (dp[j], min (l[j], d[j] - d[i]));
	 	}
	 	if (j == n) {
	 	 	if (dp[i] >= D - d[i]) {
	 	 	 	cout << "YES\n";
	 	 	 	return;
	 	 	}
	 	}
	}
	cout << "NO\n";
}

int main ()
{
	freopen (FILE"a.in", "r", stdin);
	freopen (FILE"a.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 1;i <= T;i++) {
	printf ("Case #%d: ", i);
   	Load();
   	Solve();
   }

	return 0;
}
