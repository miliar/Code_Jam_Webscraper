#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const int maxn=1001;
const int oo=1000000;
int n,ans;
int l[maxn],r[maxn],x[maxn],y[maxn];
int a[maxn][maxn];

void preprocess(){
	for (int i=1;i<=n;i++){
		l[i]=n-i+1;
		r[i]=n+i-1;
	}
	for (int i=n+1;i<=n*2-1;i++){
		l[i]=l[n*2-i];
		r[i]=r[n*2-i];
	}
	return;
}

void init(){
	scanf("%d",&n);
	preprocess();
	memset(a,0,sizeof(a));
	memset(x,0,sizeof(x));
	memset(y,0,sizeof(y));
	for (int i=1;i<=n*2-1;i++){
		for (int j=l[i];j<=r[i];j+=2){
			scanf("%d",&a[i][j]);
		}
	}
	return;
}

int getans(){
	for (int i=1;i<=n*2-1;i++){
		for (int j=1;j<=n*2-1&&!x[i];j++){
			for (int k=l[j];k<i;k+=2){
				if (i*2-k<=r[j]&&a[k][j]!=a[i*2-k][j]){
					x[i]=1;
				}
			}
		}
		for (int j=1;j<=n*2-1&&!y[i];j++){
			for (int k=l[j];k<i;k+=2){
				if (i*2-k<=r[j]&&a[j][k]!=a[j][i*2-k]){
					y[i]=1;
				}
			}
		}
	}
	int ans=oo;
	for (int i=1;i<=n*2-1;i++){
		if (x[i]){
			continue;
		}
		for (int j=1;j<=n*2-1;j++){
			if (y[j]){
				continue;
			}
			ans=min(ans,abs(n-i)+abs(n-j));
		}
	}
	ans=(n+ans)*(n+ans)-n*n;
	return ans;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int k=1;k<=cse;k++){
		init();
		printf("Case #%d: %d\n",k,getans());
	}	
	return 0;
}
