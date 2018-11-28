#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define INF (1<<30)
#define EPS 1e-8
#define LLD long long int
using namespace std;

int n,c,a[105],dp[20005];
long long int x,y,z,AC,m;

int main(){

	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%I64d%d",&m,&n);
		
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		
		dp[0]=0;
		for (int i=1;i<=20000;i++){
			dp[i]=-1;
			for (int j=1;j<=n;j++)
			    if (i>=a[j]){
					if (dp[i-a[j]]==-1) continue;
					if (dp[i-a[j]]+1<=dp[i]||dp[i]==-1) dp[i]=dp[i-a[j]]+1;
				}
		}
		
		AC=-1;
		for (int i=1;i<=20000;i++){
			x=m/(LLD)i;
			y=m-x*(LLD)i;
			if (dp[i]==-1||dp[y]==-1) continue;
			
			z=x*(LLD)dp[i]+dp[y];
			if (AC==-1||z<AC) AC=z;

		}

		if (AC>=0) printf("Case #%d: %I64d\n",tc,AC);
		else printf("Case #%d: IMPOSSIBLE\n",tc);
	}
	
	return 0;
}
