#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<string> vstr;
typedef pair<int, int> pint;

#define TWO(k)  (1<<k)
#define TWOL(k) (((LL)(1)<<(k)))
#define MP make_pair
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int oo = 210000000;

int main()
{
    //freopen("A-small-attempt1.in.txt","r",stdin);freopen("out.txt","w",stdout);
    int t, test = 0;
    scanf("%d", &t);
    while(t--)
    {
        int n; scanf("%d", &n);
        int dp[110] = {0};
        int op[110], bp[110];
        int op1[110], bp1[110];
        char tmp[3], pre[110];
        int k;
        op[0] = bp[0] = 1;
        op1[0] = bp1[0] = 0;
        for(int i = 1; i <= n; i++)
        {
            scanf("%s %d", tmp, &k);
            if(tmp[0] == 'O')
            {
                int t1 = abs(k - op[i-1]);
                int t2 = abs(dp[i-1] - dp[op1[i-1]]);
                    if( t1 <= t2)
                    {
                        dp[i] = dp[i-1] + 1;
                    }
                    else
                    {
                        dp[i] = dp[i-1] + 1 + t1 - t2;
                    }
                op[i] = k;
                op1[i] = i;
                bp[i] = bp[i-1];
                bp1[i] = bp1[i-1];              
            }
            if(tmp[0] == 'B')
            {
                int t1 = abs(k - bp[i-1]);
                int t2 = abs(dp[i-1] - dp[bp1[i-1]]);
                    if( t1 <= t2)
                    {
                        dp[i] = dp[i-1] + 1;
                    }
                    else
                    {
                        dp[i] = dp[i-1] + 1 + t1 - t2;
                    }
                bp[i] = k;
                bp1[i] = i;
                op[i] = op[i-1];
                op1[i] = op1[i-1];
            }
        }
        printf("Case #%d: %d\n", ++test, dp[n]);
    }                          
    return(0);
}
