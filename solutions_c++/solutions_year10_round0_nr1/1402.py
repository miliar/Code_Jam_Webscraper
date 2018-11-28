#include <stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	for (int caseID = 1; caseID <= T; ++caseID){
		int N, K;
		scanf("%d %d",&N,&K);
		printf("Case #%d: ", caseID);
		int gap = K - (1<<N) + 1;
		if (gap < 0) {
			printf("OFF\n");
			continue;
		}
		if ((gap%(1<<N)) == 0) printf("ON\n");
		else printf("OFF\n");
		
	}
	return 0;
}