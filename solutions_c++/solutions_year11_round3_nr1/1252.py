#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <bitset>
#include <set>


#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define inp(x) rep(i, sz(x)) cin >> (x)[i];
#define out(x) rep(i, sz(x)) cout << (x)[i];
#define sqr(x) ((x) * (x))

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

int main(int argc, char **argv)
{
	//Small
	/*freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w+", stdout);*/


	//Large
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);

	int tt;
	cin >> tt;
	for(int t=1; t<=tt; t++)
	{
		int r, c;
		scanf("%d%d", &r, &c);
		printf("Case #%d:\n", t);
		vs a(r);
		for(int i=0; i<r; i++)
		{
			cin >> a[i];
		}
		
		bool ok=true;
		for(int i=0; i<r; i++)
		for(int j=0; j<c; j++)
		{
			if(a[i][j]=='#' && (i==0 || a[i-1][j]!='#') && (j==0 || a[i][j-1]!='#'))
			{
				if(i==r-1 || a[i+1][j]!='#')
					ok=false;
				else if(j==c-1 || a[i][j+1]!='#')
					ok=false;
				else if(a[i+1][j+1]!='#')
					ok=false;
				else
				{
					a[i][j] = '/' ;
					a[i][j+1] = '\\' ;
					a[i+1][j]='\\';
					a[i+1][j+1]='/';
				}
			}
			else if(a[i][j]=='#')
				ok=false;
		}
		if(ok)
		{
			for(int i=0; i<r; i++)
				cout << a[i] << endl;
		}
		else cout << "Impossible\n";
	}
	return 0;
}
