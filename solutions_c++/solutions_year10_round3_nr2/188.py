#include <cstdio>

int main() {

	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
		long long L,C,P;
		scanf("%lld %lld %lld",&L,&P,&C);

		int numVals = 0;
		long long start = L;
		long long end = P;

		//work our way up
		while(start < end) {
			start *= C;
			numVals++;
		}

		int answer = 0;
		while(numVals>1) {
			if(numVals%2!=0) {
				numVals /= 2;
				numVals++;
			} else {
				numVals /=2;
			}
			answer++;
		}

		printf("Case #%d: %d\n",caseNum,answer);
	}

	return 0;
}
