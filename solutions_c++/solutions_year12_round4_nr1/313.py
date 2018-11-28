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
ll L[10500], D[10500];
ll x[10500];
void solve()
{
	int N;
	scanf ("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%lld%lld", &D[i], &L[i]);
	}
	ll d;
	scanf ("%lld", &d);
	memset(x, 0, sizeof(x));
	x[0] = D[0];
	for (int i = 0; i < N; ++i)
	{
		if (D[i] + x[i] >= d) 
		{
			printf("YES\n");
			return;
		}
		for (int j = i + 1; j < N; ++j)
		{
			if (D[j] > D[i] + x[i]) break;
			x[j] = max(x[j], min(L[j], D[j] - D[i]));
		}
	}
	printf("NO\n");
}
int main()
{
	freopen("Atest.txt", "r", stdin);
	freopen("Aout.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}