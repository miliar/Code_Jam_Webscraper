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
const int maxn=201;
int n,k;
int a[maxn][maxn];
bool g[maxn][maxn];
bool v[maxn];
int match[maxn];

void init(){
	scanf("%d%d",&n,&k);
	for (int i=0;i<n;i++){
		for (int j=0;j<k;j++){
			scanf("%d",&a[i][j]);
		}
	}
	return;
}

bool check(int x,int y){
	int cur=0;
	for (int i=0;i<k;i++){
		if (a[x][i]<=a[y][i]){
			break;
		}
		cur++;
	}
	if (cur>=k){
		return true;
	} else {
		return false;
	}
}

void buildgraph(){
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			g[i][j]=check(i,j);
		}
	}
	return;
}

bool dfs(int k){
	v[k]=true;
	for (int i=0;i<n;i++){
		if (!g[k][i]){
			continue;
		}
		if (match[i]!=-1){
			if (!v[match[i]]&&dfs(match[i])){
				match[i]=k;
				return true;
			}
		} else {
			match[i]=k;
			return true;
		}
	}
	return false;
}

int getans(){
	int ans=n;
	memset(match,0xff,sizeof(match));
	for (int i=0;i<n;i++){
		memset(v,false,sizeof(v));
		if (dfs(i)){
			ans--;
		}
	}
	return ans;
}

int main(){
	int t;
	scanf("%d",&t);
	for (int k=1;k<=t;k++){
		init();
		buildgraph();
		printf("Case #%d: %d\n",k,getans());
	}
	return 0;
}

