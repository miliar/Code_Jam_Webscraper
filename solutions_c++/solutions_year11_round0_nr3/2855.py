#include <cstdlib>
#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int t,n;
long ans;
int num[1005];
//bool flag;
int main(int argc, char *argv[])
{   freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {// flag=true;
      cin>>n;
      long s=0;
      for(int j=1;j<=n;j++)
       { cin>>num[j];
         s=s^num[j];
       }
      sort(num+1,num+n+1);
      
      ans=0;
      for(int j=2;j<=n;j++)
      ans+=num[j];
    
    if(!s)    
       printf("Case #%d: %ld\n",i,ans); 
    else   
       printf("Case #%d: NO\n",i); 
    }
   // ans=2^4^6;
  //  cout<<ans;
   // system("PAUSE");
    return EXIT_SUCCESS;
}
