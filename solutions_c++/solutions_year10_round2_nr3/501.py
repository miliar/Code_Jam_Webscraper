#include <cstdio>
#include <cstring>
#include <cstdlib>
#define prime 100003

int Test,n,Ans;
int ci[1005][1005],f[1005][1005];

int main()
{
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
scanf("%d",&Test);

ci[0][0]=1;
for (int i=1;i<=500;++i){
ci[i][0]=1;
for (int j=1;j<=500;++j)
ci[i][j]=(ci[i-1][j-1]+ci[i-1][j]) % prime;
}

f[1][0]=1;
for (int i=2;i<=500;++i)
for (int j=0;j<=i-1;++j)
for (int k=0;k<=j-1;++k)
f[i][j]=(f[i][j]+f[j][k]*ci[i-j-1][j-k-1]) % prime;


for (int j=1;j<=Test;++j){
scanf("%d",&n);
printf("Case #%d: ",j);
Ans=0;
for (int i=1;i<=n-1;++i)
Ans=(Ans+f[n][i]) %prime;
printf("%d\n",Ans);
}
// printf("%d %d\n",f[3][1],f[3][2]);
return 0;
}
