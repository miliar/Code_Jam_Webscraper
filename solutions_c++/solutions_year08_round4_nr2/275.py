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

#define inf 2100000000
#define eps 1e-9

int main(int argc, char* argv[])
{
	string _task = "B";
	string _in = _task + "-small.in", _out = _task + "-small.out";
	//string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string s;
	getline(fin, s);
	int N = atoi(s.c_str());

	for (int _n = 1; _n <= N; ++_n)
	{
		// don't forget to clear all global objects!

		getline(fin, s);
		//int n = atoi(s.c_str());
		vi t = split<int>(s);
		int n = t[0], m = t[1];
		int a = t[2];

		
		int x1, x2, x3, y1, y2, y3;
		x1 = x2 = x3 = y1 = y2 = y3 = -1;

		for (int c1 = 0; c1 <= n; ++c1)
			for (int c2 = 0; c2 <= n; ++c2)
				for (int c3 = 0; c3 <= m; ++c3)
					for (int c4 = 0; c4 <= m; ++c4)
					{
						if (abs(c1 * c4 - c3 * c2) == a)
						{
							x1 = n;
							x2 = x1 - c1;
							x3 = x1 - c2;
							y1 = m;
							y2 = y1 - c3;
							y3 = y1 - c4;
							break;
						}
					}


		fout << "Case #" << _n << ": ";
		
		if (x1 == -1)
			fout << "IMPOSSIBLE";
		else
		{
			//int area = abs((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3));
			//cout << area << " " << a;
			fout << x1 << " " << y1  << " " << x2 << " " <<  y2 << " " <<  x3 << " " << y3;
		}

		fout << endl;
	}	

	return 0;
}
