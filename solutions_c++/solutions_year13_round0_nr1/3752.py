#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int n;
string s[4];
char a[4][4];

bool solve(char c)
{
	//line
	forn(i,4)
	{
		bool b=1;
		forn(j,4)
			if(a[i][j]=='.' || a[i][j]==c)
				b=0;
		if(b)
			return 1;
	}
	//stolb
	forn(i,4)
	{
		bool b=1;
		forn(j,4)
			if(a[j][i]=='.' || a[j][i]==c)
				b=0;
		if(b)
			return 1;
	}
	//diag
	bool b=1;
	forn(i,4)
		if(a[i][i]=='.' || a[i][i]==c)
				b=0;
	if(b)
		return 1;
	//pob diag
	b=1;
	forn(i,4)
		if(a[i][4-i-1]=='.' || a[i][4-i-1]==c)
				b=0;
	if(b)
		return 1;
	return 0;
}

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);

	cin >>n;
	forn(k,n)
	{
		bool fl=0;
		forn(i,4)
		{
			cin >>s[i];
			forn(j,4)
			{
				a[i][j]=s[i][j];
				if(a[i][j]=='.')
					fl=1;
			}
		}
		cout <<"Case #"<<k+1<<": ";
		if(solve('O'))
			cout <<"X won";
		else if(solve('X'))
			cout <<"O won";
		else if(fl)
			cout <<"Game has not completed";
		else
			cout <<"Draw";
		cout <<endl;
	}

	return 0;
}
