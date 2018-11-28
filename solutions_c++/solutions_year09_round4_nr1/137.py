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
const int maxn=51;
int last[maxn];
int index[maxn];
int n;

void init(){
	scanf("%d",&n);
	char str[maxn];
	for (int i=1;i<=n;i++){
		scanf("%s",str);
		last[i]=0;
		for (int j=n;j>=1;j--){
			if (str[j-1]=='1'){
				last[i]=j;
				break;
			}
		}
		index[i]=i;
	}
	return;
}

int greedy(){
	int ans=0;
	for (int i=1;i<=n;i++){
		int curposi;
		for (int j=i;j<=n;j++){
			if (last[index[j]]<=i){
				curposi=j;
				break;
			}
		}
		for (int j=curposi;j>=i+1;j--){
			swap(index[j],index[j-1]);
			ans++;
		}
	}
	return ans;
}

int main(){
	freopen("a1.in","r",stdin);
	int t;
	scanf("%d",&t);
	for (int k=1;k<=t;k++){
		init();
		printf("Case #%d: %d\n",k,greedy());
	}
	return 0;
}
