#include<cstdio>
#include<set>
using namespace std;

int solve()
{
	int a, b, ans = 0;
	scanf("%d%d", &a, &b);

	int p = 1, c = 1;;
	while(a / p / 10)
		p *= 10, ++c;

	for(int n = a; n <= b; ++n)
	{
		set<int> Set;
		int m = n;
		for(int i = 1; i < c; ++i)
		{
			m = (m / 10) + (m % 10 * p);
			if(m > n && m <= b && !Set.count(m))
				Set.insert(m);
		}
		ans += Set.size();
	}
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
		printf("Case #%d: %d\n", t, solve());

	return 0;
}
