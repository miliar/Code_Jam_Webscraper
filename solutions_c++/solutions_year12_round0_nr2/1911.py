#include<cstdio>
#include<algorithm>
#define NMAX 105
using namespace std;

int solve()
{
	int T[NMAX], n, s, p, ans = 0;

	scanf("%d%d%d", &n, &s, &p);
	for(int i = 0; i < n; ++i)
		scanf("%d", T + i);

	sort(T, T + n);

	for(int i = n - 1; i >= 0; --i)
		if((T[i] + 2) / 3 >= p)
			++ans;
		else if(T[i] && T[i] % 3 != 1 && s && (T[i] + 2) / 3 == p - 1)
			++ans, --s;
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
		printf("Case #%d: %d\n", t, solve());

	return 0;
}
