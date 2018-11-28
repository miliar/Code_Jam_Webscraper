#include<stdio.h>
#include<math.h>
#include<vector>
#include<string.h>
#include<iostream>
using namespace std;

int ok[2100000];

int ans;
int n;
int a[1600];

void dfs(int len,int sum,int cnt){
	if(ok[sum]){
		ans = max(ans,cnt);
	}
	if(len == n)
		return ;

	dfs(len + 1, sum ^ a[len],cnt + a[len]);
	dfs(len + 1, sum,cnt);
}
void prework(){
	int t = 2;
	while(t <= 1000000){
		ok[t-1] = 1;
		t *= 2;
	}
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("1.out","w",stdout);
	//prework();
	int t;
	int cas = 1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		ans = 0;
		int sum = 0;
		int mmin = 100000000;
		for(int i = 0 ; i < n; i ++)
		{
			scanf("%d",&a[i]);
			ans = ans ^ a[i];
			sum += a[i];
			mmin = min(mmin,a[i]);
		}
		printf("Case #%d: ",cas++);
		if(ans != 0){
			printf("NO\n");
			continue;
		}
	//	ans = 0;
	//	dfs(0,0,0);
		printf("%d\n",sum - mmin);
	}
	return 0;
}