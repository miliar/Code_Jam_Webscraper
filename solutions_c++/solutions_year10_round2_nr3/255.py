/*****************************

******************************/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define rep(i,n) for((i)=0;(i)<(n);++(i))

#define MOD 100003

i64 memo[510][510];
i64 C[510][510];

i64 go1(i64 n, i64 r){
	i64 &ret = C[n][r];
	if(-1!=ret) return ret;

	if (n == r) return ret = 1;
	if (n < r) return ret = 0;
	
	if (r == 0) return ret = 1;
	
	ret = go1(n -1, r) + go1(n - 1, r - 1);
	ret%=MOD;

	return ret;
}

i64 go(i64 val, i64 ind){
	i64 &ret = memo[val][ind];
	if(-1!=ret) return ret;

	if (ind == 1) return ret = 1;

	i64 inMid = val - ind - 1;
	i64 i;
	ret = 0;
	for (i = 0; i <= inMid; ++i){
		i64 c = go1(inMid, i);
		if (ind - 1 - i < 1) continue;
		
		ret = (ret + go(ind, ind - 1 - i) * c) % MOD;
	}

	return ret;
}

i64 main (void){
	freopen("C-large.in","r",stdin);
	freopen("C-large.ans","w",stdout);
	i64 kase, i;
	scanf("%I64d", &kase);
	memset(C, -1, sizeof(C));
	memset(memo, -1, sizeof(memo));
	for(i64 t = 1; t <= kase; ++t){
		i64 N; scanf("%I64d", &N);

		i64 res = 0;
		for (i = 1; i < N; ++i) {
			res = (res + go(N, i))% MOD;
		}
		printf("Case #%I64d: %I64d\n",t, res);

	}

	return 0;
}