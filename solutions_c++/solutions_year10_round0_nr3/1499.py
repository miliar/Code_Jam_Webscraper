#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

#define MAXG 1001

int T, R, K, N, nCase=1;
int G[MAXG];
long long head[MAXG], earn[MAXG];
int series, ptr, nextPtr;
long long cnt, total;

int nextGroups(int p){
	int pt=(p+1)%N;
	cnt=G[p];
	while(cnt+G[pt]<=K && pt!=p){
		cnt += G[pt];
		pt = (pt+1)%N;
	}
	return pt;
}

int main()
{
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d%d", &R, &K, &N);
		for(int i=0;i<N;i++) scanf("%d", &G[i]);
		memset(head, 0, sizeof head);
		memset(earn, 0, sizeof earn);
		series = 1; ptr = 0; total = 0;
		do{
			head[ptr] = series++;
			ptr = nextGroups(ptr);
			total += cnt;
			if(head[ptr]) break;
			earn[ptr] = total;
//			ptr = nextPtr;
		}while(head[ptr]==0);
/*
	    printf("head(earn) with series  : %d(%d), %d\n", ptr, total, series);
		for(int i=0;i<N;i++)
		    printf("%d(%d) : \n", head[i], earn[i]);
		printf("\n");
//*/
		long long loopEarn = total - earn[ptr], loopLength = series-head[ptr];
		long long nLoop = (R-head[ptr])/loopLength;
		long long nEarn = nLoop*loopEarn;
		
//		printf("Loop : n=%d, l=%d, e=%d; totalEarn=%d\n", nLoop, loopLength, loopEarn, nEarn);
		
		total = earn[ptr]+nEarn;
		series = head[ptr]+nLoop*loopLength;
		while(series <= R){
			series++;
			ptr = nextGroups(ptr);
			total += cnt;
		}
		printf("Case #%d: ", nCase++);
		cout<<total<<endl;
	}
    return 0;
}


