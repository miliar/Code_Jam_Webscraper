// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include"iostream"
#include"algorithm"
using namespace std;
int ans,p,q;
bool hash[200],a[200];
void dfs(int t,int cost)
{
	if(t == q+1){
		if(ans == -1 || cost < ans)
			ans = cost;
		return;
	}
	int i,temp,j;
	for(i=0;i<q;i++){
		if(!hash[i]){
			temp = cost;
			for(j=i-1;j>=0;j--){
				if(hash[j] == 1)
					break;
			}
			if(j < 0)
				temp += a[i]-1;
			else
				temp += a[i]-a[j]-1;
			for(j=i+1;j<q;j++){
				if(hash[j] == 1)
					break;
			}
			if(j >= q)
				temp += p-a[i];
			else
				temp += a[j]-a[i]-1;
			hash[i] = 1;
			dfs(t+1,temp);
			hash[i] = 0;
		}
	}
}

int main()
{
	freopen("G:\\C-small-attempt0.in","r",stdin);
	freopen("G:\\Cout.out","w",stdout);
	int t,ci=1,i;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&p,&q);
		for(i=0;i<q;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+q);
		memset(hash,0,sizeof(hash));
		ans = -1;
		dfs(1,0);
		printf("Case #%d: %d\n",ci++,ans);
	}
	return 0;
}