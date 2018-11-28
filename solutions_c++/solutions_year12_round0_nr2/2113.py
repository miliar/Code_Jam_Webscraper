#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	int testCases,p,n,best,s,total,idealSum,count,inp,surpriseSum;
	scanf("%d",&testCases);
	for(int i =1; i<= testCases; i++){
		count = 0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		idealSum = p * 3 -2;
		surpriseSum = p * 3 -4;
		for(int j = 0; j < n; j++){
			scanf("%d",&inp);
			if(inp >= idealSum){
				count++;
			}
			else if(inp >= surpriseSum && s > 0 && inp >= p){
				count++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}