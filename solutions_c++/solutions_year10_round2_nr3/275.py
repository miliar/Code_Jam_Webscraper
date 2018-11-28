#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <string>
#include <cstring>
#include <ctime>
#include <cmath>

using namespace std;
int dp[1600][1600];
int C[600][600];

long long getc(int n,int k){
	if(n<k)return 0;
	if(k<0)return 0;
	return C[n-k][k];
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q;
	scanf("%d",&q);
	int i,j,k,p;
	for(i=0;i<600;i++)C[i][0]=C[0][i]=1;
	for(i=1;i<600;i++)
		for(j=1;j<600;j++)
			C[i][j]=(C[i-1][j]+C[i][j-1])%100003;
	for(i=2;i<600;i++)dp[i][1]=1;
	for(i=3;i<520;i++){
		for(j=2;j<i;j++){
			for(k=1;k<j;k++){
//				if(i==5)printf("i=%d j=%d k=%d dp[j][k]=%d getc(i-j-1,i-j-k)=%d\n",i,j,k,dp[j][k],getc(i-j-1,i-j-k));
				dp[i][j]=(dp[i][j]+(long long)dp[j][k]*getc(i-j-1,j-k-1))%100003;
			}
		}
	}
	for(int test=1;test<=q;test++){
		int n;
		scanf("%d",&n);
		int ans=0;
		for(i=1;i<n;i++)ans=(ans+dp[n][i])%100003;
		printf("Case #%d: %d\n",test,ans);
	}

	return 0;
}
