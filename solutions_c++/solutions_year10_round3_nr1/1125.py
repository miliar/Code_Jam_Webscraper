#include <stdio.h>
#include <stdlib.h>
int left[10002];
int right[10002];

struct POINT {
	int left;
	int right;
};

typedef struct POINT point;

point p[10002];

int compare (const void * a, const void * b) {
  return ( (*(point *)a).left - (*(point *)b).left );
}


int main(int argc, char *argv[]) {
	int num_of_test;
	int count;
	int n, a, b;
	scanf("%d", &num_of_test);
	for (int z = 1; z <= num_of_test; z++) {
		count = 0;
		scanf("%d", &n);
		for (int i = 1; i <= 10000; i++) {
			left[i] = 0;
			right[i] = 0;
		}
		for (int i = 0; i < n; i++) scanf("%d %d", &p[i].left, &p[i].right);

		qsort (p, n, sizeof(point), compare);

//		for (int i = 0; i < n; i++) printf("%d %d\n", p[i].left, p[i].right);

		for (int i = 0; i < n; i++) {
			left[p[i].left] = i+1;
			right[p[i].right] = i+1;
		}

		for (int i = 1; i <= 10000; i++) {
			if (left[i] == 0) continue;
			for (int j = 1; j <= 10000; j++) {
				if (right[j] == left[i]) break;
				if (left[i] < right[j]) {
					count++;
				}
			}
		}
		printf("Case #%d: %d\n", z, count);
	}
	return 0;
}
