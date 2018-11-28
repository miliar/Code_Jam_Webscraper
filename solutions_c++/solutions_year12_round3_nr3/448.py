#include <cstdio>
#include <cstring>
#define MAXN 101

int T , N ,M ,  a[MAXN] , b[MAXN];
__int64 ans;
__int64 A[MAXN] , B[MAXN];

__int64 min(__int64 x , __int64 y) {
    if (x < y) return x;
    return y;
}

void    dfs(int atype , __int64 anum , int btype , __int64 bnum , __int64 sum) {
    if (sum > ans) ans = sum;
    if (atype == N || btype == M) return;
    if (a[atype] != b[btype]) {
        dfs(atype,anum,btype+1,0,sum);
        dfs(atype+1,0,btype,bnum,sum);
    }
    else {
      __int64 t = min(A[atype]-anum,B[btype]-bnum);
      if (A[atype]-anum == B[btype]-bnum) dfs(atype+1,0,btype+1,0,sum+t);
      else {
        if (t == A[atype]-anum)
             dfs(atype+1,0,btype,bnum+t,sum+t);
        else
             dfs(atype,anum+t,btype+1,0,sum+t);
      }
    }
}

int main () {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    int i , j;
    scanf("%d\n",&T);
    for (int p = 1;p <= T;p++) {
        scanf("%d %d\n",&N,&M);
        for (i = 0;i < N;i++)
            scanf("%I64d %d\n",&A[i],&a[i]);
        for (i = 0;i < M;i++)
            scanf("%I64d %d\n",&B[i],&b[i]);
        ans = 0;
        dfs(0,0,0,0,0);
        printf("Case #%d: %I64d\n",p,ans);
    }
    return 0;
}
