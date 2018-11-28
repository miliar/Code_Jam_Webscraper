#include <iostream>
#include <stdio.h>

int main()
{
	int t,n,s,p,x,count;

	scanf("%d",&t);
	for(int i = 1 ; i <= t ; i++){
		scanf("%d %d %d",&n,&s,&p);
		count = 0;
		while(n--){
			scanf("%d",&x);
			if(p*3 < x || (p*3 - x) <= 2){
				count++;
			}
			else if(s > 0 && x > 0 && ((p*3 - x) <= 4)){
				count++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}

