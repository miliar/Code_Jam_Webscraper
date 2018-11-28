#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
main()
{
 vector<int> a;
 int i,j,l,p,k,s,m,n,q,r,t,count,x,y,z;
 cin>>t;
r=0;
while(t--)
{
r++;
 cin>>p>>k>>l;
a.clear();
count=0;x=1;y=1;z=1;
 for(i=0;i<l;i++)
 { 
   cin>>j;
 //  a.push_back(empty);
   a.push_back(j);    
 }
sort(a.begin(),a.end());
s=a.size();
s--;
while(s>=0)
{
  if(x>k)
  {x=1;y++;}
  count=count+a[s]*y;
   x++;
   s--;
  
}
cout<<"Case #"<<r<<": "<<count<<endl;
}
}
