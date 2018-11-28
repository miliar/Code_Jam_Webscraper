#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;
#define MAXN 100

int  a[MAXN], p[MAXN];
char s[MAXN];
LL   ans, r;
int n, k;
int main()
{
    int tc;
	//freopen("d.in", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
		scanf("%s", s);
		n = strlen(s);
		k = 0;
		for(int i=0; i<n; ++i)if (s[i] == '?') p[k++] = i; else a[i] = s[i] - '0';

		for(int v=0; v< (1<<k); ++v)
		{
			int j = v;
			for(int i=0; i<k; ++i) a[ p[i] ] = j & 1, j = j >> 1;
			ans = 0;
			for(int i=0; i<n; ++i) ans = ans * 2 + a[i];
			r = sqrt( (double)ans );
			if ( (r - 1)*(r - 1) == ans ||
				 (r + 1)*(r + 1) == ans ||
				 r*r == ans)
			{
				break;
			}
		}
        printf("Case #%i: ", tt);
		for(int i=0; i<n; ++i) printf("%i", a[i]);
		printf("\n");
    }
}