#include<stdio.h>
#include<vector>
#include<string>

using namespace std;

int main(){
	int T, tc = 1, PG, PD, N;
	for(scanf("%d ", &T); T; T--){
		printf("Case #%d: ", tc++);
		scanf("%d %d %d ", &N,&PD,&PG);
		if(PD != 100 && PG == 100){
			printf("Broken\n");
			continue;
		}
		else if(PD == 100 && PG == 100){
			printf("Possible\n");
			continue;
		}
		else if(PD < 100 && PD > 0 && N == 1){
			printf("Broken\n");
			continue;
		}
		else if(PG == 0 && PD != 0){
			printf("Broken\n");
			continue;
		}
		int flag = 0;
		if(N < 100){
			for(int i = 1; i <= N; i++){
				if((i*PD) % 100 == 0){
					printf("Possible\n");
					flag = 1;
					break;
				}
			}
			if(flag == 0) printf("Broken\n");
		}
		else
			printf("Possible\n");
		

	}
	return 0;
}
