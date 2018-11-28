#include<iostream>
#include <cstdio>
#include <string.h>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
struct data
{
       int num;
       int pos;
};
data c[200];
int n;
long long m;
bool cmp(const data &r, const data &s)
{
     return r.pos<s.pos;
 }
 long long lxabs(long long x) {return x>=0 ? x : -x;}
bool checkok(long long md)
{
     long long x = 1000000,g;
     x*=x;
     x*=(-1);
     for (int i=0;i<n;++i)
     if (c[i].num)
     {
  
         if (x < c[i].pos - md) x = c[i].pos - md;
         x = x + m * (c[i].num-1);
         if (lxabs(x-c[i].pos) > md) return false;
         x+=m;
     }
     return true;
 }
double work()
{
       sort(c,c+n,cmp);
       m*=2;
       long long st,en,mid;
       st=5;en=6;
       st = 0; en = 1000001;
       en *= en;
       while (st<en)
       {
             mid=(st+en)/2;
             if (checkok(mid)) en=mid;
             else st=mid+1;
       }
       return double(st)/2;
}
int main()
{
    int tc,cas;
    freopen("B-large.in","r",stdin);
    freopen("outputb_lr.txt","w",stdout);
    scanf("%d",&tc);
    for (cas=1;cas<=tc;++cas)
    {
        scanf("%d%lld",&n,&m);
        for (int i=0;i<n;++i) {scanf("%d%d",&c[i].pos, &c[i].num); c[i].pos*=2;}
        printf("Case #%d: %.2lf\n", cas, work());
    }
    return 0;
}
