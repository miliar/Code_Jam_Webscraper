#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

int dp[10007];
int d[10007], l[10007];
int n;

int main()
{
    freopen("C:\\GCJ\\A-large (1).in", "r", stdin);
    freopen("C:\\GCJ\\alarge.txt", "w", stdout);
    int T, nowCase = 0;
    cin >> T;
    while (T--)
    {
        cin >> n;
      //  cout << n << endl;
        int last;
        REP(i, n)
            scanf("%d%d", &d[i], &l[i]);
        cin >> last;

        CLEAR(dp);
        REP(i, 1)
        {
            if (l[i] >= d[i])
                dp[i] = min(d[i], l[i]);
        }
       // REP(i, n) cout << dp[i] << endl;

        int ans = 0;
        REP(i, n)
        {
            if (!dp[i]) continue;
            if (ans) break;
            if (d[i]+dp[i] >= last) ans = 1;
            for (int j = i+1; j < n; ++j)
            {
                if (dp[i] >= d[j] - d[i])
                    dp[j] = max(dp[j], min(dp[i], min(l[j], d[j]-d[i])));
            }
        }
        printf("Case #%d: ", ++nowCase);
        if (ans)
            printf("YES\n");
        else printf("NO\n");
    }
	return 0;
}
