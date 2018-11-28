#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define FIL(c,n) memset(c,n,sizeof(c))

struct Elem
{
    double v;
    double d;
}em[1010];

int cmp(Elem a,Elem b)
{
    return a.v<b.v;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ct=1;ct<=t;ct++)
    {
        int x,s,tim,r,n;
        scanf("%d%d%d%d%d",&x,&s,&r,&tim,&n);
        int w[1010];
        int last=x;
        for(int i=0;i<n;i++)
        {
            int b,e;
            scanf("%d%d%d",&b,&e,&w[i]);
            em[i].v=s+w[i];
            em[i].d=e-b;
            last-=(e-b);
        }
        em[n].d=last;
        em[n].v=s;
        int dv=r-s;
        sort(em,em+n+1,cmp);
        for(int i=0;i<n+1;i++)
        {
      //      cout << em[i].d << " "  << em[i].v << endl;
        }
        double ans=0;
        double rt=tim;
        for(int i=0;i<n+1;i++)
        {
            if(em[i].d/(em[i].v+dv)<=rt)
            {
                rt-=em[i].d/(em[i].v+dv);
                ans+=em[i].d/(em[i].v+dv);
            }
            else
            {
                ans+=(em[i].d-rt*(em[i].v+dv))/em[i].v+rt;
                rt=0;
            }
         //   cout << rt << " " << ans << endl;
        }
        printf("Case #%d: %.8lf\n",ct,ans);
    }
    return 0;
}

