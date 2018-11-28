#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
using namespace std;
typedef long long int int64;
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int i,j,n,k,m,t,cnt=1,s,p,a[100],wis,wos,ns,ans;
cin>>t;
while(t--)
{
scanf("%d %d %d",&n,&s,&p);
for(i=0;i<n;i++)scanf("%d",&a[i]);
wos = (3*p)-2;
wis = (3*p)-4;
if(p==0){wos = 0;wis = 0;}
else if(p==1){wos = 1;wis = 1;}
ans = ns = 0;
for(i=0;i<n;i++)
  {
  if(a[i]>=wos)ans++;
  else if(a[i]>=wis&&ns<s){ns++;ans++;} 
  }
printf("Case #%d: %d\n",cnt,ans);
cnt++;
}
return 0;
}
