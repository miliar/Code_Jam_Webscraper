#include <stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		long long n;
		int d,g;
		scanf("%lld%d%d",&n,&d,&g);
		int poss = 0;
		for(int i = 1;i <= n && i <= 100;i ++){
			for(int j = i ;j <= 20000;j ++) {
				if((d*i)%100 == 0 && (g*j)%100 == 0){
					int t1 = d*i/100;
					int t2 = g*j/100;
					if(t1 > t2) continue;
					t1 = i - d*i/100;
					t2 = j - g*j/100;
					if(t1 > t2) continue;

					poss = 1;
				}
			}
		}
		if(poss){
			printf("Case #%d: Possible\n",testcase);
		}else{
			printf("Case #%d: Broken\n",testcase);
		}
	}
	return 0;
}
