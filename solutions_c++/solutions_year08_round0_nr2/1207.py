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
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(s); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9

int get(vp const & sc)
{
	int res = 0;
	int av = 0;
	for (int i = 0; i < sz(sc); ++i)
	{
		if (sc[i].second == 0)
			++av;
		else
		{
			if (av == 0)
				++res;
			else
				--av;
		}
	}
	return res;
}

int main(int argc, char* argv[])
{
	string _task = "B";
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
		int T = atoi(s.c_str());
		getline(fin, s);
		vi t = split<int>(s);
		int n = t[0], m = t[1];

		vp ab, ba;
		for (int i = 0; i < n; ++i)
		{
			getline(fin, s);
			vi t1 = split<int>(s, ":");
			int depT = t1[0] * 60 + t1[1], arrT = t1[2] * 60 + t1[3];
			ab.push_back(pii(depT, 1));
			ba.push_back(pii(arrT + T, 0));
		}
		for (int i = 0; i < m; ++i)
		{
			getline(fin, s);
			vi t1 = split<int>(s, ":");
			int depT = t1[0] * 60 + t1[1], arrT = t1[2] * 60 + t1[3];
			ba.push_back(pii(depT, 1));
			ab.push_back(pii(arrT + T, 0));
		}
		
		sort(all(ab));
		sort(all(ba));

		int resA = get(ab), resB = get(ba);

		fout << "Case #" << _n << ": ";
		fout << resA << " " << resB;
		fout << endl;
	}	

	return 0;
}
