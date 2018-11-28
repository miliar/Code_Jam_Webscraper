#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, b) FOR(i, 0, (b))
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))
#define X first
#define Y second

typedef long long ll;

int dif(int x, int p)
{
	if (x > 0)
		return x;
	else
		return x + p;
}

int e[1000000];

int main()
{
	e[0] = 1, e[1] = 1;
	int ee = 0;
	FOR(i, 2, 1000000)
		if (!e[i])
		{
			for (int j = 2; j * i < 1000000; j++)
				e[i * j] = 1;
			ee++;
		}
    int t;
    scanf("%d", &t);
    REP(ii, t)
    {
        int d, k;
        scanf("%d%d", &d, &k);
        vector <int> a;
        int mmn = 0;
        REP(i, k)
			a.pb(0), scanf("%d", &a.back()), mmn = max(mmn, a.back());
		if (k == 1)
		{
			printf("Case #%d: I don't know.\n", ii + 1);
			continue;
		}
		if (k == 2)
		{
			if (a[0] != a[1])
				printf("Case #%d: I don't know.\n", ii + 1);
			else
				printf("Case #%d: %d\n", ii + 1, a[0]);
			continue;
		}
        int rt = -1;
        int mx = pow(10, d);
        FOR(i, mmn + 1, mx)
			if (!e[i])
			{
				REP(j, i)
				{
					int dif = ((ll)a[1] - (ll)a[0] * (ll)j % (ll)i + (ll)i) % (ll)i;
					bool q = 1;
					FOR(t, 1, k)
						if (((ll)a[t - 1] * (ll)j + (ll)dif) % (ll)i != a[t])
						{
							q = 0;
							break;
						}
					if (q)
					{
						if (rt == -1)
							rt = ((ll)a[k - 1] * (ll)j + (ll)dif) % i;
						else if (rt != ((ll)a[k - 1] * (ll)j + (ll)dif) % i)
						{
							printf("Case #%d: I don't know.\n", ii + 1);
							goto wtf;
						}
					}
				}
			}
		printf("Case #%d: %d\n", ii + 1, rt);
		wtf:;
	}
}
/*
c1 = A * s - s2
c2 = A * s2 - s3
(c + B) % P = s2 => (c1 + B) % P = 0
(c + B) % P = s3 => (c2 + B) % P = 0

(c1 + B - c2 - B) % P = 0
|(c1 - c2)| % P = 0
|(A * s - s2 - A * s2 - s3)| % P = 0
|A * (s - s2) - s2 - s3| % P = 0
|C1| % P = 0
|C2| % P = 0
|C3| % P = 0
..
|CK| % P = 0
|C| % P = 0

(A * s + B) % p = s2
(A * s2 + B) % p = s3
(A^2 + A * s + A * B + B) % p = s3
*/
