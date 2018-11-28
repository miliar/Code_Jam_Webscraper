#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main(){
	int i,j,k,h,t,n;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		k=0;
		for(i=1;i<=n;i++){
			scanf("%d",&j);
			if(j!=i)k++;
		}
		printf("Case #%d: %.6lf\n",h,k+0.0);
	}
	return 0;
}
