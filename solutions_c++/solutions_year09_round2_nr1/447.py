#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
#include <map>  
#include <set>  

using namespace std;  

typedef long long i64;
typedef unsigned long long u64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;   

const int inf = 1<<30;

#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()   
#define forr(it,b,lim) for (it = (b); it < (lim); ++it)
#define forn(it,b,lim) for (it = (b); it >= (lim); --it)
#define rep(it,lim) for (it = 0; it < (lim); ++it)
#define mset(array,value) memset(array, value, sizeof(array))

char in[] = "A-large.in";
char out[] = "A-large.out";


string S;

struct token
{
	token(string S) {s = S, d = -1.0, c = 0;}
	token(char C) {s = "", d = -1.0, c = C;}
	token(double D) {s = "", d = D, c = 0;}
	double d;
	char c;
	string s;
};

struct T
{
	T(string S)
	{ s = S, d = -1.0, li = ri = -1; }
	T(double D, string S)
	{ s = S, d = D, li = ri = -1; }
	T()
	{ s = "", d = -1.0, li = ri = -1; }
	string s;
	double d;
	int li, ri;
};

vector<token> v;
vector<T> b;

int pos;
int rec()
{
	if (pos >= v.size())
		return -1;

	if (v[pos].c == '(')
	{
		++pos;
		double d = v[pos].d;
		int le = -1, re = -1;
		string S;
		++pos;

		if (v[pos].s.size())
		{
			S = v[pos].s;
			++pos;
			le = rec();
			re = rec();
		}
		++pos;

		T t;
		t.d = d, t.s = S, t.li = le, t.ri = re;
		b.pb( t );

		return b.size() - 1;
	}
}

double dfs (int root, vs &ftrs)
{
	double res = b[root].d;
	if (b[root].li == -1)
		return res;
	if (find(all(ftrs), b[root].s) != ftrs.end())
		res *= dfs(b[root].li, ftrs);
	else res *= dfs(b[root].ri, ftrs);
	return res;
}
char s[1000];
int main()
{
	int i, j;
	freopen(in, "rt", stdin); 
	freopen(out, "wt", stdout);

	int T, test;
	gets(s);
	sscanf(s, "%d", &T);

	rep(test, T)
	{
		int res = 0;
		int n;
		gets(s);
		sscanf(s, "%d", &n);

		S = "";

		v.clear();
		for (i = 0; i < n; ++i)
		{
			gets(s);
			int len = strlen(s);
			for (j = 0; j < len; )
			{
				if (s[j] == '(' || s[j] == ')' )
					v.pb(token(s[j])), ++j;
				else if ( isdigit(s[j]) || s[j] == '.' )
				{
					double d;
					sscanf(s + j, "%lf", &d);
					while (isdigit(s[j]) || s[j] == '.')
						++j;
					v.pb(token(d));
				}
				else if (isalpha(s[j]))
				{
					int k = j;
					while (isalpha(s[k]))
						++k;
					string S(s + j, s + k);
					j = k;
					v.pb(token(S));
				}
				else j++;
			}
		}

		b.clear();

		pos = 0;
		rec();

		int m;
		gets(s);
		sscanf(s, "%d", &m);

		printf ("Case #%d:\n", test + 1);

		for (i = 0; i < m; ++i)
		{
			char f[1000];
			int nm;
			gets(s);
			stringstream read(s);

			read >> f;
			read >> nm;
			vs ft;
			while(nm--)
			{
				read >> f;
				ft.pb(f);
			}

			rep(j, nm)
			{
				gets(f);
				ft.pb(f);
			}

			printf ("%lf\n", dfs(b.size() - 1, ft));
		}

		
	}

	return 0;
}