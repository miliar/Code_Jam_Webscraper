#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int a[1001];
int t,tc,i,n,x,s;

main()
{
   cin>>t;
   
   for(tc=1;tc<=t;++tc)
   {
      cin>>n;
      
      int min=10000000,s=0,x=0;
      
      for(i=0;i<n;++i)
      {   cin>>a[i];
          if(a[i]<min) min=a[i];
          x^=a[i];
          s+=a[i];
      }
      
      cout<<"Case #"<<tc<<": ";
      
      if(x) cout<<"NO\n";
      else cout<<s-min<<"\n";
      
      
   }
}
