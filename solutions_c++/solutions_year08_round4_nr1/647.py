#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long

using namespace std;

int type[20000];
int val[20000];
int change[20000];
int dp[20000][4];

#define INF 10000000

int N,R;

int go(int pos, int want) {
	if (change[pos]==2) {
		if (want==val[pos]) return 0;
		return INF;
	}
	int &ans=dp[pos][want];
	if (ans!=-1) return ans;
	if (want==val[pos]) return ans=0;

	int ta=INF;
	ans=INF;
	int left0=go(pos*2,0);
	int right0=go(pos*2+1,0);
	int left1=go(pos*2,1);
	int right1=go(pos*2+1,1);

	// AND
	if (type[pos]==1) {
		if (want==0) {
			ta=min(left0,right0);
		}
		else {
			ta=left1+right1;
			if (change[pos]==1) {
				ta=min(ta,1+left0+right1);
				ta=min(ta,1+left1+right0);
			}
		}
	}
	// OR
	else {
		if (want==0) {
			ta=left0+right0;
			if (change[pos]==1) {
				ta=min(ta,1+left0+right1);
				ta=min(ta,1+left1+right0);
			}
		}
		else {
			ta=min(left1,right1);
		}
	}
	ans=ta;
	return ans;
}

void calc(int pos) {
	if (change[pos]==2) {
		return;
	}
	if (type[pos]==1) {
		if (val[pos*2]==1 && val[pos*2+1]==1)
			val[pos]=1;
		else
			val[pos]=0;
	}
	else {
		if (val[pos*2]==1 || val[pos*2+1]==1)
			val[pos]=1;
		else
			val[pos]=0;
	}
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	int i,j;
	for (t=1; t<=T; t++) {
		memset(dp,-1,sizeof(dp));
		scanf("%d %d", &N, &R);
		j=1;
		for (i=1; i<=(N-1)/2; i++) {
			scanf("%d %d", &type[j], &change[j]);	
			j++;
		}
		for (i=1; i<=(N+1)/2; i++) {
			scanf("%d", &val[j]);
			change[j]=2;
			j++;
		}
		for (i=N; i>=1; i--) {
			calc(i);
		}
		int ans=go(1,R);
		if (ans>=INF) {
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		else {
			printf("Case #%d: %d\n",t,ans);
		}
	}
	return 0;
}
