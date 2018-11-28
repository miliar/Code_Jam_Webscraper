#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const int maxn=110;
int a[maxn][maxn];
int n;

void init(){
	memset(a,0,sizeof(a));
	scanf("%d",&n);
	for (int k=1;k<=n;k++){
		int x1,x2,y1,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for (int i=x1-1;i<x2;i++){
			for (int j=y1-1;j<y2;j++){
				a[i][j]=1;
			}
		}
	}
	return;
}

bool outside(int x,int y){
	return x<0||y<0;
}

int simu(){
	int ans=0;
	while (1){
		ans++;
		int cur[maxn][maxn];
		memset(cur,0,sizeof(cur));
		int s=0;
		for (int i=0;i<100;i++){
			for (int j=0;j<100;j++){
				int tmp=0;
				if (!outside(i,j)){
					tmp+=a[i][j];
				}
				if (!outside(i-1,j)){
					tmp+=a[i-1][j];
				}
				if (!outside(i,j-1)){
					tmp+=a[i][j-1];
				}
				if (tmp>=2){
					cur[i][j]=1;
				} else {
					cur[i][j]=0;
				}
				s+=cur[i][j];
			}
		}
		if (s==0){
			break;
		}
		memcpy(a,cur,sizeof(a));
	}
	return ans;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int k=1;k<=cse;k++){
		init();
		printf("Case #%d: %d\n",k,simu());
	}	
	return 0;
}
