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

#define M 50

int x[M],y[M],r[M];

double d(int i,int j)
{
    return sqrt((double)((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])));
}

int main()
{
    int dd,cas=0;
    scanf("%d",&dd);    
    while(dd--)
    {
        double ret = 1e100;
        int n;
        scanf("%d",&n);
        REP(i,n) scanf("%d %d %d",&x[i],&y[i],&r[i]);
        if(n==1) ret = r[0];
        else if(n==2) ret = max(r[0], r[1]);
        else
        {
            ret = min(ret, max((double)r[0], r[1]+r[2]+d(1,2))/2.);
            ret = min(ret, max((double)r[1], r[0]+r[2]+d(0,2))/2.);
            ret = min(ret, max((double)r[2], r[1]+r[0]+d(1,0))/2.);
        }
        printf("Case #%d: %.7lf\n",++cas,ret);
    }
    return 0;
}
