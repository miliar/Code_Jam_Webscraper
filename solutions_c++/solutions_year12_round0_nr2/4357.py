#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
int main() {
	int t,n,s,p,i,j,score,ans;

	scanf("%d",&t);

	for(i=0;i<t;i++){
		ans = 0;

		scanf("%d %d %d",&n,&s,&p);

		for (j=0;j<n;j++){
			scanf("%d",&score);

			if (score == 0 and p ==0){
				ans = ans+1;
			} 

			else if (score >= (3*p) - 2 ){
				ans = ans + 1 ;
			}
			else if (s > 0 && (score > 1) && (score == (3*p)-3 || score == (3*p)-4 )) {
				ans = ans + 1 ;
				s = s-1;
			} 
		}

		printf("Case #%d: %d \n",i+1,ans);
	} 
	return 0;
}