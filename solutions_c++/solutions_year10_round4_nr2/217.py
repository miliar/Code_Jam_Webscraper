#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,c) for(__typeof((c).begin()) i =(c).begin();i!=(c).end();++i)
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int NIL = (-1);

const int P = 11;
const int N = 1<<10;
const long long INF = 2000LL*1000000LL;

int p,n;
long long dp[2*N][P];
int M[N];
long long cost[N];

void scase() {
    scanf("%d",&p);
    n = 1<<p;
    for(int i=n-1;i>=0;i--) scanf("%d",&M[i]);
    for(int i=n-1;i>0;i--) scanf("%lld",&cost[i]);
    
    for(int i=0;i<n;i++) 
        for(int k=0;k<=p;k++)
            if (M[i]>=p-k)
                dp[n+i][k] = 0;
            else {
                //printf("M[%d] = %d, p-k = %d, first one is less\tp=%d,k=%d\n",i,M[i],p-k,p,k);
                dp[n+i][k] = INF;
            }
    for(int i=n-1;i>0;i--)
        for(int k=0;k<=p;k++) {
            dp[i][k] = min(
                    dp[2*i][k]+dp[2*i+1][k],
                    dp[2*i][k+1]+dp[2*i+1][k+1]+cost[i]
            );
        }
//    printf("%d\n",M[0]);
//    printf("%lld\n",dp[n][p]);
    printf("%lld\n",dp[1][0]);
}

int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        printf("Case #%d: ",i);
        scase();
    }
    return 0;
}

