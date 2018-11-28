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
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
 int T,vv=0;cin>>T;while(T--)
{vv++;
long long l,p,c;
long long cnt,cc,temp,count;
printf("Case #%d: ",vv);
scanf("%lld %lld %lld",&l,&p,&c);
cnt=0;

while(l<p)
{l=l*c;
cnt++;
}
temp=1;
cc=0;
while(temp<cnt)
{cc++;
temp=temp*2;
}printf("%lld\n",cc);










}
//while(1);
return 0;
}
