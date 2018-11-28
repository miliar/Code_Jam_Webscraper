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
const __int64 maxn=1001;
__int64 p,k,l;
bool v[maxn][maxn];
__int64 a[maxn];

void init(){
	scanf("%I64d%I64d%I64d",&p,&k,&l);
	for (__int64 i=1;i<=l;i++){
		scanf("%I64d",&a[i]);
	}
	sort(a+1,a+1+l);
	return;
}

void process(){
	__int64 ans=0;
	memset(v,false,sizeof(v));
	for (__int64 i=l;i>=1;i--){
		if (a[i]==0){
			break;
		}
		bool flag=false;
		for (__int64 j=1;j<=p;j++){
			for (__int64 key=1;key<=k;key++){
				if (!v[key][j]){
					flag=true;
					ans+=j*a[i];
					v[key][j]=true;
					break;
				}
			}
			if (flag){
				break;
			}
		}
		if (!flag){
			puts("Impossible");
			return;
		}
	}
	printf("%I64d\n",ans);
	return;
}

int main(){
	__int64 t;
	scanf("%I64d",&t);
	for (__int64 cse=1;cse<=t;cse++){
		init();
		printf("Case #%I64d: ",cse);
		process();
	}
	return 0;
}
