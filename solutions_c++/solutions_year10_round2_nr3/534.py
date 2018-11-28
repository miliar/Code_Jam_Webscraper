#include <stdio.h>
#include <algorithm>

using namespace std;

const int mod=100003;

long long f[510][510];
long long c[510][510];
long long ans[510];

int main()
{

	int T, i, j, k, ti, n;;
	for (i=0; i<=500; i++)
	{
		c[i][0]=c[i][i]=1;
		for (j=1; j<i; j++)
		  c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod;
	}
	f[1][1]=1;	
	for (i=2; i<=500; i++)
	 for (j=1; j<i; j++)
	 {
	 	if (j==1) f[i][j]=1;
	 	else
		for (k=max(j*2-i, 1); k<j; k++)
		  f[i][j]=(f[i][j]+f[j][k]*c[i-j-1][j-k-1])%mod;	 	
		ans[i]=(ans[i]+f[i][j])%mod;
	 }
	 
	 freopen("c.txt", "r", stdin);
	 freopen("c.out", "w", stdout);	 
	 scanf("%d", &T);
	 for (ti=1; ti<=T; ti++)
	 {
	 	scanf("%d", &n);
	 	printf("Case #%d: %I64d\n", ti, ans[n]);
	 }
	 
	return 0;
}
