#include<iostream>
using namespace std;
__int64 N,n,m,x,y,z;
__int64 A[500001]; 
__int64 b[500001];
__int64 g[500001];
__int64 total;
int main()
{
int i,j,k,o;
freopen("C-small.in.txt","r",stdin);
freopen("2.out","w",stdout);
scanf("%I64d",&N);
for(o=1;o<=N;o++)
{
total=0;
scanf("%I64d %I64d %I64d %I64d %I64d",&n,&m,&x,&y,&z);
for(j=0;j<m;j++) scanf("%I64d",&A[j]);
for(j=0;j<=n-1;j++)
{
        b[j]=A[j%m];
		A[j%m]=(x * A[j%m] + y * (j + 1)) % z;

}
for(i=0;i<=n-1;i++) g[i]=1;
for(i=1;i<=n-1;i++)
{
	for(j=0;j<=i-1;j++)
  {
    if (b[j]<b[i]) g[i]+=(g[j]%1000000007)%1000000007;
  }
}
for(i=0;i<=n-1;i++)
total=(total+g[i])%1000000007;
printf("Case #%d: ",o);
printf("%I64d\n",total);
}
return 0;
}