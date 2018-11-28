#include <cstdio>
#include <ctime>
#include <cstring>
#include <assert.h>
#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define FAULT 1E16
long long dp[10][512][2];
long long cost[10][512][2];
int price[10][512];
int missbound[1024];

void getdp(int p)
{
	for(int i=0;i<(1<<(p-1));++i){
		cost[0][i][1] = price[0][i];
		cost[0][i][0] = 0;
		dp[0][i][0] = MAX(p-missbound[2*i],p-missbound[2*i+1]);
		dp[0][i][1] =  dp[0][i][0]-1;
		if(dp[0][i][0] >= p){
			dp[0][i][0]  = FAULT;
			cost[0][i][0]  = FAULT;
		}
	}
	for(int i=1;i<p;++i){
		for(int j=0;j<(1<<(p-1-i));++j){
			//选该场比赛
			long long mdp[2],mcost[2];
			if(cost[i-1][j*2][1] > cost[i-1][j*2][0]){
				mdp[0] = dp[i-1][j*2][0];
				mcost[0] = cost[i-1][j*2][0];
			}
			else{
				mdp[0] = dp[i-1][j*2][1];
				mcost[0] = cost[i-1][j*2][1];
			}

			if(cost[i-1][j*2+1][1] > cost[i-1][j*2+1][0]){
				mdp[1] = dp[i-1][j*2+1][0];
				mcost[1] = cost[i-1][j*2+1][0];
			}
			else{
				mdp[1] = dp[i-1][j*2+1][1];
				mcost[1] = cost[i-1][j*2+1][1];
			}

			dp[i][j][1] = MAX(mdp[0],mdp[1] ) -1 ;
			cost[i][j][1] = price[i][j] + mcost[0] + mcost[1];

			//不选该场比赛
			mdp[0] = dp[i-1][j*2][1];
			mcost[0] = cost[i-1][j*2][1];
			if(dp[i-1][j*2][0] <= p-i-1 && cost[i-1][j*2][0] < cost[i-1][j*2][1]){
				mdp[0] = dp[i-1][j*2][0];
				mcost[0] = cost[i-1][j*2][0];
			}
			mdp[1] = dp[i-1][j*2+1][1];
			mcost[1] = cost[i-1][j*2+1][1];
			if(dp[i-1][j*2+1][0] <= p-i-1 && cost[i-1][j*2+1][0] < cost[i-1][j*2+1][1]){
				mdp[1] = dp[i-1][j*2+1][0];
				mcost[1] = cost[i-1][j*2+1][0];
// 				printf("sddg %lld\n", mcost[1]);
			}
			dp[i][j][0] = MAX(mdp[0],mdp[1] )  ;
			cost[i][j][0] = mcost[0] + mcost[1];
			if(dp[i][j][0] > (p-i-1)){
				dp[i][j][0] = cost[i][j][0] = FAULT;
			}
// 			printf("dp(%d,%d,1) = %lld\n",i,j,dp[i][j][1]);
// 			printf("cost(%d,%d,1) = %lld\n",i,j,cost[i][j][1]);
// 			printf("dp(%d,%d,0) = %lld\n",i,j,dp[i][j][0]);
// 			printf("cost(%d,%d,0) = %lld\n\n",i,j,cost[i][j][0]);
		}
	}
}

int main()
{
 	freopen("input.txt","r",stdin);
 	freopen("output.txt","w",stdout);
	int T,p;
	cin>>T;
	for(int t=1;t<=T;++t){
		cin>>p;
		for(int i=0;i<(1<<p);++i)
			cin>>missbound[i];
		for(int i=0;i<p;++i){
			for(int j=0;j<(1<<(p-1-i));++j)
				cin>>price[i][j];
		}
		getdp(p);
		long long res;
		res = MIN(cost[p-1][0][1], cost[p-1][0][0]);
		printf("Case #%d: %lld\n",t,res);
	}
	return 0;
}