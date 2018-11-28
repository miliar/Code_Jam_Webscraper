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
typedef pair<char, int> pci;
typedef pair<int, pii> piii;
typedef pair<int, piii> piiii;
typedef pair<pii, pii> edge;
typedef pair<int64, int64> pii64;
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

int n;
int cnt;
int a[1 << 10];
double k[1 << 10];
double v[1 << 10][1 << 10];
double f[1 << 10];

double rec(int n)
{
	if (n < 2) return 0.0;

	if (f[n] != -1.0) return f[n];

	double res = 0;
	for (int i = 1; i <= n; ++i)
		res += (1.0 + rec(n - i)) * v[n][i];
	res += v[n][0];

	res /= (1.0 - v[n][0]);
	return f[n] = res;
}

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	for (int i = 0; i < 11; ++i)
		f[i] = -1.0;

	for (int n = 1; n < 11; ++n)
	{
		memset(k, 0, sizeof k);
		for (int i = 0; i < n; ++i)
			a[i] = i;
		do
		{
			cnt = 0;
			for (int i = 0; i < n; ++i)
				if (a[i] == i) ++cnt;
			++k[cnt];
		} while (next_permutation(a, a + n));

		double Z = 1.0;
		for (int i = 1; i <= n; ++i)
			Z *= (double)i;

		for (int i = 0; i <= n; ++i)
			v[n][i] = k[i] / Z;
	}

	cin >> n;
	int m = 0, x;
	for (int i = 0; i < n; ++i)
	{
		cin >> x;
		--x;
		if (x != i) ++m;
	}
	n = m;

	double res = rec(n);
	cout.precision(7);
	cout << fixed << res << endl;

    return 0;  
}