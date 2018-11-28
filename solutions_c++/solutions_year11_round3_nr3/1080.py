#include<iostream>
#include<cstdio>

using namespace std;

main()
{
      int n,l,h,t,tc,i,j,ii;
      bool done;
      int a[101];
      
      cin>>t;
      
      for(tc=1;tc<=t;++tc)
      {
         cin>>n>>l>>h;
         
         for(i=0;i<n;++i) cin>>a[i];
         
         done=false;
         
         //cout<<l<<"  "<<h<<"\n";
         
         for(i=l;i<=h && !done;++i)
         {
             for(j=0;j<n;++j)
             {
                 if((a[j]%i) && (i%a[j]))
                 {   //ii=i;
                     break;
                     //cout<<"broke : "<<a[j]<<" "<<i<<"\n";
                 }
             }
             
             if(j==n) { ii=i; done=true;}
             
         }
         
         cout<<"Case #"<<tc<<": ";
         if(!done) cout<<"NO\n";
         else cout<<ii<<"\n";
         
      }
      
}
