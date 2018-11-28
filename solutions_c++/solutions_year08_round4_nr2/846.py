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
	ifstream ifstr("b-small.in");
	ofstream ofstr("b-small.out");
	char buf[1024];
	ifstr.getline(buf, 1024);
	int n = atoi(buf);
	REP(i, n)
	{
		cout << i << "\n";
		ifstr.getline(buf, 1024);
		istringstream istr(buf);
		int m, n, a;
		istr >> n >> m >> a;
		int l1, l2;
		bool flag = false;
		FOR(i1, 0, n + 1)
			FOR(j1, 0, m + 1)
				FOR(i2, 0, n + 1)
					FOR(j2, 0, m + 1)
		{
			if (flag)
				break;
			int s2 = (i2 - i1)*(j1 + j2) + (0 - i2)*(0 + j2) + (i1 - 0)*(j1 + 0);
			if (s2 == a)
			{
				ofstr << "Case #" << i + 1 << ": " << i1 << " " << j1 << " " << i2 << " " << j2 << " " << 0 << " " << 0  <<  "\n";
				flag = true;
			}
		}
			
		if (!flag)
			ofstr << "Case #" << i + 1 << ": IMPOSSIBLE" << "\n";
	}
	return 0;
}

