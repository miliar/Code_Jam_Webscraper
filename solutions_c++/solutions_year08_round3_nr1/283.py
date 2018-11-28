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
	ifstream ifstr("A-large.in");
	ofstream ofstr("A-large.out");
	char buf[102400];
	ifstr.getline(buf, 102400);
	int n = atoi(buf);
	REP(i, n)
	{
		ifstr.getline(buf, 102400);
		istringstream istr1(buf);
		ll p, k, l;
		istr1 >> p >> k >> l;
		ifstr.getline(buf, 102400);
		vector<ll> freq = split<ll>(buf, " ");
		sort(freq.begin(), freq.end());
		reverse(freq.begin(), freq.end());
		ll res = 0;
		REP(j, sz(freq))
			res += freq[j] * (j / k + 1);
		ofstr << "Case #" << i + 1 << ": " << res << "\n";
	}
	return 0;
}

