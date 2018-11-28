#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,n,l1,l2,a[105],b1[105],b2[105],k1,k2,i,j,l,p,t1,t2,c1,c2;
char c;
cin>>t;
for(l=1;l<=t;l++)
{
cin>>n;
k1=k2=1;
for(i=1;i<=n;i++)
{
cin>>c;
a[i]=0;
if(c=='O')
{
a[i]=1;
cin>>b1[k1++];
}
else
{
cin>>b2[k2++];
}
}
i=l1=l2=t1=t2=1;
for(p=0;i<=n;p++)
{
c1=c2=1;
if(a[i]==1 && l1==b1[t1]) i++,t1++,c1=0;
else if(a[i]==0 && l2==b2[t2]) i++,t2++,c2=0;
if(l1<b1[t1] && c1) l1++;
else if(l1>b1[t1] && c1) l1--;
if(l2<b2[t2] && c2) l2++;
else if(l2>b2[t2] && c2) l2--;
//cout<<"Step #"<<p<<": "<<l1<<" "<<l2<<endl;
}
cout<<"Case #"<<l<<": "<<p<<endl;
}
return 0;
}