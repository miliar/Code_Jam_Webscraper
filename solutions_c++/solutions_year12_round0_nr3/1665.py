#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

bool used[2000100];
int A, B;
int calc(int x)
{
	int t = x;
	int d = 1;
	while (t)
	{
		t /= 10;
		d *= 10;
	}
	d /= 10;
	int cnt = 0;
	while(true)
	{
		if (A <= x && x <= B)
		{
			if (used[x]) break;
			++cnt;
			used[x] = true;
		}
		t = x % 10;
		x /= 10;
		x += t*d;
	}
	return (cnt*(cnt-1))/2;
}
void solve(int n)
{
	ll ans = 0;
	memset(used, false, sizeof(used));
	scanf ("%d%d", &A, &B);
	for (int i = A; i <= B; ++i)
	{
		if (used[i]) continue;
		ans += calc(i);
	}
	printf("Case #%d: %lld\n", n, ans);
}
int main()
{
#ifdef _DEBUG
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		solve(i + 1);
	}
	return 0;
}