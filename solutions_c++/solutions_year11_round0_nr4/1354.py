#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);
	for(int k=1;k<=T;++k){
		double ans=0;
		int n;
		scanf("%d",&n);
		int a[1024],b[1024];
		for(int i=0;i<n;++i){
			scanf("%d",&a[i]);
			b[i]=a[i];
		}
		sort(a,a+n);
		for(int i=0;i<n;++i)
			if(a[i]!=b[i])++ans;
		printf("Case #%d: %.6f\n",k,ans);
	}
	return 0;
}
