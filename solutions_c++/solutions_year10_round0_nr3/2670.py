#include<iostream>
#include<queue>
using namespace std;
int main()
{

int t,r,k,n,l,g[11],cas=1,sum,j,tmp,i,no,count,h[11],b;
cin>>t;
while(t--)
{
queue<int> q;
cin>>r>>k>>n;
tmp=0;
for(i=0;i<n;i++)
{
cin>>g[i];
q.push(g[i]);
tmp=tmp+g[i];
}
if(tmp<=k)
sum=r*tmp;
else
{
sum=0;
while(r--)
{
no=0;b=0;
while(no<=k || !(q.empty()))
{
tmp=q.front();
no=no+tmp;
if(no>k || q.empty()) break;
else { sum=sum+tmp; q.pop(); h[b++]=tmp;}
}
for(l=0;l<b;l++) {q.push(h[l]); }
}
}
cout<<"Case #"<<cas++<<": "<<sum<<endl;
}
return 0;
}

