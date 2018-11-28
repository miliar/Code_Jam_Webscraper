#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const int size = 1000 * 100;

int ans[size];

int main() {

	freopen("problem_a.in", "r", stdin);
	freopen("problem_a.out", "w", stdout);
	
	int tc, d, len, n;
	vector <pair <int, int> > h;
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		cin >> n;
		h.clear();
		for (int i = 0; i < n; i++)
		{
			cin >> d >> len;
			h.pb(mp(d, len));
		}
		cin >> d;
		h.pb(mp(d, inf));
		sort(h.begin(), h.end());
		ans[0] = h[0].fs;
		for (int i = 1; i < int(h.size()); i++)
			ans[i] = -1;
		for (int i = 0; i < n; i++)
		{
			if (ans[i] == -1)
				continue;
			for (int j = i + 1; j <= n; j++)
				if (h[j].fs - h[i].fs <= ans[i])
					ans[j] = max(ans[j], min(h[j].sc, h[j].fs - h[i].fs));
		}
		cout << "Case #" << t + 1 << ": " << (ans[n] >= 0 ? "YES" : "NO") << endl;
	}

	return 0;
}