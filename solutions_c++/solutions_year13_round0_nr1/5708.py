//Solution by Miras Myrzakerey
//Look at my code
//My code is amazing

#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <ctime>
#include <queue>
#include <iomanip>

using namespace std;

#define INF 1000000001
#define sqr(x) (x) * (x)
#define maxn 200001
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define all(a) a.begin(),a.end()
#define len(a) (int)(a.length())
#define F first
#define S second
#define pii pair<int,int>
#define LL long long
#define vi vector<int>
#define forn(xx,yy,zz) for(int zz = xx; zz <= yy; ++zz)
#define forl(xx,yy,zz) for(int zz = xx; zz >= yy; --zz)
#define str string
#define eps 1e-7
#define pi M_PI

int t;
string s[4];

int main()
{
	freopen ("out", "w", stdout);
	freopen ("in", "r", stdin);

	scanf ("%d", &t);

	for (int it = 1; it <= t; ++it)
	{
	    int ans = 0;
		int cntx = 0, cnt0 = 0, ok = 0;
		
		cin >> s[0] >> s[1] >> s[2] >> s[3];

		for (int i = 0; i < 4; ++i)
		{
			cntx = 0, cnt0 = ok = 0;
			for (int j = 0; j < 4; ++j)	
				if (s[i][j] == 'X')
					cntx++;
				else
					if (s[i][j] == 'O')
						cnt0++;
					else
						if (s[i][j] == 'T')
							ok = 1;

			if (cntx == 4 || (cntx == 3 && ok))
			{
				ans = 1;
				break;
			}

			if (cnt0 == 4 || (cnt0 == 3 && ok))
			{
				ans = 2;
				break;
			}
		}

		if (ans)
		{
			printf ("Case #%d: %c won\n", it, ans == 1 ? 'X' : 'O');
			continue;
		}

		for (int i = 0; i < 4; ++i)
		{
			cntx = 0, cnt0 = ok = 0;
			for (int j = 0; j < 4; ++j)	
				if (s[j][i] == 'X')
					cntx++;
				else
					if (s[j][i] == 'O')
						cnt0++;
					else
						if (s[i][j] == 'T')
							ok = 1;

			if (cntx == 4 || (cntx == 3 && ok))
			{
				ans = 1;
				break;
			}

			if (cnt0 == 4 || (cnt0 == 3 && ok))
			{
				ans = 2;
				break;
			}
		}

		if (ans)
		{
			printf ("Case #%d: %c won\n", it, ans == 1 ? 'X' : 'O');
			continue;
		}

		cntx = cnt0 = ok = 0;

		for (int i = 0; i < 4; ++i)
		{
			if (s[i][i] == 'X')
				cntx++;
			else
				if (s[i][i] == 'O')
					cnt0++;
				else
					if (s[i][i] == 'T')
						ok = 1;				
		}

		if (cntx == 4 || (cntx == 3 && ok))
			ans = 1;

		if (cnt0 == 4 || (cnt0 == 3 && ok))
			ans = 2;

		if (ans)
		{
			printf ("Case #%d: %c won\n", it, ans == 1 ? 'X' : 'O');
			continue;
		}

		cntx = cnt0 = ok = 0;

		for (int i = 0; i < 4; ++i)
		{
			if (s[i][3 - i] == 'X')
				cntx++;
			else
				if (s[i][3 - i] == 'O')
					cnt0++;
				else
					if (s[i][3 - i] == 'T')
						ok = 1;
		}

		if (cntx == 4 || (cntx == 3 && ok))
			ans = 1;

		if (cnt0 == 4 || (cnt0 == 3 && ok))
			ans = 2;

		if (ans)
		{
			printf ("Case #%d: %c won\n", it, ans == 1 ? 'X' : 'O');
			continue;
		}

		for (int i = 0; i < 4 && !ans; ++i)
			for (int j = 0; j < 4; ++j)
				if (s[i][j] == '.')
				{
					ans = 1;
					break;
				}

		if (ans)
			printf ("Case #%d: Game has not completed\n", it);
		else
			printf ("Case #%d: Draw\n", it);
	}
}