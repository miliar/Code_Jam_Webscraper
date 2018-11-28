//Tomasz Kulczyński
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define COND 1
#define DB(x) { if(COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

#define inf (1<<30)

int t[105];
int w[105][105];

int main()
{
    int dd, cas=0;
    scanf("%d",&dd);    
    while(dd--)
    {
        int p,q;
        scanf("%d %d",&p,&q);
        REP(i,q) scanf("%d",&t[i]);
        t[q] = 0, t[q+1] = p+1;
        q+=2;
        sort(t,t+q);
        REP(i,q-1) w[i][i+1] = 0;
        FOR(d,2,q-1) REP(i,q-d) 
        {
            w[i][i+d] = inf;
            FOR(j,i+1,i+d-1) w[i][i+d] = min(w[i][i+d], w[i][j] + w[j][i+d]);
            w[i][i+d] += t[i+d] - t[i] - 2;
    //        printf("%d %d :: %d\n",i,i+d,w[i][i+d]);
        }
        printf("Case #%d: %d\n",++cas,w[0][q-1]);
    }
    return 0;
}
