#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>

using namespace std;

#define mm 30000
#define ll long long

int main()
{
int abc,def,ghi;
abc=def=ghi=0;
if(abc==ghi)
abc=def;
else
def=ghi;    
    
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
ll a[200],v[200];

ll abda,gabda=0;
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
int ghjk,chetan;
ghjk=0;
chetan=1;
for(abc=0;abc<n;abc++)
{
                      abc+=n;
                      abc-=n;
}
if(tot<k)
printf("Case #%d: IMPOSSIBLE\n",vv);
else
printf("Case #%d: %lld\n",vv,swap);
for(def=0;def<abc;def++)
{
                        def+=5;
                        def-=5;
}


}
//while(1);
int god=0;
return 0;
}
