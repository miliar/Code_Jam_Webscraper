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
#include <iomanip>
#include <cmath>
#include <cassert>

using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<ll>
#define vvl vector<vl>
#define vd vector<double>
#define vvd vector<vd>
#define vp vector<pii>
#define vvp vector<vp>
#define msi map<string, int>
#define mii map<int, int>

#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define twoLL(n) (1LL << (n))
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

inline ll abs(ll a) { return (a < 0) ? -a : a; }
inline ll pow(int a, int b) { ll res = 1; for (int i = 1; i <= b; ++i) res *= a; return res; }
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(s); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9

int main()
{
	string _task = "C";
	//string _in = _task + "-small.in", _out = _task + "-small.out";
	string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	string word = "welcome to code jam";

	for (int _n = 1; _n <= _N; ++_n)
	{	
		string s;
		getline(fin, s);

		int res = -1;

		int n = sz(s), m = sz(word);
		vvl dp(n, vl(m, 0));
		
		if (n < m)
		{
			res = 0;
			goto answer;
		}
		
		if (s[0] == word[0]) 
			dp[0][0] = 1;
		for (int i = 1; i < n; ++i)
			dp[i][0] = dp[i - 1][0] + ((s[i] == word[0]) ? 1 : 0);
				
		for (int j = 1; j < m; ++j)
			for (int i = j; i < n; ++i)
				dp[i][j] = (dp[i - 1][j] + ((s[i] == word[j]) ? dp[i - 1][j - 1] : 0)) % 10000;

		res = (int)dp[n - 1][m - 1];
		
answer:
		fout << "Case #" << _n << ": ";
		string r = cast<string>(res % 10000);
		while (sz(r) < 4)
			r = '0' + r;
		fout << r;
		fout << endl;
	}	

	return 0;
}
