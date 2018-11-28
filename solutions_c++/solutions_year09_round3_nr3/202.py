#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int res,ntc,p,q,tq,cost,dp[200][200],inf=100000000;
vector <int> qq;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output11.txt","w",stdout);
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		res=0;
		scanf("%d %d",&p,&q);
		qq.clear();
		for (int i=0;i<q;i++){
			scanf("%d",&tq); tq--;
			qq.push_back(tq);
		}
		memset(dp,0,sizeof(dp));
		for (int d=0;d<q;d++)
			for (int i=0;(i+d<q);i++){
				int j=i+d;
				dp[i][j]=inf;
				for (int k=i;k<=j;k++){
					cost=0;
					if (i<=k-1) cost+=dp[i][k-1];
					if (k+1<=j) cost+=dp[k+1][j];
					if (i<k) cost+=(qq[k]-qq[i]);
					if (i==0) cost+=qq[i];
					else cost+=(qq[i]-qq[i-1]-1);
					if (k<j) cost+=(qq[j]-qq[k]);
					if (j==q-1) cost+=(p-qq[j]-1);
					else cost+=(qq[j+1]-qq[j]-1);
					if (cost<dp[i][j]) dp[i][j]=cost;
				}
			}
		printf("Case #%d: %d\n",tc,dp[0][q-1]);
	}
	return 0;
}
