#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
//#include <cmath>
#include <string>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())
#define sqr(x) ((x) * (x))
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000 * 1000 * 1000;
const int64 INF64 = (int64)1e18;

int n;
char a[100][100];
int p[100];
bool used[10];

bool ok()
{
	forn(i, n)
		forn(j, n)
			if (a[i][j] == '1' && j > p[i])
				return false;
    return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	forn(test, tests)
	{
		scanf("%d\n", &n);
        forn(i, n)
        {
        	forn(j, n)
        		scanf("%c", &a[i][j]);
        	scanf("\n");
        }

        int ans = 0;
        memset(p, 0, sizeof(p));
        forn(i, n)
        	forn(j, n)
        		if (a[i][j] == '1') p[i] = j;

        forn(i, n)
        {
        	int idx = i;
        	for (int j = i; j < n; ++j)
        	{
        		if (p[j] <= i)
        		{
        			idx = j;
        			break;
        		}
        	}

        	for (int j = idx - 1; j >= i; --j)
        	{
        		forn(k, n)
        			a[j + 1][k] = a[j][j];
        		p[j + 1] = p[j];
        	}
        	

        	ans += idx - i;
        }

       	printf("Case #%d: %d\n", test + 1, ans);	
	}	

	return 0;
}
