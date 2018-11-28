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

template<typename TContainer> TContainer rev(TContainer c) { reverse(all(c)); return c; }

int sumOfConvertToBase(int n, int b)
{
	if (n == 0) 
		return 0;

	int res = 0;
	while (n != 0)
	{
		int dig = n % b;
		res += dig * dig;
		n = (n - dig) / b;
	}
	return res;
}

vvi mem;

int get(int base, int num)
{
	int & res = mem[base][num];
	if (res != -1)
		return res;

	if (num == 1)
		return res = 1;

	res = 0;
	int sum = sumOfConvertToBase(num, base);
	if (get(base, sum) == 1)
		res = 1;

	return res;
}

bool isLucky(int num, int base)
{
	int sum = sumOfConvertToBase(num, base);
	return get(base, sum) == 1;
}

int main()
{
	string _task = "A";
	//string _in = _task + "-small.in", _out = _task + "-small.out";
	string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	mem.assign(11, vi(10000, -1));

	int x[] = { 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	int x1[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
	int x2[] = { 2, 3, 4, 5, 6, 7, 8, 10 };
	int x3[] = { 2, 3, 4, 5, 6, 7, 9, 10 };
	int x4[] = { 2, 3, 4, 5, 6, 8, 9, 10 };
	int x5[] = { 2, 3, 4, 5, 7, 8, 9, 10 };
	int x6[] = { 2, 3, 4, 6, 7, 8, 9, 10 };
	int x7[] = { 2, 3, 5, 6, 7, 8, 9, 10 };
	int x8[] = { 2, 4, 5, 6, 7, 8, 9, 10 };
	int x9[] = { 3, 4, 5, 6, 7, 8, 9, 10 };

	for (int _n = 1; _n <= _N; ++_n)
	{	
		getline(fin, ts);
		vi b = split<int>(ts);

		//{
		//	vi b1(x, x + sizeof(x) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 11814485;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x1, x1 + sizeof(x1) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 569669;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x2, x2 + sizeof(x2) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 2688153;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x3, x3 + sizeof(x3) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 711725;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x4, x4 + sizeof(x4) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 28099;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x5, x5 + sizeof(x5) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 346719;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x6, x6 + sizeof(x6) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 4817803;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x7, x7 + sizeof(x7) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 11814485;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x8, x8 + sizeof(x8) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 11814485;
		//		fout << endl;
		//		continue;
		//	}
		//}

		//{
		//	vi b1(x9, x9 + sizeof(x9) / sizeof(int));
		//	if (b == b1)
		//	{
		//		fout << "Case #" << _n << ": ";
		//		fout << 11814485;
		//		fout << endl;
		//		continue;
		//	}
		//}

		{
			if (find(all(b), 5) != b.end() && find(all(b), 6) != b.end() &&
				find(all(b), 7) != b.end() && find(all(b), 8) != b.end() &&
				find(all(b), 9) != b.end() && find(all(b), 10) != b.end())
			{
				fout << "Case #" << _n << ": ";
				fout << 11814485;
				fout << endl;
				continue;
			}
		}

		int res = 0;
		for (int i = 2; ; ++i)
		{
			bool ok = true;
			for (int j = sz(b) - 1; j >= 0; --j)
				if (!isLucky(i, b[j]))
				{
					ok = false;
					break;
				}

			if (ok)
			{
				res = i;
				break;
			}
		}
		
		fout << "Case #" << _n << ": ";
		fout << res;
		fout << endl;
	}	

	return 0;
}
