#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

void run(int casen) {
	long n=0;
	int pd,pg;
	int nmin=0;
	int i=1;
	n=0;pd=0;pg=0;
	scanf("%d",&n);
	scanf("%d",&pd);
	scanf("%d",&pg);
	
	if(pg==0 &&pd!=0 ){
		printf("Case #%d: Broken\n",casen);
		return ;
	}
	if(pg==100 &&pd!=100 ){
		printf("Case #%d: Broken\n",casen);
		return ;
	}
	if(n>=100){
	printf("Case #%d: Possible\n",casen);
	return ;
	}
	
	for(i=1;i<=n;i++){
		if(100%i==0){
			nmin=100/i;
			
			if(pd%nmin==0){
				printf("Case #%d: Possible\n",casen);
				return ;
			}
		}
		
	}
	
		printf("Case #%d: Broken\n",casen);
	
	
}

int main(int argc, char* argv[]) {
	int ncases=0;
	freopen(argv[1], "rt", stdin);
	freopen("A.out", "wt", stdout);
	scanf("%d",&ncases); 
	for(int i=1;i<=ncases;i++) 
	run(i);
	
	return 0;
}
