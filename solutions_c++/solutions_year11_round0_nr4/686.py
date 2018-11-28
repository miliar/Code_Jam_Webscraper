#include<iostream>
using namespace std;
int main()
{
 freopen("D-large.in","r",stdin);
 freopen("D-large.out","w",stdout);
 double s;
 int i,t,n,a,m=0;
 scanf("%d",&t);
 while(t--)
      {
       s=0;
       scanf("%d",&n);
       for(i=1;i<=n;i++)
          {
           scanf("%d",&a);
           if(a!=i) s++;
          }
       printf("Case #%d: %.6lf\n",++m,s);
      }
 return 0;
}
