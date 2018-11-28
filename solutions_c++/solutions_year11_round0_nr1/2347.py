#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <math.h>

void main() {
	int num_cases;
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d ", &num_cases);

	for (int w=0; w<num_cases; w++) {
		int num;
		scanf("%d", &num);
		//printf("num-%d\n", num);

		int excessR=0, excessO=0;
		int prevR=1, prevO=1;
		int nextR, nextO;
		int total=0;

		for (int k=0; k<num; k++) {
			char clr;
			int tmp;
			
			scanf(" %c", &clr);
			scanf("%d", &tmp);
			if (clr == 'B') {
				nextR = tmp;
				int time = (abs(nextR - prevR) - abs(excessR) < 0 ? 0 : abs(nextR - prevR) - abs(excessR)) + 1;
				//printf("%d B\n", time);
				total += time;
				excessR = 0;
				excessO += time;
				prevR = nextR;
			}
			else if (clr == 'O') {
				nextO = tmp;
				int time = (abs(nextO - prevO) - abs(excessO) < 0 ? 0 : abs(nextO - prevO) - abs(excessO)) + 1;
				//printf("%d O\n", time);
				total += time;
				excessO = 0;
				excessR += time;
				prevO = nextO;
			}
		}

		printf("Case #%d: %d\n", w+1, total);
	}

	//system("pause");
}