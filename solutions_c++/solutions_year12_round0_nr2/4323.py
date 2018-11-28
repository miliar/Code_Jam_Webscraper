#include <stdio.h>

int main(){
	int t=0, count = 0, n=0, s=0, p=0; 
	int out=0,number=0;

	scanf("%d\n",&t);

	while(count<t){
		out=0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);

		for(int j=0;j<n;j++) {
			scanf("%d",&number);
			if (p==0)out++;
			else if (p==1 && number>0)out++;
			else if (p==1 && number==0);
			else if (number<3*p-4);		//5 -> number lower than 11 has no chance (5 3 2 - this will never happen)
			else if(number>3*p-3)out++;	//5 -> number higher than 12 (13,14,,15,....) is automatically added (5 4 4 =13  5 5 4 =14 ...)  , 2-> 4 is added
			else if (s>0){	//there are some surprising that can be used yet  , there are two numbers that arent processed yet 5 -> 11 and 12  , 2->2 and 3
							//number is 3*p-4 or 3*p-3
				out++;	//the number is added, 
				s--;	//but there are one less surprising occurencies possible
			}
		}
		printf("Case #%d: %d\n",count+1,out);
		count++;
	}

	return 0;
}