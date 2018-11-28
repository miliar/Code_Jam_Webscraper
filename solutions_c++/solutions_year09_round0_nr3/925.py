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
const string task = "";

template <class T> T sqr (T x) {return x * x;}

char c[1000];
string s = "welcome to code jam";
int t[1000][20];

int main ()
{
	int nn;
	scanf ("%d", &nn);
	gets (c);
	forn (ii, nn)
	{
		seta (c, 0);
		seta (t, 0);
		gets (c);
		int l = strlen (c);
		forn (i, l+1)
			t[i][0] = 1;
		for (int i = 1; i <= l; i ++)
			for (int j = 1; j <= I s.length(); j ++)
			{
				t[i][j] = t[i-1][j];
				if (c[i-1] == s[j-1])
					t[i][j] = (t[i][j] + t[i-1][j-1]) % 10000;
			}
		printf ("Case #%d: %04d\n", ii+1, t[l][s.length()]);
	}
	return 0;
}
