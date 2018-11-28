#include<iostream>
using namespace std;
int main()
{
   int t,c1=0;
   cin>>t;
   while(t--)
   {
      int n,i,j,a[10005],b[10005];
      long long sum=0;
      c1++;
      cin>>n;
      for(i=0;i<n;i++)
        cin>>a[i]>>b[i];
      for(i=0;i<n-1;i++)
        for(j=i+1;j<n;j++)
           {
              if(a[i]-b[i]==a[j]-b[j]) continue;
              if(a[i]>=a[j] && b[i]>=b[j]) continue;
              if(a[i]<=a[j] && b[i]<=b[j]) continue;
              sum++;
           }
      cout<<"Case #"<<c1<<": "<<sum<<endl;
   //   return 0;
   }
    return 0;
}        
