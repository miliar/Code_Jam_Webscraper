#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define maxn (25*60)

int n,m,T;
int A[maxn],B[maxn];
int ra,rb;
void input(){
     memset(A,0,sizeof(A));
     memset(B,0,sizeof(B));
     int a,b;
     scanf("%d",&T);
     scanf("%d%d",&n,&m);
     for(int i=0;i<n;i++){
         scanf("%d:%d",&a,&b);
         A[a*60+b]--;
         scanf("%d:%d",&a,&b);
         B[(a*60+b+T)%maxn]++;
     }
     for(int i=0;i<m;i++){
         scanf("%d:%d",&a,&b);
         B[a*60+b]--;
         scanf("%d:%d",&a,&b);
         A[(a*60+b+T)%maxn]++;
     }
}
void work(){
     ra=0;rb=0;
     for(int i=1;i<maxn;i++)A[i]+=A[i-1];
     for(int i=1;i<maxn;i++)B[i]+=B[i-1];
     for(int i=0;i<maxn;i++)ra=max(ra,-A[i]);
     for(int i=0;i<maxn;i++)rb=max(rb,-B[i]);
}
int main(){
    int cases;
    //freopen("b-small.in","r",stdin);
    //freopen("b-small.out","w",stdout);
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    scanf("%d",&cases);
    for(int i=1;i<=cases;i++){
        input();
        work();
        printf("Case #%d: %d %d\n",i,ra,rb);
    }
    return 0;
}
