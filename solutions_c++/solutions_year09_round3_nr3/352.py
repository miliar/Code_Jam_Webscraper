#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <stdlib.h>

using namespace std;

#define inf 100000000

int arr[150] , dp[105][105] , l;

int recur(int i , int j){
	if(i+1 == j) return 0;
	if(dp[i][j] != -1) return dp[i][j];

	int ret = inf , k , tmp;
	for(k = i+1;k<j;k++){
		tmp = recur(i , k)+recur(k , j)+(arr[k]-arr[i]-1)+(arr[j]-arr[k]-1);
		if(tmp < ret) ret = tmp;
	}
	return dp[i][j] = ret;
}

int main(){ 
	//freopen("c-small.in" , "rt" , stdin);
	//freopen("c-small.out" , "wt" , stdout);
	freopen("c-large.in" , "rt" , stdin);
	freopen("c-large.out" , "wt" , stdout);
	int tst , n , i , kase = 1;
	scanf("%d" , &tst);
	while(tst--){
		scanf("%d %d" , &n , &l);
		arr[0] = 0;
		for(i = 1;i<=l;i++)
			scanf("%d" , &arr[i]);
		arr[i] = n+1;
		l++;
		sort(arr , arr+l+1);
		memset(dp , -1 , sizeof(dp));
		int ret = recur(0 , l);
		printf("Case #%d: %d\n" , kase++ , ret);
	}
	return 0;
}

