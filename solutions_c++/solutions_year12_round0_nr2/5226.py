#include <iostream>
#include <cstdio>
 
using namespace std;
 
 
int main()
{
       freopen("B-small-attempt3.in","r",stdin);
       freopen("output.txt","w",stdout);
 
        int t;
cin>>t;
int N,S,P;
for(int i=0;i<t;i++)
{int a[100];
cin>>N>>S>>P;
for(int z=0;z<N;z++)
cin>>a[z];int ans=0;
for(int j =0;j<N;j++)
{
if(P<1)	
{ans=N;
break;}if(a[j]<1)
a[j]-=20;
else
a[j]-=P;
a[j]/=2;
if(P-a[j]<=1)
ans++;
else
if(P-a[j]<=2 && S>0)
{S--;ans++;}
}
cout<<"Case #"<<i+1<<": "<<ans<<endl; 
}
return 0;
};