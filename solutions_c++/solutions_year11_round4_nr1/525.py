#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
struct data
{
       int l,r,v;
}a[1003];
bool cmp(const data &a,const data &b)
{
     return a.v<b.v;
}
int main()
{
     int i,j,k,n,m,cs,x,s,r,t,q=0;
     freopen("A-large.in","r",stdin);
     freopen("A.out","w",stdout);
     scanf("%d",&cs);
     while (cs--)
     {
         m=0;
         scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
         for (i=1;i<=n;i++)
         {
             scanf("%d%d%d",&a[i].l,&a[i].r,&a[i].v);
             m+=a[i].r-a[i].l;
         }
         sort(a+1,a+1+n,cmp);
         double T=t;
         double ans,rem;
         if ((x-m)>t*r)
         {
             ans=t;
             rem=x-m;
             rem-=ans*r;
             ans+=rem/s;
             rem=0;
         }
         else 
         {
             ans=(x-m);
             ans/=r;
             rem=t-ans;
         }
         for (i=1;i<=n;i++)
         {
             if (rem==0)
             {
                double tt=a[i].r-a[i].l;
                ans+=tt/(s+a[i].v);
             }
             else
             {
                if ((r+a[i].v)*rem>=a[i].r-a[i].l)
                {
                   double tt=a[i].r-a[i].l;
                   rem-=tt/(r+a[i].v);
                   ans+=tt/(r+a[i].v);
                }
                else
                {
                   double tt=a[i].r-a[i].l;
                   ans+=rem+(tt-rem*(a[i].v+r))/(a[i].v+s);
                   rem=0;
                }
             }
         }
         printf("Case #%d: %f\n",++q,ans);
    }
}
