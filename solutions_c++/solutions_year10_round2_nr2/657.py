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
 int T,vv=0;
ll ass[200],v[200];
 cin>>T;while(T--)
{ll n,k,b,t,skip,swap,tot,fin;
scanf("%lld %lld %lld %lld",&n,&k,&b,&t);
for(int i=0;i<n;i++)
scanf("%lld",&ass[i]);
tot=0;
for(int i=0;i<n;i++)
scanf("%lld",&v[i]);
skip=0;
swap=0;
vv++;
for(int i=n-1;i>=0;i--)
    {
                 fin=ass[i]+t*v[i];
                 if(fin>=b)
                 {tot++;
                 swap=swap+skip;
                           if(tot==k)
                        break;
                 }
                 else
                 {skip++;}
     }
if(tot<k)
printf("Case #%d: IMPOSSIBLE\n",vv);
else
printf("Case #%d: %lld\n",vv,swap);



}
//while(1);
return 0;
}
