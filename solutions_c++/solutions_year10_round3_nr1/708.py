#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas = 1,sum,i,j,T,n,a[1002],b[1002];
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i = 0;i < n;i ++){
			scanf("%d%d",&a[i],&b[i]);
		}
		sum = 0;
		for(i = 0;i < n;i ++){
			for(j = i+1;j < n;j ++){
				if(a[i] > a[j] && b[j] > b[i]){
					sum ++;
				}
				if(a[i] < a[j] && b[i] > b[j]){
					sum ++;
				}
			}
		}
		printf("Case #%d: %d\n",cas++,sum);
	}
	return 0;
}