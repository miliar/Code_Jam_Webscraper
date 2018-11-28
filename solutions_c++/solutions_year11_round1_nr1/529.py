#include<iostream>
using namespace std;
int nod(int x,int y)
{
if(x<y) swap(x,y);
while(y)
{
x%=y;
swap(x,y);
}
return x;
}
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
long long t,t2,n,i,p1,p2,nd;
cin>>t;
for(t2=1;t2<=t;t2++)
{
cin>>n>>p1>>p2;
nd=nod(p1,100);
cout<<"Case #"<<t2<<": ";
if(100/nd>n || p2==100 && p1!=100 || p2==0 && p1!=0) cout<<"Broken";
else cout<<"Possible";
cout<<endl;
}
return 0;
}