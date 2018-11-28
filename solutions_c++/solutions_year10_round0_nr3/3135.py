#include<iostream>
#include<deque>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
deque<int> a;
int t,r,k,n,i,j,l,p,u,y;
cin>>t;
for(y=1;y<=t;y++)
{
cin>>r>>k>>n;
a.clear();
l=0;
for(i=1;i<=n;i++)
{
cin>>p;
a.push_back(p);
}
while(r>0)
{
r--;
p=u=0;
while(p+a.front()<=k && u<a.size())
{
u++;
p+=a.front();
a.push_back(a.front());
a.pop_front();
}
l+=p;
}
cout<<"Case #"<<y<<": "<<l<<endl;
}
return 0;
}