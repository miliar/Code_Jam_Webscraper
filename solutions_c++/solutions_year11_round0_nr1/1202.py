
#include "cstdio"
#include "cmath"


int main(int argc, char *argv[]) {
  freopen(argv[1], "r", stdin);

	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		int n;
		scanf("%d", &n);

		int timeO = 0;
		int posO = 1;
		int timeB = 0;
		int posB = 1;
		for (int i = 0; i < n; i++) {
			char c[10];
			int pos;
			scanf("%s %d", c, &pos);
			//printf("%s %d\n", c, pos);

			if (c[0] == 'O') {
				timeO += abs(pos - posO); //go
				posO = pos;
				if (timeB > timeO) timeO = timeB;
				timeO++; //push
			}
			if (c[0] == 'B') {
				timeB += abs(pos - posB); //go
				posB = pos;
				if (timeO > timeB) timeB = timeO;
				timeB++; //push
			}
		}

		int sol;
		if (timeO > timeB) {
			sol = timeO;
		} else {
			sol = timeB;
		}

		printf("Case #%d: %d\n", ti, sol);

	}


	return 0;
}





