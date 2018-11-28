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

const int MAXN = 50;

int T;
int N;
double x[MAXN],y[MAXN],r[MAXN];

void init(){
}

double solve(){
	if(N == 1){
		return r[0];
	}
	else if(N == 2){
		return max(r[0], r[1]);
	}
	double ans = 1E308;
	for(int i = 0; i < N; ++i){
		double rad = r[i];
		vector<int> vi;
		for(int j = 0; j < N; ++j){
			if(i != j){
				vi.push_back(j);
			}
		}
		double dist = sqrt((x[vi[0]] - x[vi[1]]) * (x[vi[0]] - x[vi[1]]) + (y[vi[0]] - y[vi[1]]) * (y[vi[0]] - y[vi[1]]));
		if(dist >= r[vi[0]] + r[vi[1]]){
			dist += r[vi[0]] + r[vi[1]];			
		}
		else if(dist <= abs(r[vi[0]] - r[vi[1]])){
			dist = max(r[vi[0]], r[vi[1]]);
		}
		else{
			dist += r[vi[0]] + r[vi[1]];
		}
		rad = max(rad, dist / 2);
		ans = min(ans, rad);
	}
	return ans;
}

int main()
{
	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	scanf("%d", &T);
	init();
	for(int tt = 1; tt <= T; ++tt)
	{
		scanf("%d", &N);
		for(int i = 0; i < N; ++i){
			scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
		}
		double ans = solve();
		printf("Case #%d: %.8lf\n", tt, ans);
	}

	return 0;
}
