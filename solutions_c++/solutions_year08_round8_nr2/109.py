#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

#define assert_equal(x, y) {if ((x) != (y)) {cout << (x) << " != " << (y) << endl; exit(1);}}
#define assert_nequal(x, y) {if ((x) == (y)) {cout << (x) << " == " << (y) << endl; exit(1);}}
#define print(x) cout <<"'"<< x << "'" << endl
#define print_array(x, n) {for (int __i = 0; __i < (n); ++__i) cout << " '" << x[__i] << "'"; cout << endl;}
#define print_array2d(x, m, n) {cout << endl << "----" << endl; for (int _i = 0; _i < (m); ++_i, cout << endl) {print_array((x)[(_i)], (n));}}
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair


FILE *in, *out;
const int N = 402;
const int oo = 0x3f3f3f3f;
int n, m;
vector < pair<int, int> > a[N];

int span[N][3*N];

struct RMQ
{
	int n;
	int base;
	int size;	
	int a[6*N];
	RMQ(int n)
	{
		this->n = n;
		base = 2;
		int leaves = 2;
		while (leaves < n)
		{
			base += leaves;
			leaves *= 2;
		}
		size = base + leaves;
		memset(a, oo, sizeof(a));
	}
	void set(int i, int value)
	{
		a[base + i] = value;
		for (int k = (base + i) / 2; k >= 1; k /= 2)
		{
			a[k] = min(a[2 * k], a[2 * k + 1]);
		}
	}
	int getMin(int lo, int up)
	{
		lo += base;
		up += base;
		int res = min(a[lo], a[up]);
		for (int pl = lo / 2, pu = up / 2; pl != pu; lo = pl, up = pu, pl /= 2, pu /= 2)
		{
			if (2 * pl + 1 != lo) res = min(res, a[2 * pl + 1]);
			if (2 * pu + 0 != up) res = min(res, a[2 * pu + 0]);
		}
		return res;
	}
};

int main(int argc, char* argv[])
{
    string filename = (argc == 2 ? argv[1] : "b");
    print("processing file: " << filename);
    in = fopen((filename + ".in").c_str(), "r"); assert_nequal(in, 0);
    out = fopen((filename + ".out").c_str(), "w"); assert_nequal(out, 0);
    int cases;
    fscanf(in, "%d", &cases);
    for (int caseno = 1; caseno <= cases; ++caseno)
    {
        print("case: " << caseno);
		
		
		for (int i = 0; i < N; ++i) a[i].clear();

		map <string, int> id;

		fscanf(in, "%d", &n);

		map<int, int> x;
		x[0] = 0;
		x[10000] = 0;

		for (int i = 0; i < n; ++i)
		{
			char str[16];
			int clr, fr, to;
			fscanf(in, " %s %d %d", str, &fr, &to);
			if (id.count(str)) clr = id[str];
			else {clr = id.size(); id[str] = clr;}
			
			
			if (fr > to) swap(fr, to);
			fr --;
			x[fr] = 0;
			x[to] = 0;
			a[clr].push_back(make_pair(to, fr));
		}
		n = id.size() + 2;
		if (caseno == 11) print(n);
		int m = 0;
		for (map<int,int>::iterator it = x.begin(); it != x.end(); ++it)
		{
			it->second = m;
			m++;
		}
		if (caseno == 11) print(m);
		for (int c = 0; c < n; ++c)
		{
			for (int i = 0; i < m; ++i) span[c][i] = oo;
			for (int i = 0; i < (int)a[c].size(); ++i)
			{
				int to = x[a[c][i].first];
				int fr = x[a[c][i].second];
				span[c][to] = min(span[c][to], fr);
			}
		}
		
		int res = oo;
		for (int i1 = 0; i1 < n; ++i1)
		for (int i2 = i1+1; i2 < n; ++i2)
		for (int i3 = i2+1; i3 < n; ++i3)
		{
			RMQ rmq(m);
			rmq.set(0, 0);
			for (int k = 1; k < m; ++k)
			{
				int mn = oo;
				if (span[i1][k] < oo) mn = min(mn, rmq.getMin(span[i1][k], k) + 1);
				if (span[i2][k] < oo) mn = min(mn, rmq.getMin(span[i2][k], k) + 1);
				if (span[i3][k] < oo) mn = min(mn, rmq.getMin(span[i3][k], k) + 1);
				if (mn < oo) rmq.set(k, mn);
			}
			int cur = rmq.getMin(m-1, m-1);
			if (cur < res) res = cur;
		}
		if (res == oo) fprintf(out, "Case #%d: IMPOSSIBLE\n", caseno, res);
		else fprintf(out, "Case #%d: %d\n", caseno, res);
    }
    return 0;
}