#include <iostream>
#include <cmath>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second
#define kw(x) ((x)*(x))
using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
typedef double D;
typedef pair<D,D> pdd;

pdd add(pii a, pii b) { return pdd (a.x+b.x,a.y+b.y);}

const int M = 45;
int R [M];
pii P [M];

D dist(pdd a, pdd b) { return sqrt(kw(a.x-b.x)+kw(a.y-b.y)); }
D solve()
{
    int n;
    scanf("%d",&n);
    fru(i,n) scanf("%d %d %d",&P[i].x,&P[i].y,&R[i]);
    while(n<3) 
    {
        P[n]=P[n-1];
        R[n]=R[n-1];
        ++n;
    }
    D ret=10000000.0;
    fru(i,n) fru(j,n) if(i!=j)
    {
        pdd a=add(P[i],P[j]);
        D q=(dist(P[j],P[i])+R[i]+R[j])/2.0;
        q=max(q,1.0*R[3^i^j]);
        ret=min(ret,q);
    }
    return ret;
}

int main()
{
    int t;
    scanf("%d",&t);
    fru(i,t) printf("Case #%d: %.6lf\n",i+1,solve());

return 0;
}
