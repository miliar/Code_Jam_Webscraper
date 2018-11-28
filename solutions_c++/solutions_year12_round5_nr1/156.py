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

bool compp(pair <int, int> a, pair <int, int> b)
{
	return a.sc * b.fs - b.sc * a.fs > 0;
}

bool comp(pair <pair <int, int>, int > s, pair <pair <int, int>, int> f)
{
	if (!compp(s.fs, f.fs) && !compp(f.fs, s.fs))
		return s.sc < f.sc;
	return compp(s.fs, f.fs);
}

int main() {
	int tc, n;
	int len, p;
	vector <pair <pair <int, int>, int > > h;

	freopen("problem_a.in", "r", stdin);
	freopen("problem_a.out", "w", stdout);
	
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		cin >> n;
		h.clear();
		for (int i = 0; i < n; i++)
		{
			cin >> len;
			h.pb(mp(mp(len, 0), i));
		}
		for (int i = 0; i < n; i++)
		{
			cin >> p;
			h[i].fs.sc = p;
		}
		sort(h.begin(), h.end(), comp);
		cout << "Case #" << t + 1 << ":";
		for (int i = 0; i < n; i++)
			cout << " " << h[i].sc;
		cout << endl;
	}

	return 0;
}