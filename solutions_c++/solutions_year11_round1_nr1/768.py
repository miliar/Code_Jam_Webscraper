#include <stdio.h>
#include <string.h>

long long N,pg,pd;

long long GCD(long long a,long long b) {
	if(b == 0)	return a;
	return GCD(b,a%b);
}

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%I64d%I64d%I64d",&N,&pd,&pg);
		
		printf("Case #%d: ",++c);
		if(pg == 100) {
			if(pd == 100)
				puts("Possible");
			else
				puts("Broken");
		} else if(pg == 0) {
            if(pd == 0) {
                puts("Possible");   
            } else {
                puts("Broken");
            }
        } else {
            if(pd == 0) {
                if(pg == 0)
                    puts("Possible");
                else
                    puts("Broken");
            } else {
    			long long gcd = GCD(pd,100);
    			long long k = 100/gcd;
    			//printf("%I64d\n",gcd);
	   	        if(k <= N)
				    puts("Possible");
    			else
	       			puts("Broken");
            }
		}
		
	}
	
	return 0;
}
