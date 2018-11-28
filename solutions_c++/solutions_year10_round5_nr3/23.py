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
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

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

int s[4000000];
set <int> st;

void calc ()
{
	int n;
	cin >> n;
	seta (s, 0);
	forn (i, n)
	{
		int x, y;
		cin >> x >> y;
		forn (i, y)
			s[x+2000000] ++;
	}
	st.clear ();
	forn (i, 4000000)
		if (s[i] > 1)
			st.insert (i);
        int res = 0;
        while (st.size() > 0)
        {
        	int x = *st.begin();
        	st.erase (st.begin());
        	if (s[x] < 2)
        		continue;
        	int l = x;
        	int r = x;
        	while (s[l] > 0)
        		l --;
        	while (s[r] > 0)
        		r ++;
        	l ++;
        	r --;
        	while (l < x && x < r)
        	{
        		s[l-1] ++;
        		s[l] --;
        		s[r+1] ++;
        		s[r] --;
        		res += r - l + 1;
        		l ++;
        		r --;
        	}
       		s[l-1] ++;
       		s[l] --;
       		s[r+1] ++;
       		s[r] --;
       		res += r - l + 1;
       		l ++;
       		r --;
       		if (s[x] > 1)
       			st.insert (x);
        }
	cout << res << endl;	
}

int main ()
{
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		printf ("Case #%d: ", ii+1);
		calc ();
	}
	return 0;
}
