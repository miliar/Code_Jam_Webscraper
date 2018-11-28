#include<iostream>
using namespace std;
int main()
{
    int temp=1;
int t,n;
int a[10005],b[10005];
cin>>t;
while(t--)
{
cin>>n;
int i,j;
j=n;
i=0;
while(n--)
{
cin>>a[i]>>b[i];
i++;
}
int count=0;
for(i=0;i<j;i++)
{
    for(int k=i+1;k<j;k++)
    {
     if(a[k]<a[i] && b[k]>b[i])
     count++;
     else if(a[k]>a[i] && b[k]<b[i])
     count++;
     else
     continue;
    }
}
cout<<"Case #"<<temp<<": "<<count<<endl;
temp++;
}
return 0;
}
