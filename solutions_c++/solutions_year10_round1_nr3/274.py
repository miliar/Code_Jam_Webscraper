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

#define G 0.6180339887
int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T , cas = 1;
	scanf("%d",&T);
	while(T --) {
		long long A1 , A2 , B1 , B2;
		scanf("%lld%lld%lld%lld",&A1,&A2,&B1,&B2);
		long long cnt = 0;
		for (long long i = A1 ; i <= A2 ; i ++) {
			long long e = i + (long long)(i*G);
			if(e > B2) e = B2;
			long long s = max(i,B1);
			if(s > e) continue;
			cnt += (e - s + 1);
		}
		for (long long i = B1 ; i <= B2 ; i ++) {
			long long e = i + (long long)(i*G);
			if(e > A2) e = A2;
			long long s = max(i+1,A1);
			if(s > e) continue;
			cnt += (e - s + 1);
		}
		printf("Case #%d: %lld\n",cas++,(A2-A1+1)*(B2-B1+1) - cnt);
	}
	return 0;
}