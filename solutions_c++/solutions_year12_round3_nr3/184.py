#include<stdio.h>
#include<string.h>

#define maxn 1100
#define max(a,b) ((a) > (b)?(a):(b))
#define min(a,b) ((a) < (b)?(a):(b))
#define clear(a,b) memset(a,b,sizeof(a))

int p = 1;
long long f1[maxn][maxn],f2[maxn][maxn],type_b[maxn],type_t[maxn],box[maxn],toy[maxn],dp[maxn][maxn];

void work()
{
  int n,m,i,j,ii,jj,k;
  clear(box,0);
  clear(toy,0);
  clear(type_b,0);
  clear(type_t,0);
  clear(f1,0);
  clear(f2,0);
  clear(dp,0);

  scanf("%d%d",&n,&m);
  for(i = 1;i <= n;i++) scanf("%lld%lld",&box[i],&type_b[i]);
  for(i = 1;i <= m;i++) scanf("%lld%lld",&toy[i],&type_t[i]);
  for(i = 1;i <= n;i++)
    for(j = 1;j <= i;j++)
      for(k = j;k <= i;k++){
       if (type_b[i] == type_b[k]) f1[j][i] += box[k];
       }
  for(i = 1;i <= m;i++)
    for(j = 1;j <= i;j++)
      for(k = j;k <= i;k++){
       if (type_t[i] == type_t[k]) f2[j][i] += toy[k];
       }
   for(i = 1;i <= n;i++)
      for(j = 1;j <= m;j++) {
         dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
         if (type_b[i] == type_t[j]) {
           for(ii = 0;ii < i;ii++)
              for(jj = 0;jj < j;jj++)
                 if (dp[i][j] < dp[ii][jj] + min(f1[ii+1][i],f2[jj+1][j])) dp[i][j] = dp[ii][jj] + min(f1[ii+1][i],f2[jj+1][j]);
           }
         }
    printf("Case #%d: %lld\n",p++,dp[n][m]);
    /*for(i = 1;i <= n;i++,printf("\n"))
       for(j = 1;j <= m;j++)
         printf("%5lld",f1[i][j]);
    printf("***********\n");
    for(i = 1;i <= n;i++,printf("\n"))
       for(j = 1;j <= m;j++)
         printf("%5lld",f2[i][j]);
    printf("***********\n");
    for(i = 1;i <= n;i++,printf("\n"))
       for(j = 1;j <= m;j++)
         printf("%5lld",dp[i][j]);*/
    return ;
}

int main()
{
  int t;
  freopen("xx.in","r",stdin);
  freopen("GCJ_OUT.txt","w",stdout);
  scanf("%d",&t);
  while (t--) work();
  return 0;
}
