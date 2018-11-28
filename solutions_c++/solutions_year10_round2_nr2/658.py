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
ll a[200],v[200];
 int T,vv=0;cin>>T;while(T--)
{ll n,k,b,t,skip,swap,tot,fin;
scanf("%lld %lld %lld %lld",&n,&k,&b,&t);
vv++;
for(int i=0;i<n;i++)
scanf("%lld",&a[i]);
for(int i=0;i<n;i++)
scanf("%lld",&v[i]);
swap=0;
skip=0;
tot=0;
for(int i=n-1;i>=0;i--)
    {
                 fin=a[i]+t*v[i];
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
