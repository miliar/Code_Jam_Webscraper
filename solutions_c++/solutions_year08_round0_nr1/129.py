#pragma warning (disable:4786)
#include<stdio.h>
#include<string>
#include<map>
using namespace std;

#define INF 1000000000

int dp[1001][101];

int n;
map<string,int> M;

int main(){

	char name[1005];

	int T,N;
	int i,j,x,q,id;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d",&n);gets(name);
		M.clear();
		for(i=1;i<=n;i++){
			gets(name);
			M[string(name)] = i;
		}

		for(i=1;i<=n;i++)
			dp[0][i] = 0;

		scanf("%d",&q);gets(name);
		for(x=1;x<=q;x++){
			gets(name);
			id = M[string(name)];

			for(i=1;i<=n;i++){
				dp[x][i] = INF;
				if(i==id)
					continue;
				for(j=1;j<=n;j++)
					if( dp[x-1][j] + (i!=j) < dp[x][i])
						dp[x][i] = dp[x-1][j] + (i!=j);
			}
		}

		x = INF;
		for(i=1;i<=n;i++)
			if(dp[q][i] < x)
				x = dp[q][i];
		printf("Case #%d: %d\n",N,x);
		
	}

	return 0;
}