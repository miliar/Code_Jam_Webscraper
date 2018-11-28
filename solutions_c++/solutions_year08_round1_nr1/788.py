#include<iostream>
#include<algorithm>
using namespace std;
main()
{
int n,t,i,j,k,a[900],b[900];
long int prod=0;
cin>>t;
for(i=0;i<t;i++)
{
prod=0;
cin>>n;
for(j=0;j<n;j++)
cin>>a[j];
for(j=0;j<n;j++)
cin>>b[j];
sort(a,a+n);
sort(b,b+n);
for(j=0;j<n;j++)
prod+=a[j]*b[n-j-1];
cout<<"Case #"<<(i+1)<<": "<<prod<<endl;
}
}
