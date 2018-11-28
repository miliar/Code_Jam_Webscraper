#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <string>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)))
#define Out(x) (cout << #x << " = " << x << endl)
#define  sqr(x) ((x) * (x))
#define eps  1e-8

const double pi = acos(-1.0);

const int INF = 0x7fffffff;

int n,m;
int main()
{
//        freopen("B-small-attempt1.in","r",stdin);
//        freopen("B-small-attempt1.out","w",stdout);

        freopen("B-large.in","r",stdin);
        freopen("B-large.out","w",stdout);

    int i,T,cases;
    cin>>T;
    double x,y,z,a,b,c;

   for(cases=1;cases<=T;cases++)
    {
        scanf("%d",&n);
        double X=0,Y=0,Z=0,VX=0,VY=0,VZ=0;
        for(i=1;i<=n;i++)
        {
           scanf("%lf%lf%lf%lf%lf%lf",&x,&y,&z,&a,&b,&c);
           X+=x;Y+=y;Z+=z,VX+=a,VY+=b,VZ+=c;
        }
        double Q,d;
        if((VX*VX+VY*VY+VZ*VZ)!=0)
                Q=-1.0*(VX*X+VY*Y+VZ*Z)/(VX*VX+VY*VY+VZ*VZ);
        else
                Q=0;
        if(Q<0)
                Q=0;

        d=sqr(X+VX*Q)+sqr(Y+VY*Q)+sqr(Z+VZ*Q);

        if(d<=eps)
                printf("Case #%d: 0.00000000 %.8lf\n",cases,Q);
        else
                printf("Case #%d: %.8lf %.8lf\n",cases,sqrt(d)/n,Q);
    }
    return 0;
}
