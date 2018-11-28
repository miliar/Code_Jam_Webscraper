#define _USE_MATH_DEFINES  
#define _CRT_SECURE_NO_DEPRECATE  
  
#include <algorithm>  
#include <bitset>  
#include <cassert>  
#include <cmath>  
#include <cstdio>  
#include <cstdlib>  
#include <cstring>   
#include <deque>  
#include <functional>  
#include <iomanip>  
#include <iostream>  
#include <list>  
#include <map>  
#include <numeric>  
#include <queue>  
#include <set>  
#include <sstream>  
#include <stack>  
#include <string>  
#include <utility>  
#include <vector>  
  
using namespace std;  
  
#pragma comment(linker, "/STACK:64000000")  
  
#define problem "Khaustov"  

typedef long long int64;  
typedef unsigned long long ull;
typedef unsigned char byte;  
typedef pair<int, int> pii;
typedef pair<int64, int64> pii64;
typedef pair<pii64, int64> piii;
typedef pair<int, piii> piiii;
typedef pair<pii, pii> edge;
typedef pair<int64, pii64> shit;
typedef pair<pii64, int> piii64;
typedef pair<double, int> pdi;
typedef pair<pdi, int> pdii;
typedef pair<int, string> pis;
typedef vector<int> vi;  
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<pii> vpii;  
typedef vector<vpii> vvpii;  
typedef vector<string> vs;  
typedef vector<vs> vvs;  
typedef list<int> li;   
  
#define y1 _dsfdsfkn
#define left _dsfdsf
#define right _dfjdsj
#define link _tsu_sux
#define prime 1103
#define eps 1e-6
#define inf 123456789
#define toMod 1000000007LL

int n, nt;
double res;
int X, S, R;
double t;
pdi a[1 << 10];
int s[1 << 10];
int w[1 << 10]; 

inline double calc(double s, double v)
{
	return s / v;
}

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	cout.precision(10);
	for (int tn = 1; tn <= nt; ++tn)
	{
		cin >> X >> S >> R >> t;
		R = max(0, R - S);
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			int from, to;
			cin >> from >> to >> w[i];
			w[i] += S;
			s[i] = to - from;
			X -= s[i];
			a[i].first = (double)1.0 / ((double)w[i] * (double)(w[i] + R));
			a[i].second = i;
		}
		res = 0.0;
		a[n] = pii(X, S);
		s[n] = X;
		w[n] = S;
		a[n].first = (double)1.0 / ((double)w[n] * (double)(w[n] + R));
		a[n].second = n;
		++n;
		sort(a, a + n);
		reverse(a, a + n);
		for (int i = 0; i < n; ++i)
		{
			int x = a[i].second;
			double T = calc((double)s[x], (double)(w[x] + R));
			if (T > t)
			{
				res += t;
				double TS = (double)s[x] - t * (double)(w[x] + R);
				t = 0.0;
				double add = calc(TS, (double)w[x]);
				res += add;
				continue;
			}
			t -= T;
			res += T;
		}
		cout << "Case #" << tn << ": ";
		cout << fixed << res << endl;
	}

    return 0;  
}