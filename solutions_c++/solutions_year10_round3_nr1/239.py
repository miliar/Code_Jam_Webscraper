#include <cstdio>

int main() {

	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
		int N;
		scanf("%d",&N);

		int wires[1005][2];

		for(int i=0;i<N;i++) {
			scanf("%d %d",&wires[i][0],&wires[i][1]);
		}

		int answer;
		if(N==1) {
			answer = 0;
		} else {
			if((wires[0][0]>wires[1][0]) && (wires[0][1]<wires[1][1])) {
				answer = 1;
			} else if((wires[0][0]<wires[1][0]) && (wires[0][1]>wires[1][1])) {
				answer = 1;
			} else {
				answer = 0;
			}
		}

		printf("Case #%d: %d\n",caseNum,answer);
	}

	return 0;
}
