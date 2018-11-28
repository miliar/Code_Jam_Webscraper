#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

int R, k, N;
int a[2000], next[1000];
int64 s[1000];

void calc (int ii)
{
	scanf ("%d%d%d", &R, &k, &N);
	forn (i, N)
	{
		scanf ("%d", &a[i]);
		a[i+N] = a[i];
	}
	forn (i, N)
	{
		s[i] = 0;
		next[i] = 0;
		while (next[i] < N && s[i] + a[i+next[i]] <= k)
		{
			s[i] += a[i+next[i]];
			next[i] ++;
		}
		next[i] = (i + next[i]) % N;
	}
	int64 res = 0;
	int p = 0;
	forn (i, R)
	{
		res += s[p];
		p = next[p];
	}
	cout << "Case #" << ii << ": ";
	cout << res << endl;
	cerr << "Case #" << ii << ": ";
	cerr << res << endl;
}

int main ()
{
	int tt;
	cin >> tt;
	forn (ii, tt)
		calc (ii+1);
	return 0;
}
