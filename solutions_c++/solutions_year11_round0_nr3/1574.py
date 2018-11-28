#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxt=1050000;
const int maxn=1001;
int f[2][maxt];
int a[maxn];
int n;

void init(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	return;
}

void dp(){
	memset(f,0xff,sizeof(f));
	int cur=1;
	int last=0;
	f[last][0]=0;
	int mask=0;
	for (int i=1;i<=n;i++){
		mask^=a[i];
		for (int j=0;j<=1048575;j++){
			f[cur][j]=max(f[last][j],(f[last][j^a[i]]==-1)?(-1):(f[last][j^a[i]]+a[i]));
		}
		swap(cur,last);
	}
	int best=-1;
	for (int i=1;i<=1048575;i++){
		if ((i^mask)==i){
			best=max(best,f[last][i]);
		}
	}
	if (best==-1){
		printf("NO\n");
	} else {
		printf("%d\n",best);
	}
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		dp();
	}
	
	return 0;
}
