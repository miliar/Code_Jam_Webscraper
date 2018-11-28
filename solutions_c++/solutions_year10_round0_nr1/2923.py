#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	int t,n,k;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d%d",&n,&k);
		printf("Case #%d: O",i);
		int temp=1<<n;
		int kk=k%temp;
		if(kk==temp-1)printf("N\n");
		else printf("FF\n");
	}
	return 0;
}