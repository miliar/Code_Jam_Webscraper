#include<iostream>
using namespace std;
int main()
{
    long long n,m,cnt1=1,cnt,a[10000],b[10000],i,j,k,t;
    cin>>t;
    for(i=0;i<t;i++)
    {
      cnt=0;
      cin>>n;
      for(j=0;j<n;j++) cin>>a[j]>>b[j];
      for(j=1;j<n;j++)
        for(k=0;k<n;k++)
        {
           if((a[j]>a[k] && b[j]<b[k]) || a[j]<a[k] && b[j]>b[k])
           {
             cnt++;
             break;
           }
        }
      cout<<"Case #"<<cnt1++<<": "<<cnt<<"\n";
    }
    return 0;
}
