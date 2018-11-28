#include <iostream>
#include <cstdio>
#include <cmath>
#define FOR(a,b,c) for(int a=b;a<=c;a++)
#define FORR(a,b,c) for(int a=b;a>=c;a--)
using namespace std;
const int inf=1000000000;
int res,ts,a[110],na,b[110],nb,u,v,ntest,n;
int l[110];
char m;
int main(){
freopen("A.INP","r",stdin);
freopen("A.OUT","w",stdout);
scanf("%d",&ntest);
FOR(nt,1,ntest){
                scanf("%d ",&n);
                na=nb=res=0;
                FOR(i,1,n){
                           scanf("%c %d ",&m,&ts);
                           l[i]=(m=='O');
                           if (m=='O')a[++na]=ts;else b[++nb]=ts;  
                           }
                u=v=1;
                na=nb=0;
                FOR(i,1,n)
                if (l[i]){
                          res+=abs(a[++na]-u)+1;
                          if (b[nb+1]>v)v+=min(b[nb+1]-v,abs(a[na]-u)+1);
                          else
                          if (b[nb+1]<v)v-=min(v-b[nb+1],abs(a[na]-u)+1);
                          u=a[na];
                          }
                          else
                          {
                          res+=abs(b[++nb]-v)+1;
                          if (a[na+1]>u)u+=min(a[na+1]-u,abs(b[nb]-v)+1);
                          else
                          if (a[na+1]<u)u-=min(u-a[na+1],abs(b[nb]-v)+1);
                          v=b[nb];
                          }
                printf("Case #%d: %d\n",nt,res);
                };
fclose(stdin);
fclose(stdout);
}
