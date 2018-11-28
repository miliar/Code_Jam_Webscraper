// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <set>
#include <map>

/////////////////////////
///@author: sakar2003 ///
///@lang: C++         ///
/////////////////////////

using namespace std;
typedef __int64 LL;

const int MAXN = 1 << 10;

int T;
int N,K,R;
int d[MAXN], nextIdx[MAXN];
LL sum[MAXN << 1], sub[MAXN];


void bs(int idx, LL x) {
	int low = idx, high = idx + N;
	while (high - low > 1) {
		int mid = (high + low) / 2;
		if (sum[mid] - sum[idx] > x) {
			high = mid;
		} else {
			low = mid;
		}
	}
	LL si = sum[idx];
	LL sh = sum[high];
	LL sl = sum[low];
	sub[idx] = x - (sl - si);
	nextIdx[idx] = low % N;
}

void init(){
}

struct Node{
	int r,c, step;
	Node(int rr, int cc, int s):r(rr),c(cc),step(s){}
	bool operator<(const Node& b)const{
		return step > b.step;
	}
};

LL solve(){
	LL total = 1;
	sum[0] = 0;
	for (int i = 1; i <= N * 2; ++i) {
		sum[i] = sum[i - 1] + d[(i - 1) % N];
	}
	LL all = sum[N];
	if (K >= all) {
		return total * all * R;
	}
	for (int i = 0; i < N; ++i) {
		bs(i, K);
	}
	total *= R;
	total *= K;
	int pos = 0;
	while (R--) {
		total -= sub[pos];
		pos = nextIdx[pos];		
	}
	return total;
}


int main()
{
	//freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	scanf("%d", &T);
	init();
	for(int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d%d", &R,&K,&N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &d[i]);
		}
		LL ans = solve();
		//if(ans > 0)
			printf("Case #%d: %I64d\n", tt, ans);
		//else
		//	printf("Case #%d: %I64d\n", tt);
	}

	return 0;
}
