#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

#define ll long long
#define MM  1000


int main()
{   int N,n,s,p,t,fix,sus,low,up,ans,C=1;
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
    scanf("%d",&N); while(N--)
{
scanf("%d%d%d",&n,&s,&p);
printf("Case #%d: ",C);
C++;
fix=0;
sus=0;
ans=0;
if(p==1)
{
for(int i=0;i<n;i++)
{
scanf("%d",&t);
if(t>0)
ans++;
}
printf("%d\n",ans);
}
else
{
up=3*p-2;
low=3*p-4;
for(int i=0;i<n;i++)
{
scanf("%d",&t);
if(t>=up)
ans++;
else if(t>=low)
sus++;
}
ans=ans+min(s,sus);
printf("%d\n",ans);

}
}
//system("pause");
return 0;
}
