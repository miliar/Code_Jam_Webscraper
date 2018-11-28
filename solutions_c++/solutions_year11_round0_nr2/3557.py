#include <iostream>
#include <cstring>
#define FOR(a,b,c) for(int a=b;a<=c;a++)
using namespace std;
int ntest;
bool b[100][100];
int a[100][100];
int c[110],top;
int main(){
freopen("B.INP","r",stdin);
freopen("B.OUT","w",stdout);
scanf("%d\n",&ntest);
FOR(nt,1,ntest){
                int m,n;
                memset(b,0,sizeof(b));
                memset(a,0,sizeof(a));
                scanf("%d ",&m);
                FOR(i,1,m){
                           char u,v,k;
                           scanf("%c%c%c ",&u,&v,&k);
                           a[u-'A'+1][v-'A'+1]=k-'A'+1;
                           a[v-'A'+1][u-'A'+1]=k-'A'+1;
                           }
                scanf("%d ",&m);
                FOR(i,1,m){
                           char u,v,k;
                           scanf("%c%c ",&u,&v);
                           b[u-'A'+1][v-'A'+1]=true;
                           b[v-'A'+1][u-'A'+1]=true;
                           }
                scanf("%d ",&n);
                top=0;
                FOR(i,1,n){
                           char u;
                           scanf("%c",&u);
                           int v=u-'A'+1;
                           while (a[c[top]][v]!=0){
                                 v=a[c[top]][v];
                                 top--;
                                 }
                           top++;
                           c[top]=v;
                           FOR(x,1,top-1)
                           FOR(y,x+1,top)
                           if (b[c[x]][c[y]])top=0;
                           }
                printf("Case #%d: [",nt);
                FOR(i,1,top-1)printf("%c, ",c[i]+'A'-1);
                if (top)printf("%c]\n",c[top]+'A'-1);else printf("]\n");
                }
fclose(stdin);
fclose(stdout);
}
