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

int d[10], d1[10];

string calc (string s)
{
	seta (d1, 0);
	forn (i, s.length())
	{
		d1[s[i]-'0'] ++;
		for (int j = s[i]-'0' + 1; j <= 9; j ++)
			if (d1[j])
			{
				d1[j] --;
				s[i] = (j + '0');
				int k = i-1;
				forn (l, 10)
					while (d1[l])
					{
						s[k] = (l + '0');
						d1[l] --;
						k --;
					}
			        reverse (all (s));
				return s;		
			}
	}
	return "";
	
}

int main ()
{
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		string s;
		cin >> s;
		seta (d, 0);
		forn (i, s.length())
			d[s[i]-'0'] ++;
		reverse (all (s));
		string res = calc (s);
		if (res == "")
		{
			d[0] ++;
			for (int i = 1; i <= 9; i ++)
				if (d[i])
				{
					res += (i + '0');
					d[i] --;
					break;
				}
			forn (i, 10)
				while (d[i])
				{
					res += (i + '0');
					d[i] --;
				}
		}
		printf ("Case #%d: ", ii+1);
		cout << res << endl;
	}
	return 0;
}
