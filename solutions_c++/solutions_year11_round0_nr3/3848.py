#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int q=0;q<tc;q++)
{
int n;
cin>>n;
int a[n];
int ans[100000];
int ind=0;
for(int i=0;i<n;i++)
{
cin>>a[i];
}
for(int j=1;j<(pow(2,n)-1);j++)
{
int b[n],c[n];
int bi=0,ci=0;
for(int i=0;i<n;i++)
{
int v=pow(2,i);

if(!(j&v))
{//cout<<j<<" b "<<a[i]<<endl;
b[bi]=a[i];
bi++;
}
else
{//<<j<<" c "<<a[i]<<endl;
c[ci]=a[i];
ci++;
}
}
int bx=0,cx=0;
for(int e=0;e<bi;e++)
{
bx=bx^b[e];
}
for(int e=0;e<ci;e++)
{
cx=cx^c[e];
}
if(cx==bx)
{
int temp=0;
for(int r=0;r<ci;r++)
{
temp=temp+c[r];
}
ans[ind]=temp;
ind++;
}
}
if(ind==0)
cout<<"Case #"<<q+1<<": NO"<<endl;
else
{
int k=ans[0];
for(int h=1;h<ind;h++)
{
if(ans[h]>k)
k=ans[h];
}
cout<<"Case #"<<q+1<<": "<<k<<endl;
}
}
return 0;
}
