#include <cstdio>

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
		int N,K;
		scanf("%d %d",&N,&K);

		bool lightState = true;

		for(int i=1;i<=N;i++) {
			int cycleLength = (1<<i);
			int pos = K % cycleLength;
			if(pos<(1<<(i-1))) {
				lightState = false;
				break;
			}
		}

		printf("Case #%d: ",caseNum);
		if(lightState) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}

	return 0;
}

