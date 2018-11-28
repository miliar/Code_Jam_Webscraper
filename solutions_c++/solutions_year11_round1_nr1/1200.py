//GCJ Round 1A: A.Large
#include <cstdio>

int gcd(int x,int y){
	if(y==0) return x;
	return gcd(y,x%y);
}

int main(){
	int t,tt;
	int pd,pg,x,y;
	long long n;
	scanf("%d",&t);
	//t=1;
	for(tt=1;tt<=t;tt++){
		scanf("%I64d%d%d",&n,&pd,&pg);
		printf("Case #%d: ",tt);
		//printf("%d\n",gcd(6,15));
		if(pg == 100){
			if(pd != 100){
				printf("Broken\n");
				continue;
			}
		}else if(pg == 0){
			if(pd != 0){
				printf("Broken\n");
				continue;
			}
		}
		if(n<100){
			x=100/gcd(pd,100);
			if(n<x){//impossible
				printf("Broken\n");
				continue;
			}
		}
		/*y=100/gcd(pg,100);
		if(y<x){//impossible
			printf("Broken\n");
			continue;
		}*/
		printf("Possible\n");
	}
	return 0;
}
