#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <list>
#include<queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char A[15][15];
int C,M,N;
int dp[12][(1<<10) + 1];

bool f2(int bm1,int bm,int m) {
	for(int i = 0; i < N;++i) {
		if(((1<<i)&bm) && A[m][i] == 'x') return false;
		if(((1<<i)&bm) && i > 0 && A[m][i-1] != 'x' && ((1<<(i-1))&bm)) return false;
		if(((1<<i)&bm) && i < N-1 && A[m][i+1] != 'x' && ((1<<(i+1))&bm)) return false;
		if(((1<<i)&bm) && i < N-1 && m > 0 && A[m-1][i+1] != 'x' && ((1<<(i+1))&bm1)) return false;
		if(((1<<i)&bm) && i > 0 && m > 0 && A[m-1][i-1] != 'x' && ((1<<(i-1))&bm1)) return false;
	}
	return true;
}


int main() {
	scanf("%d\n",&C);
	for(int ii = 1;ii<=C;++ii) {
		scanf("%d %d\n",&M,&N);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<M;++i) scanf("%s\n",A+i);
		for(int i = 0;i < (1<<N);++i) {
			if(f2(0,i,0)) dp[0][i] = __builtin_popcount(i);
			//printf("%d %d\n",i,dp[0][i]);
		}
		for(int i = 1;i < M;++i) {
		for(int k = 0; k < (1<<N);++k) 	for(int j = 0; j < (1<<N);++j) {
				if(f2(0,j,i-1) && f2(j,k,i)) dp[i][k] = max(dp[i][k],dp[i-1][j]+__builtin_popcount(k));
			}
		}
		int mm = 0;
		for(int i =0; i < (1 << N); ++i) mm = max(mm,dp[M-1][i]);
		printf("Case #%d: %d\n",ii,mm);
	}
	return 0;
}
