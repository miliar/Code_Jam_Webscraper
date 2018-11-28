#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define ft first
#define sc second

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long double ld;
typedef pair<ld, ld> ptd;
typedef pair <int, int> pt;
typedef long long li;
typedef unsigned char byte;

const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int N = 100 + 13;

int n;
char a[N][N];
ld ans[N];
ld wp[N], owp[N], oowp[N];

void solve()
{
	forn(i, n)
	{
		wp[i] = 0.0;
		owp[i] = 0.0;
		oowp[i] = 0.0;
		ans[i] = 0.0;
	}

	forn(i, n)
	{
		int win = 0, cnt = 0;
		
		forn(j, n)
		{
			if (a[i][j] == '1')
				win++;
				
			if (a[i][j] != '.')
				cnt++;
		}
		
		wp[i] = win * 1.0 / cnt;
		
		int cntop = 0;
		ld sum = 0.0;
		
		forn(j, n)
			if (a[i][j] != '.')
			{
				int cntj = 0, winj = 0;
			
				forn(k, n)
				{
					if (k == i)
						continue;
						
					if (a[j][k] != '.')
						cntj++;
						
					if (a[j][k] == '1')
						winj++;
				}
				
				assert(cntj != 0);
				
				cntop++;
				sum += winj * 1.0 / cntj;
			}
			
		assert(cntop != 0);
			
		owp[i] = sum / cntop;
	}
	
	forn(i, n)
	{
		int cntop = 0;
		ld sum = 0.0;
		
		forn(j, n)
			if (a[i][j] != '.')
				sum += owp[j], cntop++;
				
		assert(cntop != 0);
				
		oowp[i] = sum / cntop;
	}
	
	forn(i, n)
		ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		cin >> n;
		
		forn(i, n)
			scanf("%s", a[i]);
			
		solve();
		
		printf("Case #%d:\n", test + 1);
		
		forn(i, n)
			printf("%.10lf\n", double(ans[i]));
	}

	return 0;
}
























































