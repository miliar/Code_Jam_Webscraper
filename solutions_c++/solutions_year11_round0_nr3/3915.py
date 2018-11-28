#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;
int main(){
	int cas;
	scanf("%d",&cas);
	for (int i=1;i<=cas;i++){
		printf("Case #%d: ",i);
		int num;
		scanf("%d",&num);
		int sum=0;
		int xsum=0;
		int lit = 10000000;
		int dat;
		while(num--){
			scanf("%d",&dat);
			sum+=dat;
			xsum^=dat;
			lit= min(lit,dat);
		}
		//printf("sum:%d little:%d\n",sum,little);
		xsum?printf("NO\n"):printf("%d\n",sum-little);
	}
	return 0;
}
