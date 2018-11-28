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

struct node
{
	double w;
	string f;
	int l, r;
};

node a[100000];
stringstream ss;
int n;

int go ()
{
	int v = n;
	n ++;
	string s;
	ss >> s;
	sscanf (s.data(), "%lf", &a[v].w);
	ss >> s;
	a[v].f = "";
	if (s != ")")
	{
		a[v].f = s;
		ss >> s;
		int l = go ();
		ss >> s;
		int r = go ();
		a[v].l = l;
		a[v].r = r;
		ss >> s;
	}
	return v;
}

set <string> st;
int root;

double calc ()
{
	int v = root;
	double res = a[root].w;
	string s;
	cin >> s;
	int num;
	cin >> num;
	st.clear ();
	forn (i, num)
	{
		cin >> s;
		st.insert (s);
	}
	while (a[v].f != "")
	{
		if (st.count(a[v].f))
			v = a[v].l;
		else
			v = a[v].r;
		res *= a[v].w;
	}
	return res;
}

char c[10000];

int main (int argc, char **argv)
{
	if (argc != 2)
		return 0;
	if (argv[1][0] == '1')
	{
	char ch;
	while (scanf ("%c", &ch) > 0)
	{
		if (ch == '(')
			printf ("%c ", ch);
		else
		if (ch == ')')
			printf (" %c", ch);
		else
			printf ("%c", ch);		
	}
        return 0;
        }
        int tt;
        scanf ("%d", &tt);
        cerr << tt << endl;
        forn (ii, tt)
        {
        	int l;
        	scanf ("%d", &l);
        	ss.clear ();
        	gets (c);
        	forn (j, l)
        	{
        		gets (c);
        		ss << c << " ";
        	}
		n = 0;
		string s;
		ss >> s;
		root = go ();
		int k;
		printf ("Case #%d:\n", ii+1);
		scanf ("%d", &k);
		forn (i, k)
		{
			double x = calc ();
			printf ("%.7lf\n", x);
		}
        }
	
	return 0;
}
