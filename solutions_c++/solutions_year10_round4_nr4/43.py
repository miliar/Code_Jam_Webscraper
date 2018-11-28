
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
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
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

D od(D x, D y, D a, D b)
{
    return sqrt((x-a)*(x-a)+(y-b)*(y-b));
}

D wyc(D x, D r, bool odwr = 0)
{
    D e = x/r;
    if(e>1) e=1;
    if(e<-1) e=-1;
    e = asin(e);
    if(odwr) e = M_PI - e;
    if(e < 0) e += M_PI;
    if(e > M_PI ) e-=M_PI;
    return e * r * r;
}

int x[5013],y[5013];

void test()
{
    int n,m;
    scanf("%d %d",&n,&m);
    REP(i,n) scanf("%d %d",&x[i],&y[i]);
    REP(i,m) 
    {
        int e,f;
        scanf("%d %d",&e,&f);
        D r[2],d;
        r[0] = od(x[0],y[0], e, f);
        r[1] = od(x[1],y[1], e, f);
        d = od(x[0],y[0],x[1],y[1]);
        if(d<1e-5 || r[0]<1e-5 || r[1]<1e-5) while(1);
        D p = (r[0]+r[1]+d)/2;
        D a = sqrt(p * (p-d) * (p-r[0]) * (p-r[1]));
        D xx = 2*a/d;
     //   printf("\n xx=%.3lf a=%.3lf r[0]=%.3lf r[1]=%.3lf d=%.3lf \n",xx,a,r[0],r[1],d);
            if(r[0] > r[1]) swap(r[0], r[1]);
            D u = sqrt(r[1] * r[1] -xx*xx);
        if( u > d)
        {
            printf(" %.8lf",(wyc(xx,r[0],1)+wyc(xx,r[1])) - a-a);
            continue;
        }
        printf(" %.8lf",(wyc(xx,r[0])+wyc(xx,r[1])) - a-a);
    }
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d:",cas);
        test();
        printf("\n");
    }
    return 0;
}
