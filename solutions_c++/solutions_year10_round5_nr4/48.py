#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const int maxn=71;
int n,b,remain,ans;
int f[maxn][maxn];

void init(){
	scanf("%d%d",&n,&b);
	memset(f,0,sizeof(f));
	remain=n;
	ans=0;
	return;
}

void search(int k){
	if (remain==0){
		ans++;
		return;
	}
	for (int i=k+1;i<=remain;i++){
		int flag=0;
		int posi=0;
		for (int j=i;j>0;j/=b){
			if (f[posi][j%b]>0){
				flag=j;
				break;
			}
			posi++;
		}
		if (flag!=0){
			continue;
		}
		posi=0;//try
		for (int j=i;j>0;j/=b){
			f[posi][j%b]++;
			posi++;
		}
		remain-=i;
		search(i);
		remain+=i;
		posi=0;//backup
		for (int j=i;j>0;j/=b){
			f[posi][j%b]--;
			posi++;
		}
	}
	return;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int i=1;i<=cse;i++){
		init();
		search(0);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
