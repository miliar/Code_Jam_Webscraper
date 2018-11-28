#include<cstdio>
#include<algorithm>
using namespace std;

const int MAXN  =   500000+10;
long long P   =   1000000007;

long long cnt[MAXN];
long long c[MAXN];
long long X,Y,Z,A[MAXN];
int n,m;
int seq[MAXN],list[MAXN];

long long sum(int p){
    //printf("sum %d\n", p);
    long long res = 0;
    for(; p; p=p&(p-1))
        res = (res + c[p]) % P;
    return res;
}

void add(int p,long long d){
    //printf("add %d %I64d\n", p, d);
    for(; p<=n+1; p=(p|(p-1))+1)
        c[p] = (c[p] + d) % P;
}

void init(){
    scanf("%d%d%I64d%I64d%I64d", &n, &m, &X, &Y, &Z);
    for(int i=0; i<m; ++i)scanf("%I64d", &A[i]);
    for(int i=0; i<n; ++i){
        list[i] = seq[i] = A[i % m];
        //printf("seq[%d] = %d\n", i,seq[i]);
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
    }
    sort(list, list+n);
    int list_cnt = unique(list, list+n) - list;
    for(int i=0; i<n; ++i){
        seq[i] = lower_bound(list, list+list_cnt, seq[i]) - list + 1;
        //printf("seq[%d] = %d\n", i,seq[i]);
    }
    //printf("Hello\n");
}

void solve(){
    memset(c, 0, sizeof(c));
    add(n+1, 1);
    for(int i=n-1; i>=0; --i){
        cnt[i] = ((sum(n+1) - sum(seq[i])) % P + P) % P;
        //printf("cnt[%d] = %I64d\n", i,cnt[i]);
        add(seq[i], cnt[i]);
    }
    printf("%I64d\n", (sum(n) % P + P) % P);
}

int main(){
    int N;
    scanf("%d", &N);
    for(int i=1; i<=N; ++i){
        init();
        printf("Case #%d: ", i);
        solve();
    }
}
