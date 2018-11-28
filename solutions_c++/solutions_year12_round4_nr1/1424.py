#include <stdio.h>


typedef struct {
	int position;
	int vine;
} DATA;

DATA queue[100000000];
int data[10010][2];

int main() {
	int t;
	scanf("%d", &t);

	int i;
	for(i = 0; i < t; i++) {
		int n;
		scanf("%d", &n);

		int j;
		for(j = 0; j < n; j++) {
			scanf("%d %d", &data[j][0], &data[j][1]);
		}

		int end;
		scanf("%d", &end);

		queue[0].position = 0;
		queue[0].vine = 0;
		int tail = 0;
		int head = 1;
		while(tail < head) {
			int now = queue[tail].position;
			int index = queue[tail].vine;

			int vine = data[index][0];
			int min = data[index][1];

			if(min > (vine-now)) {
				min = vine-now;
			}

			if((vine+min) >= end) {
				printf("Case #%d: YES\n", i+1);
				break;
			}

			for(j = queue[tail].vine+1; j < n; j++) {
				if(data[j][0] <= (vine+min)) {
					queue[head].position = vine;
					queue[head++].vine = j;

				}
			}

			tail++;
		}

		if(tail == head) {
			printf("Case #%d: NO\n", i+1);
		}
	}

	return 0;
}