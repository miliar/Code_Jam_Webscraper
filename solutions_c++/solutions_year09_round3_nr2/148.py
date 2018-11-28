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

int main()
{
    int dd, cas = 0;
    scanf("%d",&dd);    
    while(dd--)
    {
        int n;
        ll a=0,b=0,c=0,A=0,B=0,C=0;
        scanf("%d",&n);
        REP(i,n)
        {
            int x,y,z;
            scanf("%d %d %d",&x,&y,&z);
            A+=x;
            B+=y;
            C+=z;
            scanf("%d %d %d",&x,&y,&z);
            a+=x;
            b+=y;
            c+=z;
        }
        ll x = A*A + B*B + C*C;
        ll y = 2LL * (a*A + b*B + c*C);
        ll z = a*a + b*b + c*c;
        D xx=x,yy=y,zz=z;
        xx/=n; yy/=n; zz/=n;
        xx/=n; yy/=n; zz/=n;
        D d=0,t=0;
//        printf("%lld %lld %lld\n",x,y,z);
        if(z==0 || y==0 || ( (y>0) ^ (z<0) ))
            d = sqrt((D)xx);
        else
        {
                t = -yy;
                t /= 2;
                t /= zz;
                d = t*(t*zz+yy)+xx;
                if(d<1e-10) d = 0;
                d = sqrt(d);
        }
        printf("Case #%d: %.8lf %.8lf\n",++cas,d,t);
    }
    return 0;
}
