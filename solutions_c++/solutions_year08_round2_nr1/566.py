#include <vector>
#include <string>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <functional>
#include <sstream>
#include <iostream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <cmath>

using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vp vector<pii>
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

template<typename T> vector<T> split(string s, string d = "") { for (int i = 0; i < sz(d); ++i) replace(all(s), d[i], ' '); vector<T> v; istringstream iss(s); T t; while (iss >> t) v.push_back(t); return v; }
template<typename R, typename T> R cast(T t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9
#define FOR(i, a, b) for (size_t i = a, _n = b; i < _n; ++i)
#define REP(i, n)  for (size_t i = 0, _n = n; i < _n; ++i)

int main(int argc, char* argv[])
{
	ifstream ifstr("A-small.in");
	ofstream ofstr("A-small.out");
	char buf[1024];
	ifstr.getline(buf, 1024);
	int N = atoi(buf);
	REP(i, N)
	{
		ifstr.getline(buf, 1024);
		ll n, A, B, C, D, x0, y0, M;
		istringstream istr(buf);
		istr >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector<pair<ll, ll> > trees;
		trees.push_back(make_pair(x0, y0));
		ll x = x0;
		ll y = y0;
		REP(j, n - 1)
		{
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			trees.push_back(make_pair(x, y));
		}
		sort(trees.begin(), trees.end());
		trees.erase(unique(trees.begin(), trees.end()), trees.end());
		ll res = 0;
		FOR(k, 0, n)
			FOR(l, k + 1, n)
				FOR(m, l + 1, n)
		{
			if ((trees[k].first + trees[l].first + trees[m].first) % 3 == 0 &&
				(trees[k].second + trees[l].second + trees[m].second) % 3 == 0)
				++res;
		}


		ofstr << "Case #" << i + 1 << ": " << res << "\n";
	}
	return 0;
}

