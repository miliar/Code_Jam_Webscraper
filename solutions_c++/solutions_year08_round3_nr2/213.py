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
	ifstream ifstr("B-small.in");
	ofstream ofstr("B-small.out");
	char buf[1024];
	ifstr.getline(buf, 1024);
	int n = atoi(buf);
	REP(i, n)
	{
		cout << i << endl;
		ifstr.getline(buf, 1024);
		string str = buf;
		ll d = sz(str);
		ll num = 1;
		REP(j, d - 1)
			num *= 3L;
		ll res = 0;
		vector<ll> nums;
		nums.reserve(10);
		vector<ll> ops;
		ops.reserve(10);
		ll buf[16];
		REP(j, num)
		{
			ll temp = j; 
			REP(k, d)
			{
				buf[k] = temp % 3;
				temp /= 3;
			}
			string cur(1, str[0]);
			nums.clear();
			ops.clear();
			REP(k, d - 1)
			{
				if (buf[k] == 0)
				{
					cur += str[k + 1];
					continue;
				}
				nums.push_back(_atoi64(cur.c_str()));
				cur = str[k + 1];
				ops.push_back(buf[k]);
			}
			nums.push_back(_atoi64(cur.c_str()));
			reverse(nums.begin(), nums.end());
			reverse(ops.begin(), ops.end());
			ll nn = nums[0];
			REP(k, sz(ops))
			{
				ll next = nums[k + 1];
				if (ops[k] == 1)
					nn += next;
				else
					nn -= next;
			}

			if (nn % 2 == 0 || nn % 3 == 0 || nn % 5 == 0 || nn % 7 == 0)
				++res;
		}


		ofstr << "Case #" << i + 1 << ": " << res << "\n";
	}
	return 0;
}

