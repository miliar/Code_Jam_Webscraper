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

string name[10000];
vector < int > g[10000];
string s;
int num = 1;
int ans;

void solve1()
{
	int v = 0;
	string ss;
	int i = 1;
	while (i<s.size())
	{
		ss.clear();
		while (i<s.size() && s[i]!='/')
		{
			ss.pb(s[i]);
			i++;
		}
		int k;
		int ok = -1;
		for (k=0; k<g[v].size(); k++)
			if (name[g[v][k]]==ss)
			{
				ok = g[v][k];
				break;
			}
		if (ok==-1)
		{
			name[num] = ss;
			g[v].pb(num);
			v = num;
			num++;
		}
		else
			v = ok;
		i++;
	}
}

void solve2()
{
	int v = 0;
	string ss;
	int i = 1;
	while (i<s.size())
	{
		ss.clear();
		while (i<s.size() && s[i]!='/')
		{
			ss.pb(s[i]);
			i++;
		}
		int k;
		int ok = -1;
		for (k=0; k<g[v].size(); k++)
			if (name[g[v][k]]==ss)
			{
				ok = g[v][k];
				break;
			}
		if (ok==-1)
		{
			ans++;
			name[num] = ss;
			g[v].pb(num);
			v = num;
			num++;
		}
		else
			v = ok;
		i++;
	}
}



int main()
{
	freopen("a_larg.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int n,m;
	int i,j,k;
	int T,t;

	cin >> T;
	for (t=1; t<=T; t++)
	{
		for (i=0; i<num; i++)
		{
			g[i].clear();
			name[i] = "";
		}
		num = 1;
		ans = 0;
		cin >> n >> m;
		for (i=0; i<n; i++)
		{
			cin >> s;
			solve1();
		}
		for (i=0; i<m; i++)
		{
			cin >> s;
			solve2();
		}
		printf("Case #%d: %d\n", t,ans);
	}

	return 0;
}