#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <boost/foreach.hpp>

using namespace std;
using namespace boost;

int NODE[10002][2];
int DP[10002][2];
int INF = 100000000;
int M, V;

void build( int n )
{
	//printf("%d: %d %d\n", n, DP[n][0], DP[n][1]);
	if( NODE[n][0] == -1){
		DP[n][ NODE[n][1] ] = 0;
		return ;
	}
	build(2*n);
	build(2*n+1);
	if( NODE[n][0] == 0 ){
		DP[n][1] = min(DP[2*n][1], DP[2*n+1][1]);
		DP[n][0] = min(INF, DP[2*n][0] + DP[2*n+1][0]);
	}
	if( NODE[n][0] == 1 ){
		DP[n][1] = min(INF, DP[2*n][1] + DP[2*n+1][1]);
		DP[n][0] = min(DP[2*n][0], DP[2*n+1][0]);
	}
	if( NODE[n][1] == 1){
		if( NODE[n][0] == 1 ){
			DP[n][1] = min(DP[n][1], min(DP[2*n][1], DP[2*n+1][1]) + 1);
			DP[n][0] = min(DP[n][0], min(INF, DP[2*n][0] + DP[2*n+1][0] + 1));
		}
		if( NODE[n][0] == 0 ){
			DP[n][1] = min(DP[n][1], min(INF, DP[2*n][1] + DP[2*n+1][1] + 1));
			DP[n][0] = min(DP[n][0], min(DP[2*n][0], DP[2*n+1][0]) + 1);
		}
	}
}
int main()
{
	int caseN;
	scanf("%d", &caseN);
	for(int cc=0; cc<caseN;cc++){
		scanf("%d %d", &M, &V);
		for(int i=0;i<M+1;i++)
			DP[i][0] = DP[i][1] = INF;
		for(int i=0;i<(M-1)/2;i++)
			scanf("%d%d", &NODE[i+1][0], &NODE[i+1][1] ); // G C
		for(int i=0;i<(M+1)/2;i++){
			NODE[(M-1)/2+i+1][0] = -1;
			scanf("%d", &NODE[(M-1)/2+i+1][1]);
		}
		build( 1 );
		if(DP[1][V] != INF)
			printf("Case #%d: %d\n", cc+1, DP[1][V]);
		else
			printf("Case #%d: IMPOSSIBLE\n", cc+1);
	}
	return 0;
}
