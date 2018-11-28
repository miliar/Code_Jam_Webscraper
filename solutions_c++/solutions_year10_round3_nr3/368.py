#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <stdio.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define _(a,b) memset((a),b,sizeof(a))
#define sz(a) (int)size()

typedef unsigned long long ull;
typedef long long lint;

const int EPS = 1e-9;;
const int INF = 1000 * 1000 * 1000;

int m,n,t,T;
bool a[512][512];
bool used[512][512];
string s;
vector < int > ans;
vector < pair < int , int > > pr;

bool check(int x,int y, int r)
{
	int i,j;
	for (i=x; i<x+r; i++)
		for (j=y; j<y+r; j++)
			if (used[i][j])
				return false;
	for (i=0; i<r-1; i++)
	if (a[x+r-1][y+i]==a[x+r-2][y+i] || a[x+i][y+r-1]==a[x+i][y+r-2])
		return false;
	if (a[x+r-1][y+r-1]!=a[x+r-2][y+r-2] ||
		a[x+r-1][y+r-1]==a[x+r-1][y+r-2] ||
		a[x+r-1][y+r-1]==a[x+r-2][y+r-1])
		return false;
	return true;
}

int solve(int x, int y)
{
	int r = 1;

	while (y+r<m && x+r<n && check(x,y,r+1))
		r++;
	return r;
}

int main()
{
	freopen("c_sm.in","r", stdin);
	freopen("c_sm.out", "w", stdout);

	int i,j,k;
	cin >> T;
	for (t=1; t<=T; t++)
	{
		cin >> m >> n;
		for (i=0; i<m; i++)
		{
			cin >> s;
			for (j=0; j<n/4; j++)
			{
				int x;
				if (s[j]<='9' && s[j]>='0') x = s[j] - '0';
				else x = s[j] - 'A' + 10;
				for (k=0; k<4; k++)
					a[j*4+k][i] = (1 << (3 - k)) & x;
			}
		}

		ans.clear();
		_(used,false);
		int sz;
		for (sz = min(n,m); sz>=1; sz--)
		{
			for (i=0; i<m; i++)
				for (j=0; j<n; j++)
					if (!used[j][i] && solve(j,i)==sz)
					{
						ans.pb(solve(j,i));
						int x,y;
						for (x=j;x<j+sz;x++)
							for (y=i;y<i+sz;y++)
								used[x][y] = true;
					}
		}

		sort(all(ans));
		pr.clear();
		int last = -1;
		i = ans.size() - 1;
		k = 0;
		while (i >= 0)
		{
			int old = i;
			last = ans[i];
			while (i>=0 && ans[i]==last) i--;
			k++;
			pr.pb(mp(last,old-i));
		} 
		printf("Case #%d: %d\n",t,k);
		for (i=0; i<pr.size(); i++)
			cout << pr[i].first << " " << pr[i].second << endl;
	}

	return 0;
}