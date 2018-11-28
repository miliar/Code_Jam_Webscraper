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
#define vvp vector<vp>
#define msi map<string, int>
#define mii map<int, int>

#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define twoLL(n) (1LL << (n))
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

inline long long abs(long long a) { return (a < 0) ? -a : a; }
inline long long pow(int a, int b) { long long res = 1; for (int i = 1; i <= b; ++i) res *= a; return res; }
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(s); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 100000000
#define eps 1e-9

vp gr;

vvi memo;

int get(int v, int d)
{
	if (memo[v][d] != -1)
		return memo[v][d];

	if (gr[v].second == -1)
	{
		if (gr[v].first == d)
			return memo[v][d] = 0;
		else
			return memo[v][d] = inf;
	}

	if (gr[v].second == 0)
	{
		if (gr[v].first == 0 && d == 0)
		{
			int r = get(2 * v + 1, 0) + get(2 * v + 2, 0);
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 0 && d == 1)
		{
			int r = min(get(2 * v + 1, 1), get(2 * v + 2, 1));
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 1 && d == 0)
		{
			int r = min(get(2 * v + 1, 0), get(2 * v + 2, 0));
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 1 && d == 1)
		{
			int r = get(2 * v + 1, 1) + get(2 * v + 2, 1);
			r = min(r, inf);
			return memo[v][d] = r;
		}
	}
	else
	{
		if (gr[v].first == 0 && d == 0)
		{
			int r = get(2 * v + 1, 0) + get(2 * v + 2, 0);
			r = min(r, min(get(2 * v + 1, 0), get(2 * v + 2, 0)) + 1);
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 0 && d == 1)
		{
			int r = min(get(2 * v + 1, 1), get(2 * v + 2, 1));
			r = min(r, get(2 * v + 1, 1) + get(2 * v + 2, 1) + 1);
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 1 && d == 0)
		{
			int r = min(get(2 * v + 1, 0), get(2 * v + 2, 0));
			r = min(r, get(2 * v + 1, 0) + get(2 * v + 2, 0) + 1);
			r = min(r, inf);
			return memo[v][d] = r;
		}
		else if (gr[v].first == 1 && d == 1)
		{
			int r = get(2 * v + 1, 1) + get(2 * v + 2, 1);
			r = min(r, min(get(2 * v + 1, 1), get(2 * v + 2, 1)) + 1);
			r = min(r, inf);
			return memo[v][d] = r;
		}
	}

	cout << "error";
	return -1;
}

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
		// don't forget to clear all global objects!
		gr.clear();
		memo.clear();

		getline(fin, s);
		//int n = atoi(s.c_str());
		vi t = split<int>(s);
		int M = t[0], V = t[1];


		
		for (int i = 0; i < (M - 1) / 2; ++i)
		{
			getline(fin, s);
			vi t1 = split<int>(s);
			gr.push_back(pii(t1[0], t1[1]));
		}
		for (int i = 0; i < (M + 1) / 2; ++i)
		{
			getline(fin, s);
			vi t1 = split<int>(s);
			gr.push_back(pii(t1[0], -1));
		}

		memo.assign(M, vi(2, -1));

		int res = get(0, V);
		

		fout << "Case #" << _n << ": ";
		
		if (res == inf)
			fout << "IMPOSSIBLE";
		else
			fout << res;

		fout << endl;
	}	

	return 0;
}
