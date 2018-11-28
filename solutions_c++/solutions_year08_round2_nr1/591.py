#include<iostream>
#include<vector>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
using namespace std;
int check(double a,double b,double c,double d,double e,double f)
{
   double x,y,z;
   //x=sqrt((a-c)*(a-))

}
int main()
{
 int t,k=0;
  cin>>t;
  while(t--)
  {
    k++;
    long long n,i,j,a,b,c,d,x,y,m,ans=0,p;
    cin>>n>>a>>b>>c>>d>>x>>y>>m;
    double px[n+1],py[n+1],tx,ty;
    px[0]=x;
    py[0]=y;
    for(i=1;i<n;i++)
      {
      x= (a*x + b)%m;
      y = (c*y + d)%m;
      px[i]=x;
      py[i]=y;
      //cout<<px[i]<<" "<<py[i]<<" "<<endl;
      }
      for(i=0;i<n;i++)
      {
         for(j=i+1;j<n;j++)
         {
            if(i==j)
               continue;
            for(p=j+1;p<n;p++)
            {
             if(p==j || p==i)
               continue;
              // check(px[i],py[i],px[j],py[j],px[p],py[p]);
               tx=(px[i]+px[j]+px[p])/3;
               ty=(py[i]+py[j]+py[p])/3;
               if(tx==floor(tx) && ty==floor(ty))
                 ans++;
            }
         }
      }
               
  
  
  
  
  
  printf("Case #%d: %d\n",k,ans);
  }
}
