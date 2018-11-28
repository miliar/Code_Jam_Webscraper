#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <cstdio>
#include <set>
#include <algorithm>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int LL;
LL ans;
int t, r, k, n, last, next;
vector<LL> g, s;
vector<LL>::iterator it;
int main()
{
	ios_base::sync_with_stdio(false);
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		ans = 0;
		cin >> r >> k >> n;
		g.resize(n);
		for(int i = 0; i < n; ++i)
			cin >> g[i];
		s.resize(2 * n + 1);
		s[0] = 0;
		for(int i = 1; i <= 2 * n; ++i)
			s[i] = s[i - 1] + g[(i - 1) % n];
		last = 1;
		for(int i = 0; i < r; ++i)
		{
			next = upper_bound(s.begin() + last, s.begin() + last + n, s[last - 1] + k) - s.begin();
		//	cout << next << " " << last << endl;
			ans += s[next - 1] - s[last - 1];
			last = (next > n) ? next - n : next;
		}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
