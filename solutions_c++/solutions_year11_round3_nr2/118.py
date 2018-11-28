#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long L, t, N, C;
vector<long long> a;

vector<double> z;

void solve(int test)
{
	z.clear();
	
	int k = 0;
	long long T = 0;
	int i;
	
	for (i = 0; i < N; ++i, ++k)
	{
		if (k == C)
			k = 0;
		if (t < T + a[k] * 2)
		{
			z.push_back(a[k] - (t - T) * 1.0 / 2);
			break;
		} else
		if (t == T + a[k] * 2)
		{
			break;
		} else
			T += a[k] * 2;
//		cerr << "T == " << T << endl;
	}
	
//	cerr << i << endl;
	++i, ++k;
	for (; i < N; ++i, ++k)
	{
		if (k == C)
			k = 0;
		z.push_back(a[k]);
	}
	
	sort(z.begin(), z.end());
	
	long long ans = 0;
//	cerr << z.size() << endl;
	for (int i = (int)z.size() - 1; i >= 0; --i)
	{
//		cerr << z[i] << endl;
		if (L > 0)
			ans += z[i], --L;
		else
			ans += z[i] * 2;
	}
//	cerr << "!!!!!!!!!!!!!!!!1" << endl;
	if (z.size() == 0 && t > T)
		t = 0, ans = T;
	cout << "Case #" << test + 1 << ": " << ans + t << endl;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int T;
	cin >> T;

	for (int col = 0; col < T; ++col)
	{
		a.clear();
		cin >> L >> t >> N >> C;
		a.resize(C);
		for (int i = 0; i < C; ++i)
			cin >> a[i];
		solve(col);
	}
	return 0;
}
