#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(ll i=0; i<n; i++)
#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define RFOR(i, x, y) for(ll i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define X first
#define Y second
#define VI vector<short>
const double pi=acos(-1.0);


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tests;
	cin>>tests;
	REP(test, tests)
	{
		int n, m;
		int a[100][100];
		REP(i, 60)
			REP(j, 60)
			a[i][j] = 0;

		string s;

		cin>>n>>m;
		
		REP(i, n)
		{
			cin>>s;
			REP(j, m)
				if (s[j] == '#')
					a[i][j] = 1;
				else a[i][j] = 0;
		}


		REP(i, n-1)
			REP(j, m-1)
			if (a[i][j]==1 && a[i+1][j]==1 && a[i+1][j+1]==1 && a[i][j+1]==1)
			{
				a[i][j] = 2;
				a[i][j+1] = 3;
				a[i+1][j] = 4;
				a[i+1][j+1] = 5;
			}

		bool ok = true;
		REP(i, n)
			REP(j, m)
			if (a[i][j] == 1)
				ok = false;

		printf("Case #%d:\n", test+1);

		if (!ok)
			printf("Impossible\n");
		else
		{
			REP(i, n)
			{
				REP(j, m)
				{
					if (a[i][j] == 0) cout<<".";
					if (a[i][j] == 2) cout<<"/";
					if (a[i][j] == 3) cout<<"\\";
					if (a[i][j] == 4) cout<<"\\";
					if (a[i][j] == 5) cout<<"/";
				}
				cout<<endl;
			}
		}


	}

}

