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

int a[30];
int kols[30];
int kol=0;

bool check()
{
	for (int i=1;i<kol;i++)
	{
		if (a[i]>a[i-1])
		{
			return false;
		}
	}

	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("b.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
#endif 

	cout << setiosflags(ios::fixed) << setprecision(10);

	int n;
	string st;

	scanf("%d", &n);

	for (int i=0;i<n;i++)
	{
		clr(kols);
		cin >> st;

		kol=st.sz;

		for (int j=0;j<st.sz;j++)
		{
			a[j]=st[j]-'0';
			kols[a[j]]++;
		}

		if (check())
		{

			int nom=0;
/*
			for (int j=0;j<=9;j++)
			{
				if (kols[j]==0)
				{
					nom=j;
					break;
				}
			}
*/
			bool flag=false;

			printf("Case #%d: ", i+1);

			for (int j=1;j<=9;j++)
			{
				for (int kk=0;kk<kols[j];kk++)
				{
					cout << j;
					if (!flag)
					{
						for (int u=0;u<kols[0];u++)
						{
							cout << 0;
						}
						cout << nom;
						flag=true;
					}
				}
			}
			cout << endl;
			
		} else
		{
			next_permutation(a,a+kol);

			printf("Case #%d: ", i+1);

			for (int j=0;j<kol;j++)
			{
				cout << a[j];
			}
			cout << endl;
		}
	}
	

	return 0;
}
