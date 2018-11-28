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

const int MAXN = 100;

int T;
int N,K;


void init(){
}

struct Node{
	int r,c, step;
	Node(int rr, int cc, int s):r(rr),c(cc),step(s){}
	bool operator<(const Node& b)const{
		return step > b.step;
	}
};

int solve(){
	int x = 1 << N;
	int y = 1 + K;
	return y % x == 0;
}

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	scanf("%d", &T);
	init();
	for(int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d", &N,&K);
		
		int ans = solve();
		if(ans > 0)
			printf("Case #%d: ON\n", tt, ans);
		else
			printf("Case #%d: OFF\n", tt);
	}

	return 0;
}
