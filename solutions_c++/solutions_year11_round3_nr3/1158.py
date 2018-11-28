#include<iostream>
using namespace std;
int num[105];
int main()
{
     int n,t;
     long l,h;
     bool f;
     long ans;
    freopen("inp.txt","r",stdin);
    freopen("outp.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    { f=false;
      cin>>n>>l>>h;
     // cout<<l<<endl;
    //  cout<<h<<endl;
      for(int j=1;j<=n;j++)
      cin>>num[j];
      
      for(long j=l;j<=h;j++)
      {  long k;
         for(k=1;k<=n;k++)
         if((j%num[k]==0)||(num[k]%j==0)) continue;
         else break;
         
         if(k>n) {f=true; ans=j;break;}
      
      }

    
    cout<<"Case #"<<i<<": ";
    if(f) cout<<ans<<endl;
    else  cout<<"NO"<<endl;
    }
   // system("PAUSE");
    return 0;
    
}
