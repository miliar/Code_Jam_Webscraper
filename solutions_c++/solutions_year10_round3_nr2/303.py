#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<string>
#include<set>
#include<algorithm>
using namespace std;

#define mm 30000
#define ll long long

int main()
{

freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
 int T,v=0;cin>>T;while(T--)
{
v++;
long l,p,c;
int cnt,cc,temp,count;
int cd,cdd,cddd;
printf("Case #%d: ",v);
scanf("%ld %ld %ld",&l,&p,&c);
cnt=0;
for(cd=0;cd<2;cd++);
while(l<p)
{l=l*c;
cnt++;
}
temp=1;
cc=0;
while(temp<cnt)
{cc++;
temp=temp*2;
}printf("%d\n",cc);










}
//while(1);
return 0;
}
