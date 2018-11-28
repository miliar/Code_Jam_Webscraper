#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
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

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pf push_front
#define mp make_pair
#define popf pop_front
#define popb pop_back
#define sz size()
#define fst first
#define snd second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(int i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

char ch[128];
string name;
int kol;
string charac[128];

ld tolcc(string x)
{
	ld res=0.0;
	for (int i=int(x.sz)-1;i>=0;i--)
	{
		res*=10.0;
		res+=(x[i]-'0')*1.0;
	}
	return res;
}

ld toldc(string x)
{
	ld res=0.0;
	for (int i=0;i<int(x.sz);i++)
	{
		res*=10.0;
		res+=(x[i]-'0')*1.0;
	}
	return res;
}

ld told(string x)
{
	string cc="",dc="";

	int i=0;

	while (x[i]!='.' && i<(int)x.sz)
	{
		cc+=x[i];
		i++;
	}
	i++;
	while (i<(int)x.sz)
	{
		dc+=x[i];
		i++;
	}

	if (dc=="")
	{
		dc="0";
	}

//	cerr << x << " " << tolcc(cc)+(toldc(dc))/pow(10.0,(int)dc.sz) << endl;

	return tolcc(cc)+(toldc(dc))/pow(10.0,(int)dc.sz);

}

bool ischar(char x)
{
	return (x>='a' && x<='z' || x>='A' && x<='Z');
}

ld get_ans(string tree)
{
	ld prob=0;
//	int n=(int)tree.sz;
	int i=1;

	tree+="      ";

//	cerr << "Enter\n";
//	cerr << tree << endl;

	string probst="";

	while (isdigit(tree[i]) || tree[i]=='.')
	{
		probst+=tree[i];
    /*
		if (isdigit(tree[i]))
		{
			if (tree[i+1] == '.')
			{
				prob=(tree[i] - '0')*1.0 + ((tree[i+2]-'0')*1.0)/10.0;
				i=i+3;
				break;
			} else
			{
				prob=(tree[i] - '0')*1.0;
				i=i+1;
				break;
			}
		}
    */
    	i++;
	}
	

//	cerr << probst << endl;
	prob=told(probst);
//	cerr << prob << endl;

	if (tree[i]==')')
	{
//		cerr << "!" << endl;
		return prob;
	}

	string feat="";

	if (ischar(tree[i]))
	{
		while (tree[i]!='(' && tree[i]!=')')
		{
			feat+=tree[i];
			i++;
		}
	}

	if (tree[i]==')')
	{
		return prob;
	}

	string ltree="(";

	int bal=1;
	i++;

	while (bal!=0)
	{
		ltree+=tree[i];
		if (tree[i]=='(')
		{
			bal++;
		}
		if (tree[i]==')')
		{
			bal--;
		}
		i++;
	}

	if (tree[i]==')')
	{

		bool flag=false;

		for (int i=0;i<kol;i++)
		{
			if (charac[i]==feat)
			{
				flag=true;
				break;
			}
		}

		if (flag)
		{
			return prob*get_ans(ltree);
		} else
		{
			return prob;
		}
	}

	string rtree="(";

	bal=1;
	i++;

	while (bal!=0)
	{
		rtree+=tree[i];
		if (tree[i]=='(')
		{
			bal++;
		}
		if (tree[i]==')')
		{
			bal--;
		}
		i++;
	}

	bool flag=false;

	for (int i=0;i<kol;i++)
	{
		if (charac[i]==feat)
		{
			flag=true;
			break;
		}
	}

	if (flag)
	{
		return prob*get_ans(ltree);
	} else
	{
		return prob*get_ans(rtree);
	}

	return -1;

	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
#endif 

	cout << setiosflags(ios::fixed) << setprecision(7);

	int t,n,k;

	scanf("%d", &t);


	for (int o=0;o<t;o++)
	{
		scanf("%d", &k);
		gets(ch);

		string tree="";
		string sd;

		for (int i=0;i<k;i++)
		{
			gets(ch);
			sd=ch;

			for (int j=0;j<(int)sd.sz;j++)
			{
				if (sd[j]!=' ')
				{
					tree+=sd[j];
				}
			}

		}

//			cerr << tree << endl;

		printf("Case #%d:\n", o+1);

		scanf("%d", &n);

		for (int i=0;i<n;i++)
		{
			cin >> name >> kol;

			for (int j=0;j<kol;j++)
			{
				cin >> charac[j];
			}

			cout << get_ans(tree) << endl;
		}
//		cout << endl;
	}
	

	return 0;
}
