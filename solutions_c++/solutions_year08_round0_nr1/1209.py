#include <vector>
#include <string>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<ll>
#define vvl vector<vl>
#define vd vector<ld>
#define vvd vector<vd>
#define vp vector<pii>
#define msi map<string, int>
#define mii map<int, int>

#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define twoLL(n) (1LL << (n))
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

inline long long abs(long long a) { return (a < 0) ? -a : a; }
inline long long pow(int a, int b) { long long res = 1; for (int i = 1; i <= b; ++i) res *= a; return res; }
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(str); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9

int main(int argc, char* argv[])
{
	string _task = "A";
	//string _in = _task + "-small.in", _out = _task + "-small.out";
	string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string s;
	getline(fin, s);
	int N = atoi(s.c_str());

	for (int _n = 1; _n <= N; ++_n)
	{
		getline(fin, s);
		int n = atoi(s.c_str());
		for (int i = 0; i < n; ++i)
			getline(fin, s);

		getline(fin, s);
		int m = atoi(s.c_str());
		vs eng(m);
		for (int i = 0; i < m; ++i)
			getline(fin, eng[i]);
		
		int res = 0;
		set<string> se;
		for (int i = 0; i < m; ++i)
		{
			se.insert(eng[i]);
			if (sz(se) == n)
			{
				++res;
				se.clear();
				se.insert(eng[i]);
			}
		}

		fout << "Case #" << _n << ": ";
		fout << res;
		fout << endl;
	}	

	return 0;
}
