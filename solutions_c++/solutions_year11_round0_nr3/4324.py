#include <cstdio>

int maxValue = 0;

void recurse(int elements[], int size, int valueTaken, int countTaken, int xorTaken, int xorNotTaken, int curPos) {
	if(curPos == size) {
		if(countTaken < size && xorTaken == xorNotTaken) {
			maxValue = valueTaken > maxValue ? valueTaken : maxValue;
		}
		return;
	}

	// Take
	recurse(elements, size, valueTaken + elements[curPos], countTaken + 1, xorTaken ^ elements[curPos], xorNotTaken, curPos+1);
	// Not take
	recurse(elements, size, valueTaken, countTaken, xorTaken, xorNotTaken  ^ elements[curPos], curPos+1);

	return;
}



int main(int argc, char **argv) {
	int n;
	int e[20];
	scanf("%d", &n);

	for(int cs=1;cs<=n;cs++) {
		int N = 0;
		scanf("%d", &N);
		int xorv = 0;
		for(int in = 0;in < N; in++) {
			scanf("%d", &e[in]);
			xorv = xorv ^ e[in];
		}

		if(xorv != 0) {
			printf("Case #%d: NO\n", cs);
			continue;
		}

		maxValue = -1;
		recurse(e, N, 0, 0, 0, 0, 0);
		printf("Case #%d: %d\n", cs, maxValue);
	}
	return 0;
}

