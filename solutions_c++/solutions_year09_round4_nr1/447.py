#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){ return x > 0 ? x : (-x); }
template<class T> T sqr(T x){ return x * x; }

bool check(vi v)
{
	sort(all(v));
	for (int i = 0; i < sz(v); i++)
		if (v[i] > i + 1) return false;
	return true;
}

void solve(int testnum)
{
	printf("Case #%d: ", testnum + 1);
	int n;
	cin >> n;
	vi v;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		int x = 0;
		for (int j = 0; j < sz(s); j++)
			if (s[j] == '1') x = max(x, j + 1);
		v.pb(x);
	}
	int res = 0;
	while (sz(v))
	{
		int cur = 1000000;
		for (int i = 0; i < sz(v); i++)
		{
			if (v[i] > 1) continue;
			vi w;
			for (int j = 0; j < sz(v); j++)
				if (i != j) w.pb(v[j] - 1);
			if (check(w))
				cur = min(cur, i);
		}
		res += cur;
		{
			vi w;
			for (int j = 0; j < sz(v); j++)
				if (cur != j) w.pb(v[j] - 1);
			v = w;
		}
	}
	cout << res;
	printf("\n");
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		solve(it);
	}
	return 0;
}
