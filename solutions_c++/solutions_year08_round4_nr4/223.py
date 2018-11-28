#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn=1002;
char str[maxn];
int p[maxn];
bool v[maxn];
int n,k;
int best;
char tmp[maxn];

void init(){
	scanf("%d",&k);
	scanf("%s",str);
	n=strlen(str);
	for (int i=strlen(str);i>=1;i--){
		str[i]=str[i-1];
	}
	return;
}

int count(){
	int cnt=n/k;
	int ans=0;
	for (int i=1;i<=cnt;i++){
		for (int j=1;j<=k;j++){
			tmp[(i-1)*k+j]=str[(i-1)*k+p[j]];
		}
	}
	char last=0;
	for (int j=1;j<=n;j++){
		if (tmp[j]!=last){
			ans++;
			last=tmp[j];
		}
	}
	return ans;
}

void dfs(int dep){
	if (dep>k){
		int t=count();
		if ((best==-1)||(t<best)){
			best=t;
		}
		return;
	}
	for (int i=1;i<=k;i++){
		if (v[i]){
			continue;
		}
		v[i]=true;
		p[dep]=i;
		dfs(dep+1);
		v[i]=false;
	}
	return;
}

int main(){
	int t;
	scanf("%d",&t);
	for (int cse=1;cse<=t;cse++){
		init();
		best=-1;
		memset(v,false,sizeof(v));
		dfs(1);
		printf("Case #%d: %d\n",cse,best);
	}
	return 0;
}
