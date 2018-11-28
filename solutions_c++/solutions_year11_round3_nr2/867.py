/*
ID: amir.ho1
LANG: C++
TASK: test
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

int n,a[10001];
double dp[10001][5];

int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);	
	int ti,tc,l,t,c,i,j;

	scanf("%d",&tc);
	for (ti=1;ti<=tc;ti++){
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for (i=0;i<c;i++)
			scanf("%d",&a[i]);
		for (i=c;i<n;i++)
			a[i]=a[i%c];
		memset(dp,63,sizeof dp);
		for (i=0;i<5;i++)
			for (j=0;j<10001;j++)
				dp[j][i]=1e9;
		dp[0][l]=0;
		for (i=1;i<=n;i++){
			for (j=0;j<=l;j++){
				dp[i][j]=dp[i-1][j]+2*a[i-1];
				if (dp[i-1][j+1]>=t)
					dp[i][j]=min(dp[i][j],dp[i-1][j+1]+a[i-1]);
				else if (dp[i-1][j+1]+2*a[i-1]>t){
					dp[i][j]=min(dp[i][j],dp[i-1][j+1]+a[i-1]+(t-dp[i-1][j+1])/2);
				}
			}
		}
		int r=dp[n][0];
		for (i=1;i<=l;i++)
			if (dp[n][i]<r)
				r=dp[n][i];
		printf("Case #%d: %d\n",ti,r);
	}
	return 0;
}