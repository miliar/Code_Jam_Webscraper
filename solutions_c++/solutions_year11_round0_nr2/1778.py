#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int inf = 2000 * 1000 * 1000;
const lint linf = 2000000000000000000LL;
const double eps = 1e-9;

void prepare( )
{
#ifdef WIN32
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int n;
map < pair < char , char > , char > com;
vector < char > Dec[1 << 8];
int used[1 << 8];
string s,t,go;
vector < char > ans;

bool solve( )
{
	ans.clear();
	com.clear();
	for ( int i = 'A'; i <= 'Z'; i ++ )
	{
		used[i] = 0;
		Dec[i].clear();
	}

	int k;
	cin >> k;
	for ( int i = 0; i < k; i ++ )
	{
		cin >> s;
		com.insert(mp( mp(s[0],s[1]), s[2] ));
		com.insert(mp( mp(s[1],s[0]), s[2] ));
	}
	cin >> k;
	for ( int i = 0; i < k; i ++ )
	{
		cin >> s;
		Dec[s[0]].pb(s[1]);
		Dec[s[1]].pb(s[0]);
	}
	cin >> n;
	cin >> go;

	for ( int i = 0; i < n; i ++ )
	{
		if ( sz(ans) == 0 )
		{
			ans.pb(go[i]);
			used[go[i]]++;
		}
		else
		if ( com.find(mp(go[i],ans.back())) != com.end() )
		{
			char t = com.find(mp(go[i],ans.back()))->second;
			used[ans.back()]--;
			ans.pop_back();
			used[t]++;
			ans.pb(t);
		}
		else
		{
			bool ok = true;
			for ( int j = 0; j < sz(Dec[go[i]]); j ++ )
			{
				if (used[Dec[go[i]][j]])
				{
					for ( int k = 'A'; k <= 'Z'; k ++ )
						used[k] = 0;
					ans.clear();
					ok = false;
					break;
				}
			}
			if ( ok )
			{
				used[go[i]]++;
				ans.pb(go[i]);
			}
		}
	}
	
	printf("[");
	for ( int i = 0; i < sz(ans); i ++ )
	{
		if (i) printf(", ");
		printf("%c",ans[i]);
	}
	printf("]\n");

	return false;
}

int main()
{
	prepare( );
	int t;
	cin >> t;
	for ( int i = 0; i < t; i ++ )
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}