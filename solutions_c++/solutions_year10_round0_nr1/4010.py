#include<iostream>
using namespace std;
long long int a[33];
void printNO(long long int val ,long long int n ,int c)
{    int ans;
/*     while(n--)
     {
        ans=val%2;
        val=val/2;       
     }
     if(ans==0)
     cout<<"Case #"<<c<<": "<<"OFF"<<endl;
     else
     cout<<"Case #"<<c<<": "<<"ON"<<endl;
     return;
    */
    if(val != a[n]-1)
       cout<<"Case #"<<c<<": "<<"OFF"<<endl;
     else
     cout<<"Case #"<<c<<": "<<"ON"<<endl;
     return;
           
}
main()
{
      long long int i,t,N,K;
      cin>>t;
      a[0]=1;
      for(i=1;i<=31;i++)
      {
             a[i]=a[i-1]*2;           
      }
      int cnt=0;
      while(t--)
      {  cnt++;
         cin>>N>>K;
         long long int v = K%a[N];
         printNO(v,N,cnt);       
      }
}
