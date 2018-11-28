#include<iostream>
using namespace std;
int main()
{
    long long T,t;
    cin>>T;
    for(t=0;t<T;t++)
    {
         long long n,count=0,i,j;
         cin>>n;
         long long a[n],b[n];
         for(i=0;i<n;i++)
         {
               cin>>a[i]>>b[i];                
         }                
         for(i=1;i<n;i++)
         {
              for(j=0;j<i;j++)
              {
                   if(a[i]>a[j] && b[i]<b[j])
                          count++;                
                   if(a[i]<a[j] && b[i]>b[j])
                          count++;
              }                 
         }
         cout<<"Case #"<<(t+1)<<": "<<count<<endl;
    }
    return 0;
}
