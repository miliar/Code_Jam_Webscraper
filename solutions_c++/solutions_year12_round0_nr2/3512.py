#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <sstream>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

#define REP(i,n)      FOR(i,0,n)
#define FOR(i,a,b)    for(int i = a; i < b; i++)
#define ROF(i,a,b)    for(int i=a;i>b;i--)
#define min(a,b)      (a<b?a:b)
#define max(a,b)      (a>b?a:b)
#define GI 		      ({int t;scanf("%d",&t);t;})
#define GL 		      ({LL t;scanf("%lld",&t);t;})
#define GD 		      ({double t;scanf("%lf",&t);t;})
#define pb 	          push_back
#define mp 	          make_pair
#define fii 	      freopen("input.txt","r",stdin)
#define fio 	      freopen("output.txt","w",stdout)
#define MOD 	      1000000007
#define INF	          (int)1e9
#define EPS	          1e-9
#define TR(a,it)      for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

int NotSurprising(int sum)
{
    int maxi = 0;
    for (int i=0; i<=sum && i<=10; i++)
        for (int j=i; j<=i+1 && j<=sum && j<=10; j++) {
            int k = sum - i - j;
            if (k >= 0 && abs(i - k) <= 1 && abs(j - k) <= 1)
                maxi = max(maxi, max(max(i, j), k));
        }
    return maxi;
}

int Surprising(int sum)
{
    int maxi = 0;
    for (int i=0; i<=sum && i<=10; i++)
        for (int j=i; j<=i+2 && j<=sum && j<=10; j++) {
            int k = sum - i - j;
            if (k >= 0 && abs(i - k) <= 2 && abs(j - k) <= 2)
                maxi = max(maxi, max(max(i, j), k));
        }
    return maxi;
}

int main()
{
	fii; fio;
	int T, t = 0, n, s, p, sum[105];
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d", &n, &s, &p);
		FOR(i, 0, n)    scanf("%d", &sum[i]);

		int cnt = 0;
		for (int i=0; i<n; i++) {
            int maxScore = NotSurprising(sum[i]);
            if (maxScore >= p)
                cnt++;
            else if (s) {
                maxScore = Surprising(sum[i]);
                if (maxScore >= p)
                    cnt++, s--;
            }
		}

		printf("Case #%d: %d\n", ++t, cnt);
	}

	fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
	return 0;
}
