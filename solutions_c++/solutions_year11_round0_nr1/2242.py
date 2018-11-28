//============================================================================
// Name        : codeJam.cpp
// Author      : Loai_Ghoraba
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int K;
	scanf("%d\n",&K);
	for(int test=1;test<=K;test++)
	{
		int n;
		scanf("%d ",&n);
		int prev[2]={1,1};
		int totTime[2]={1,1};
		char c;
		int next,i;
		int time=1;
		for(int step=1;step<=n;step++)
		{
			scanf("%c %d ",&c,&next);
			i=(c=='O'?1:0);
			int moveTime=abs(next-prev[i]);
			int waitTime=max(0,time-totTime[i]-moveTime);
			int toGo=moveTime+waitTime;
			totTime[i]+=toGo+1;
			time=totTime[i];
			prev[i]=next;
		//	printf("total Time= %d\n",totTime[i]);
		}
		printf("Case #%d: %d\n",test,time-1);

	}
}
