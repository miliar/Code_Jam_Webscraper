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

int leng, s, r, t, cnt;
vector <pt> v;

ld solve ()
{
	ld res = 0.0;
	
	sort(all(v));
	
	ld remt = t;
	
	ld D = leng;

	forn(i, sz(v))
		D -= v[i].sc;
	
	if (remt > EPS)
	{
		ld willt = D / r;
		
		if (willt > remt + EPS)
		{
			res += remt;
			ld remd = D - remt * r;
			res += remd / s;
			remt = 0;
		
		} else
		{
			remt -= willt;
			res += willt;
		}
		
	} else
	{
		ld willt = D / s;
		res += willt;
	}
	
	forn(i, sz(v))
	{
		D -= v[i].sc;
	
		ld d = v[i].sc;
		
		if (remt > EPS)
		{
			ld willt = d / (r + v[i].ft);
			
			if (willt > remt + EPS)
			{
				res += remt;
				ld remd = d - remt * (r + v[i].ft);
				res += remd / (s + v[i].ft);
				remt = 0;
			
			} else
			{
				remt -= willt;
				res += willt;
			}
		
		} else
		{
			ld willt = d / (s + v[i].ft);
			res += willt;
		}
	}

	return res;
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		scanf("%d%d%d%d%d", &leng, &s, &r, &t, &cnt);
		v.clear();
		
		forn(i, cnt)
		{
			int lf, rg, ww;
			scanf("%d%d%d", &lf, &rg, &ww);
			
			v.pb(mp(ww, rg - lf));
		}
		
		printf("Case #%d: %.10lf\n", test + 1, double(solve()));
	}

	return 0;
}
























































