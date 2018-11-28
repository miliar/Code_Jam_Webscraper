//============================================================================
// Name        : code.cpp
// Author      : huhao
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <string>
#include <algorithm>
using namespace std;

int dp[111][300];//[i , ai]
int hh[111];
struct Q{
	int pos , val , cost;
	Q(){};
	Q(int a , int b , int c):pos(a) , val(b) , cost(c){}
};
queue <Q> que;
int D , I , M;
void Delete(Q a) {
	int pos = a.pos + 1;
	int val = a.val;
	int cost = a.cost + D;
	if(dp[pos][val] == -1 || dp[pos][val] > cost) {
		dp[pos][val] = cost;
		que.push( Q(pos,val,cost) );
	}
}
void Insert(Q a) {
	int cost = a.cost + I;
	int pos = a.pos;
	for (int val = 0 ; val <= 255 ; val ++) {
		if(a.val == 256 || abs(a.val - val) <= M) {
			if(dp[pos][val] == -1 || dp[pos][val] > cost) {
				dp[pos][val] = cost;
				que.push( Q(pos,val,cost) );
			}
		}
	}
}
void Change(Q a) {
	int pos = a.pos + 1;
	for (int val = 0 ; val <= 255 ; val ++) {
		if(a.val == 256 || abs(a.val - val) <= M) {
			int cost = a.cost + abs(hh[pos] - val);
			if(dp[pos][val] == -1 || dp[pos][val] > cost) {
				dp[pos][val] = cost;
				que.push( Q(pos,val,cost) );
			}
		}
	}
}
int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T , cas = 1;
	scanf("%d",&T);
	while(T --) {

		int N;
		scanf("%d%d%d%d",&D,&I,&M,&N);
		for (int i = 1 ; i <= N ; i ++) {
			scanf("%d",&hh[i]);
		}
		while(!que.empty()) que.pop();
		memset(dp,-1,sizeof(dp));

		que.push( Q(0,256,0) );
		dp[0][256] = 0;
		while(!que.empty()) {
			Q u = que.front();
			que.pop();
			if(u.pos >= N) continue;

			//delete
			Delete(u);
			Insert(u);
			Change(u);
		}
		int ans = 0x7fffffff;
		for (int i = 0 ; i <= 255 ; i ++) {
			if(dp[N][i] != -1) {
				ans = min(ans , dp[N][i]);
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}