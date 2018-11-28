#include<iostream>
#include<math.h>
using namespace std;
int main()
 { unsigned long long a,x,y,m;int t,i,n,tn=1;cin>>t;
   while(t--)
    {cin>>n;m=10000000;x=0;y=0;
     for(i=0;i<n;i++){cin>>a;x+=a;y=y^a;if(a<m)m=a;}
     if(y!=0) cout<<"Case #"<<tn<<": NO"<<endl;
     else cout<<"Case #"<<tn<<": "<<x-m<<endl;
     tn++;
   }
    return 0;
 }
     
