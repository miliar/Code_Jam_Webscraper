// round1_1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdio.h"
#include <vector>
#include <algorithm>
using namespace std;

int cmp(__int64 a, __int64 b){
	return a > b;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	vector<__int64> va;
	vector<__int64> vb;
	int t;
	scanf("%d", &t);
	int i;
	for(i = 1 ; i <= t ; ++i){
		int n;
		scanf("%d",&n);
		va.resize(n);
		vb.resize(n);
		int j;
		for(j = 0 ; j < n ; ++j){
			scanf("%I64d", &va[j]);
		}
		for(j = 0 ; j < n ; ++j){
			scanf("%I64d", &vb[j]);
		}
		sort(va.begin(), va.end());
		sort(vb.begin(), vb.end(), cmp);
		__int64 sum = 0;
		for(j = 0 ; j < n ; ++j){
			sum += va[j] * vb[j];
		}
		printf("Case #%d: %I64d\n", i, sum);
	}
	return 0;
}

