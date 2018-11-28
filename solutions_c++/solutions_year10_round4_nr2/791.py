//============================================================================
// Name        : B.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#define MAXN 1100
#define MAXP 11

int P,N,m[MAXN],tmp,t[MAXP][MAXN];

int DP(int s, int t){
	int i,j,ans=0;
	for(i = s; i <= t; ++i){
		if(m[i] < P){
			++ans;
			for(j = s; j <= t; ++j)
				++m[j];
			break;
		}
	}
	if(!ans)
		return ans;
	else
		return DP(s,(s+t)/2) + DP((s+t)/2+1, t) + 1;
}

int main() {
	int cas,cnt=0,i,j;
	freopen("B-small-attempt0.in", "r", stdin);
	FILE *out;
	out = fopen("output.txt", "w");
	scanf("%d", &cas);
	while(cas--){
		scanf("%d", &P);
		N = 1 << P;
		for(i = 0; i < N; ++i)
			scanf("%d", &m[i]);
		for(i=0,tmp=N>>1; i < P; tmp=tmp>>1,++i)
			for(j = 0; j < tmp; ++j)
				scanf("%d", &t[i][j]);
		fprintf(out, "Case #%d: %d\n", ++cnt, DP(0,N-1));
	}
	fclose(out);
	return 0;
}

