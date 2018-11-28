#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#define MAXN 1000

using namespace std;

int n,m,test,cur = 1,ans;
int s[MAXN][MAXN],sum[MAXN][MAXN];
char S[MAXN];
int sum1[MAXN][MAXN],sum2[MAXN][MAXN],sum3[MAXN][MAXN],sum4[MAXN][MAXN];
void init(){
	scanf("%d%d%d",&n,&m,&ans);
	ans = 0;
	memset(sum,0,sizeof(sum));
	for ( int i = 1 ; i <= n ; i++ ){
		scanf("%s",S);
		for ( int j = 1 ; j <= m ; j++ ){
			s[i][j] = S[j-1]-'0';
			sum[i][j] = sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+s[i][j];
		}
	}
	for ( int i = 1 ; i <= n ; i++)
		for ( int j = 1 ; j <= m ; j++ )
			sum1[i][j] = sum1[i-1][j]+i*(sum[i][j]-sum[i-1][j]);
	for ( int i = 1 ; i <= n ; i++)
		for ( int j = 1 ; j <= m ; j++ )
			sum2[i][j] = sum2[i-1][j]+(n-i+1)*(sum[i][j]-sum[i-1][j]);
	for ( int j = 1 ; j <= m ; j++ )
		for ( int i = 1 ; i <= n ; i++)
			sum3[i][j] = sum3[i][j-1]+j*(sum[i][j]-sum[i][j-1]);
	for ( int j = 1 ; j <= m ; j++ )
		for ( int i = 1 ; i <= n ; i++)
			sum4[i][j] = sum4[i][j-1]+(m-j+1)*(sum[i][j]-sum[i][j-1]);
}
void work(){
	int sumh1,sumh2,sumv1,sumv2;
	for ( int i = 1 ; i <= n ; i++ )
		for ( int j = 1; j <= m ; j++ )
			for ( int k = 1 ; i-k>=1 && i+k <= n && j-k>=1 && j+k <= m ; k++ ){
				sumh1 = sum1[i+k][j+k]-sum1[i+k][j-k-1]-sum1[i][j+k]+sum1[i][j-k-1]
				        -i*(sum[i+k][j+k]-sum[i+k][j-k-1]-sum[i][j+k]+sum[i][j-k-1])-k*(s[i+k][j+k]+s[i+k][j-k]);
				sumh2 = sum2[i-1][j+k]-sum2[i-1][j-k-1]-sum2[i-k-1][j+k]+sum2[i-k-1][j-k-1]
				        -(n-i+1)*(sum[i-1][j+k]-sum[i-1][j-k-1]-sum[i-k-1][j+k]+sum[i-k-1][j-k-1])-k*(s[i-k][j+k]+s[i-k][j-k]);
				sumv1 = sum3[i+k][j+k]-sum3[i+k][j]-sum3[i-k-1][j+k]+sum3[i-k-1][j]
				        -j*(sum[i+k][j+k]-sum[i+k][j]-sum[i-k-1][j+k]+sum[i-k-1][j])-k*(s[i+k][j+k]+s[i-k][j+k]);
				sumv2 = sum4[i+k][j-1]-sum4[i+k][j-k-1]-sum4[i-k-1][j-1]+sum4[i-k-1][j-k-1]
				        -(m-j+1)*(sum[i+k][j-1]-sum[i+k][j-k-1]-sum[i-k-1][j-1]+sum[i-k-1][j-k-1])-k*(s[i-k][j-k]+s[i+k][j-k]);
				if (sumh1==sumh2 && sumv1==sumv2) ans = max(ans,k*2+1);
			}
	for ( int i = 1; i <= n ; i++ )
		for ( int j = 1; j <= m ; j++ )
			for ( int k = 2 ; i-k>=1 && j-k>=1 && i+k-1<=n && j+k-1 <= m ; k++ ){
				sumh1 = sum1[i+k-1][j+k-1]-sum1[i+k-1][j-k-1]-sum1[i-1][j+k-1]+sum1[i-1][j-k-1]
				        -(i-1)*(sum[i+k-1][j+k-1]-sum[i+k-1][j-k-1]-sum[i-1][j+k-1]+sum[i-1][j-k-1])-k*(s[i+k-1][j+k-1]+s[i+k-1][j-k]);
				sumh2 = sum2[i-1][j+k-1]-sum2[i-1][j-k-1]-sum2[i-k-1][j+k-1]+sum2[i-k-1][j-k-1]
				        -(n-i+1)*(sum[i-1][j+k-1]-sum[i-1][j-k-1]-sum[i-k-1][j+k-1]+sum[i-k-1][j-k-1])-k*(s[i-k][j+k-1]+s[i-k][j-k]);
				sumv1 = sum3[i+k-1][j+k-1]-sum3[i+k-1][j-1]-sum3[i-k-1][j+k-1]+sum3[i-k-1][j-1]
				        -(j-1)*(sum[i+k-1][j+k-1]-sum[i+k-1][j-1]-sum[i-k-1][j+k-1]+sum[i-k-1][j-1])-k*(s[i+k-1][j+k-1]+s[i-k][j+k-1]);
				sumv2 = sum4[i+k-1][j-1]-sum4[i+k-1][j-k-1]-sum4[i-k-1][j-1]+sum4[i-k-1][j-k-1]
				        -(m-j+1)*(sum[i+k-1][j-1]-sum[i+k-1][j-k-1]-sum[i-k-1][j-1]+sum[i-k-1][j-k-1])-k*(s[i-k][j-k]+s[i+k-1][j-k]);
				if (sumh1==sumh2 && sumv1==sumv2) ans = max(ans,k*2);
			}

}
int main(){
	freopen("B-small-attempt3.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		printf("Case #%d: ",cur);
		init();
		work();
		if (ans<3) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
	}
}
