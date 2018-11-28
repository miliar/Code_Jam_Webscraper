#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
struct seg1
{
   double s,e,v,l;
   bool operator <(const seg1 & rhs) const
   {
	   return s<rhs.s;
   }
};
struct seg2
{
	double s,e,v,l;
	   bool operator <(const seg2 & rhs) const
   {
	   return v<rhs.v;
   }

};
seg2 s1[10000];
seg1 s2[10000];
int main()
{
   freopen("A_large.in","r",stdin);
   freopen("A_large.out","w",stdout);
   int n,tcase,cas,i,j;
   double x,s,e,w,sw,sr,tr,len;
   scanf("%d",&tcase);
   for(cas=1;cas<=tcase;cas++)
   {
	   scanf("%lf%lf%lf%lf%d",&x,&sw,&sr,&tr,&n);
	   len=0;
	   for(i=1;i<=n;i++)
	   {
		   scanf("%lf%lf%lf",&s1[i].s,&s1[i].e,&s1[i].v);
		   s1[i].l=s1[i].e-s1[i].s;
		   len+=s1[i].e-s1[i].s;
	   }
	   s1[0].l=x-len;
	   s1[0].v=0;
	   sort(s1,s1+n+1);
	   double ans=0;
	   for(i=0;i<=n;i++)
	   {
         double tt=s1[i].l/(s1[i].v+sr);
		 if (tt<=tr) {tr-=tt;ans+=tt;}
		 else
		 {
			 ans+=tr+(s1[i].l-(s1[i].v+sr)*tr)/(s1[i].v+sw);
			 tr=0;
		 }
	   }
	   printf("Case #%d: %.8lf\n",cas,ans);
   }
    
}