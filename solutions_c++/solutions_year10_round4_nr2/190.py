#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxr = 11, maxn=(1<<11)+100, INF=1000000000;

int pri[maxr][maxn], miss[maxn], dp[maxr][maxr][maxn];
bool a[maxn];
int task, T=0, r, n;

void calc(int o){
	if ( o == r-1 ){
		for (int i=0; i<(1<<r-1); i++){
			dp[o][max(r-miss[i<<1], r-miss[(i<<1)+1])][i] = 0;
			for (int j=0; j<r; j++)	
				dp[o][j+1][i] = min( dp[o][j+1][i], dp[o][j][i] );
		}
	}else{
		calc( o + 1 );
		for (int i=0; i<(1<<o); i++){
			for (int j=0; j<r; j++){
				int cur = min( dp[o+1][j][i<<1], dp[o+1][j+1][i<<1] + pri[o+1][i<<1] ) +
						  min( dp[o+1][j][(i<<1)+1], dp[o+1][j+1][(i<<1)+1] + pri[o+1][(i<<1)+1]);
				if ( dp[o][j][i] > cur )
					dp[o][j][i] = cur;
			}
			for (int j=0; j<r; j++)	
				dp[o][j+1][i] = min( dp[o][j+1][i], dp[o][j][i] );
		}
	}			
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d", &task); task--;){
		scanf("%d", &r);
		n = (1<<r);
		for (int i = 0; i<n; i++)
			scanf("%d", &miss[i]);
		for (int i=r-1; i>=0; i--)
		for (int j=0; j<(1<<i); j++)
			scanf("%d", &pri[i][j]);

		for (int i=0; i<maxr; i++)
		for (int j=0; j<maxr; j++)
		for (int k=0; k<maxn; k++)
			dp[i][j][k] = INF;
		calc( 0 );

		printf("Case #%d: %d\n", ++T, min( dp[0][0][0], dp[0][1][0] + pri[0][0] ) );
	}
	return 0;
}
