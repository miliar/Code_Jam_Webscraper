/*
 *  pc.cpp
 *  
 *
 *  Created by Bruce Kuo on 12/5/5.
 *  Copyright 2012 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using std::vector;


int n;
int S[510];
bool find;
int used[510];
vector<int> S1, S2;

bool check(int s1, int s2) {
	if(s1 != s2)	return false;
	if(S1.size() != S2.size())	return true;
	for(int i=0;i<S1.size();++i)
		if( S1[i] != S2[i] )
			return true;
	return false;
}

void go(int now, int sum1, int sum2) {
	if( check(sum1, sum2) ) {
		find = true;
		for(int i=0;i<S1.size()-1;++i)
			printf("%d ",S1[i]);
		printf("%d\n",S1[S1.size()-1]);
		for(int i=0;i<S2.size()-1;++i)
			printf("%d ",S2[i]);
		printf("%d\n",S2[S2.size()-1]);
		return;
	}
	if(now >= n)	return;
	go(now+1, sum1, sum2);
	if(find)	return;
	
	S1.push_back(S[now]);
	go(now+1, sum1+S[now], sum2);
	S1.pop_back();
	if(find)	return;
	
	S2.push_back(S[now]);
	go(now+1, sum1, sum2+S[now]);
	S2.pop_back();
	if(find)	return;
	
	S1.push_back(S[now]);
	S2.push_back(S[now]);
	go(now+1, sum1, sum2+S[now]);
	S2.pop_back();
	S1.pop_back();
	if(find)	return;
	
}

int main() {
	int t, cases=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d", S+i);
		std::sort(S, S+n);
		S1.clear();
		S2.clear();
		find = false;
		memset(used, 0, sizeof(used));
		printf("Case #%d:\n",++cases);
		go(0, 0, 0);
	}
	
	return 0;
}

