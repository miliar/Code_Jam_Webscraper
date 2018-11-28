#include <cstdio>
#include <iostream>

using namespace std;

typedef long long ll;

const int inf = 1 << 30;
const int MAX_N = 1000 + 5;
const int MAX_M = 1 << 22 + 1;
int A[MAX_N];
int D[MAX_M], D1[MAX_M];

int n;

void pr_no()
{
	printf("NO\n");
}

void solve(int NUM)
{
	printf("Case #%d: ", NUM);
	int xsum = 0;
	for (int i = 0; i < n; ++i)
		xsum ^= A[i];
		
	if (xsum)
		pr_no();
	else
	{
		ll sum = 0;
		ll _min = inf;
		for (int i = 0; i < n; ++i)
		{
			sum += 1LL * A[i];
			_min = min(_min, 1LL * A[i]);
		}
		ll res = sum - _min;
		cout << res << "\n";
	}
	
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	cin >> T;
	
	for (int i = 0; i < T; ++i)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; ++j)
			scanf("%d", &A[j]);
		
		solve(i + 1);
	}
	return 0;
}
