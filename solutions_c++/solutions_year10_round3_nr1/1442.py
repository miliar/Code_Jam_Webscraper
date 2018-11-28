#include<iostream>
#include<set>
#include<vector>
using namespace std;
int main()
{
long t,cno=0;
cin>>t;
while(t--)
{
int totcon;
cin>>totcon;
int a[totcon],b[totcon];
for(int i=0;i<totcon;i++)
{cin>>a[i];cin>>b[i];}
int inters=0;
for(int i=0;i<totcon;i++)
for(int j=0;i<totcon;i++)
{
if(i!=j)
{
if(a[i]>a[j]&&b[i]<b[j]||a[i]<a[j]&&b[i]>b[j]) inters++;
}
}
cout<<"Case #"<<++cno<<": "<<inters<<endl;
}
return 0;
}