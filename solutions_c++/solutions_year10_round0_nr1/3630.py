#include <iostream>
#include <sstream>
#include <math.h>


int main(int argc, char **argv) {
	//freopen("input.snapper","r",stdin);
	//freopen("out.snapper","w",stdout);
	int t; //Number of test cases
	int n; //Number of snapper
	int k; //Number of finger snapped
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d %d",&n,&k);
		if(k==0){
			printf("Case #%d: OFF\n",i);
			continue;
		}
		int devideBy=(int)pow(2,n);
		int rem=k%devideBy;
		if(rem==(devideBy-1)){
			printf("Case #%d: ON\n",i);
		}else{
			printf("Case #%d: OFF\n",i);
		}
	}
}

