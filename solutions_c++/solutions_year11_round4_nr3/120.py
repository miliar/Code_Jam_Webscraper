#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef long long llong;
typedef llong answer_type;


vector<llong> P;

const int N = 1000500;

void gen_primes()
{
	bool bad;
	for (int x = 2; x < N; x++)
	{
		bad = false;
		for (int i = 0; i < P.size(); i++)
		{
			if (P[i] * P[i] > x)
				break;
			if (x % P[i])
				continue;
			bad = 1;
			break;
		}
		if (!bad)
		{
			P.push_back(x);
			//cerr << x << ' ';
		}
	}
	cerr << "Generated " << P.size() << " primes" << endl;
}

answer_type solve()
{
	llong n;
	cin >> n;
	if (n == 1)
		return 0;
	llong sqn = (llong)sqrt((double)n);
	llong low = 0;
	llong up = 1;
	
	for (int x = 0; ; x++)
	{
		if (P[x] > sqn)
			break;
		llong q = 0, z = P[x];
		low++;
		while (z <= n)
			z *= P[x], q++;
		up += q;
	}
	cerr << low << ' ' << up << ' ';
	return up - low;
}

int main()
{
	gen_primes();
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
