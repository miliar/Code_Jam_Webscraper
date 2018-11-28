#include<cstdio>
#include<cstring>
#define MOD 100003
#define LL long long
int n;
int jum;
LL comb[505][505];
LL dp[505][505];
int gcd (int a, int b){
 if (b == 0) return a; return gcd(b,a%b);   
}
/*
LL combi (int n,int k){
 if ((n == 0) || (k == 0))return 1;
 if (n < k) return 1;
 int ar[600];
 for (int j= 1; j <= n-k; j++){
     ar[j] = j;    
 }
 LL res = 1LL;
 for (int i = k+1; i <= n; i++){
     int r = i;
     for (int j = 1; j <= n-k; j++){
         int temp = gcd(r,ar[j]);
         if (temp != 1){

            ar[j] /= temp;
            r /= temp;
         }
     }    
     res = res * (LL)r;
     res %= MOD;
 }
 return res;
}*/

LL  process (int pos, int bil){
 if (pos == 1) {
    return 1;        
 }
 if (dp[pos][bil] != -1) return dp[pos][bil];
 dp[pos][bil] = 0;
 for (int j = 1; j < pos; j++){
     if (pos-j > bil-pos) continue;
     int tempat = pos-j-1;
     int bilangan = bil-pos-1;
     if (bilangan >= tempat){
          dp[pos][bil] += (comb[bilangan][tempat] * process(j, pos))%MOD;
     }
     dp[pos][bil] %= MOD;
 }    
// printf("%d %d %I64d\n",pos,bil,dp[pos][bil]);
 return dp[pos][bil];
}
int main(){
 memset(dp,-1,sizeof(dp));
 for (int i = 0; i <= 500; i++){
     for (int j = 0; j <= i; j++){
         if ((i == 0)|| (j == 0)) comb[i][j] = 1;
         else comb[i][j] = comb[i-1][j]+comb[i-1][j-1];
         comb[i][j] = comb[i][j] % MOD;
         
     }    
 }
// printf("here\n");
 int tc;
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     int jum = 0;
     scanf("%d",&n);
     for (int i = 1; i < n; i++){
         jum += process(i,n);
         jum = jum % MOD;
     }
     printf("Case #%d: %d\n",ti,jum);
 }

}
