#include <cstdio>
#include <cstring>
const int MOD = 100003;

long long pd[600][600];
long long bin[600][600];

long long binomial(int n, int k) {
    if (bin[n][k]!=-1) return bin[n][k];
    if (k>n-k) k=n-k;
    if (k==0) return 1;
    return (bin[n][k] = (n-k+1)*binomial(n,k-1)/k);
}

int max(int a, int b) {
    return a>b?a:b;
}


long long calc(int n, int t) {
    if (t>n-1) return 0;
    if (t == 1) return 1;
    if (pd[n][t]!=-1) return pd[n][t];
    
    long long res=0;
    for (int x=max(1,2*t-n); x<t; x++)
        res = (res + calc(t,x)*binomial(n-t-1, t-x-1))%MOD;
        
    return (pd[n][t] = res);
}

int main() {
    int nt, n;
    
    scanf(" %d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        scanf(" %d",&n);
        
        memset(pd,-1,sizeof(pd));
        memset(bin,-1,sizeof(bin));
        
        int res = 0;
        for (int i=1; i<n; i++) res=(res+calc(n,i))%MOD;
        
        printf("Case #%d: %d\n",ct, res);
    }
    
    return 0;
}
