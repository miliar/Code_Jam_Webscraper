#include <cstdlib>
#include<stdio.h>
#include <iostream>
#include<algorithm>
#define inf 100000000
using namespace std;
int main(int argc, char *argv[])
{
    freopen("C-large.in","r",stdin);
   freopen("out_large.txt","w",stdout);
 //   cout<<(9865^2940^9645^5285^5545)<<endl;
    int cas,i,j,t;
    t=0;
    int n;
    int c[1005];
    int temp=i;
    int sum=0;
    int val1=0,val2=0;
    scanf("%d",&cas);
    int a;
    int ans,tot;
    while(cas--)
    {
      t++;
      scanf("%d",&n);
      memset(c,0,sizeof(c));
      a=0;
      tot=0;
      for (i=0;i<n;i++)
      {
          scanf("%d",&c[i]);
          a=a^c[i];
          tot+=c[i];
      }
     if (a!=0) {
        printf("Case #%d: NO\n",t);
        continue;
      }
   //   cout<<a<<endl;
      ans=0;
      val1=val2=0;
      sort(c,c+n);
      bool flag=false;
      for (i=0;i<n;i++)
      {
        val1=val1^c[i];
        ans+=c[i];
        val2=0;
        for (j=i+1;j<n;j++)
        {
          val2=val2^c[j];
        }
     //   cout<<val1<<" "<<val2<<endl;
       if (val1==val2&&!flag) {
         printf("Case #%d: %d\n",t,tot-ans);
         flag=true;
       }
      }
      if (!flag)  printf("Case #%d: NO\n",t);
   /*
      for (i=1;i<=((1<<n)-2);i++)
      {
        temp=i;
        sum=0;
        val1=val2=0;
        j=0;
     //    cout<<"# "<<temp<<endl;
       while(j<n)
       {      
          if (temp&1) 
          {
            sum+=c[j];
            val1=val1^c[j];
          }
          else val2=val2^c[j];
          temp=temp>>1;
          j++;
       }
    //   cout<<sum<<" "<<val1<<" "<<val2<<endl;        
       if (sum>ans&&val1==val2) ans=sum;
      }
      if (ans==0) printf("Case #%d: NO\n",t);
      else printf("Case #%d: %d\n",t,ans);*/
    }
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
