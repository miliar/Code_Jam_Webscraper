#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <utility>
#include <iostream>
using namespace std;

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()

#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define wipen(a) memset((a), -1, sizeof(a))
#define wipez(a) memset((a), 0, sizeof(a))

#define pb push_back
#define quad(a) ((a)*(a))
#define sz(c) int((c).size())

const int INF = 0x3F3F3F3F, NEGINF = 0xC0C0C0C0;

int main()
{
	int t, nt;
	scanf("%d", &nt);
	for(t = 1; t <= nt; t++)
	{
		double ans = 100000;
		int n, px[5], py[5], r[5];
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d %d %d", &px[i], &py[i], &r[i]);
		if(n == 1)
			ans = r[0];
		if(n == 2) ans = max(r[0], r[1]);
		if(n == 3)
		{
			for(int i = 0; i < 3; i++)
			{
				for(int j = i+1; j < 3; j++)
				{
					double aa =
					(sqrt(quad(px[i]-px[j])+quad(py[i]-py[j]))+r[i]+r[j])/2;
					aa = max(max(aa, (double)r[0]), max((double)r[1], (double)r[2]));
					ans = min(ans, aa);
				}
			}
		}
		printf("Case #%d: %lf\n", t, ans);
	}
}
