#include <stdio.h>

#define maxn 1000100

char p[maxn];
int pr[maxn],ptop;

void sol(int cas){
    long long n,i,j;
    int c,k;
    scanf("%lld",&n);

    if (n<2){
        printf("Case #%d: %d\n",cas,0);
        return;
    }
    c = 1;
    
    for (k=0;k<ptop;k++){
        i=pr[k];
  //      printf("i=%d k=%d\n",i,k);
        if (i*i>n) break;
        for (j=i;j<=n;j*=i) c++;
//        printf("c=%d\n",c);
        c--;
    }

    printf("Case #%d: %d\n",cas,c);
}

void prime(){
    int i,j;
    for (i=0;i<maxn;i++) p[i]=1;
    p[0]=p[1]=0;
    for (i=2;i*i<maxn;i++){
        if (!p[i]) continue;
        for (j=i*i;j<maxn;j+=i) p[j]=0;
    }
    ptop = 0;
    for (i=2;i<maxn;i++) if (p[i]) pr[ptop++] = i;
}

int main(){
    int t,cas;
    scanf("%d",&t);
    prime();
    for (cas=1;cas<=t;cas++) sol(cas);
    return 0;
}

