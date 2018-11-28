#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;

#define NMAX 2005

int n, m;
int mault[NMAX];
bool unm[NMAX][NMAX];
int deg[NMAX];
bool used[NMAX];
int ans[NMAX];

void solve(int test)
{
    scanf("%d %d", &n, &m);
    forn(i, m)
    {
    	forn(j, n)
    	{
    		unm[i][j] = false;
    	}
    }
    forn(i, m)
    {
    	mault[i] = -1;
    	used[i] = false;
    	deg[i] = 0;
    }
    forn(i, n) ans[i] = 0;

    int k, num, ty;
    forn(i, m)
    {
    	scanf("%d", &k);
    		
    	forn(j, k)
    	{
    		scanf("%d %d", &num, &ty);
    		--num;
	    	if (ty == 1)
    		{
    			mault[i] = num;
	    	}
	    	else
	    	{
	    		unm[i][num] = true;
	    		deg[i]++;
	    	}  	
    	}
    }

    bool impos = false;
    queue<int> q;
    forn(i, m)
    {
    	if (used[i]) continue;
    	if (deg[i] == 0)
    	{
    		if (mault[i] == -1)
    		{
    			impos = true;
    			break;
    		}
    		q.push(mault[i]);
    		forn(j, m)
    		{
    			if (mault[j] == mault[i])
    			{
    				used[j] = true;
    			}
    		}
    	}
    }

	while (!q.empty())
	{
		int u = q.front(); q.pop();
		ans[u] = 1;
		forn(i, m)
		{
			if (used[i]) continue;
			if (unm[i][u])
			{
				unm[i][u] = false;
				deg[i]--;
				if (deg[i] == 0)
				{
					if (mault[i] == -1)
					{
						impos = true;
						break;
					}
					q.push(mault[i]);
					
					forn(l, m)
					{
						if (mault[l] == mault[i])
						{
							used[l] = true;
						}						
					}
				}
			}
		}
		if (impos) break;
	}

	if (impos)
	{		
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}
	printf("Case #%d:", test);
	forn(i, n)
	{
		printf(" %d", ans[i]);		
	}
	printf("\n");
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
