#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t;
	s(t);
	int k = 0;
	while(t--)
	{
		k++;
		int r, c; s(r); s(c);
		char g[100][100];
		int i, j;
		rep(i,r) rep(j,c) cin>>g[i][j];
		rep(i,r)
		{
			rep(j,c)
			{
				if(g[i][j] == '#')
				{
					if(i+1 < r && j+1 < c)
						if(g[i+1][j]=='#' && g[i][j+1]=='#' && g[i+1][j+1]=='#')
						{
							g[i][j] = '/'; g[i][j+1] = '\\';
							g[i+1][j] = '\\'; g[i+1][j+1] = '/';
						}
				}
			}
		}
		bool done=true;
		rep(i,r) rep(j,c) if(g[i][j]=='#') done=0;
		cout << "Case #" << k << ":" << endl;
		if(!done) cout << "Impossible" << endl;
		else
		{
			rep(i,r)
			{
				rep(j,c)
					cout << g[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}
