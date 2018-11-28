#include <cstdio>
#include <cstdlib>
#include <cstring>

#define INPUT_BUFFER	(20)
#define INPUT_N			(100)

#undef DEBUG


int compare_0 (const void * a, const void * b) {
	return ( ((int*)a)[0] - ((int*)b)[0]);
}
int compare_1 (const void * a, const void * b) {
	return ( ((int*)a)[1] - ((int*)b)[1]);
}

int main() {
	char in_buf[INPUT_BUFFER];
	gets(in_buf);
	int case_size = atoi(in_buf);
	
#ifdef DEBUG
	printf("%d cases\n", case_size);
#endif

	// each case
	for (int i = 0; i < case_size; i++) {
		gets(in_buf);
		int delay = atoi(in_buf);
		int a[INPUT_N][2];
		int b[INPUT_N][2];
		int a_size = 0, b_size = 0;
		
		gets(in_buf);
		sscanf(in_buf, "%d %d", &a_size, &b_size);

#ifdef DEBUG
		printf("Case #%d, a_size=%d, b_size=%d, delay=%d\n", i + 1, a_size, b_size, delay);
#endif

		for (int j = 0; j < a_size; j++) {
			int leave_hour, leave_minute, arrive_hour, arrive_minute;
			gets(in_buf);
			sscanf(in_buf, "%d:%d %d:%d", &leave_hour, &leave_minute, &arrive_hour, &arrive_minute);
			a[j][0] = leave_hour * 60 + leave_minute;
			a[j][1] = arrive_hour * 60 + arrive_minute + delay;
#ifdef DEBUG
			printf("A(%d) %d:%d %d:%d (%d %d)\n", j, leave_hour, leave_minute, arrive_hour, arrive_minute, a[j][0], a[j][1]);
#endif
		}
		
		for (int j = 0; j < b_size; j++) {
			int leave_hour, leave_minute, arrive_hour, arrive_minute;
			gets(in_buf);
			sscanf(in_buf, "%d:%d %d:%d", &leave_hour, &leave_minute, &arrive_hour, &arrive_minute);
			b[j][0] = leave_hour * 60 + leave_minute;
			b[j][1] = arrive_hour * 60 + arrive_minute + delay;
#ifdef DEBUG
			printf("B(%d) %d:%d %d:%d (%d %d)\n", j, leave_hour, leave_minute, arrive_hour, arrive_minute, b[j][0], b[j][1]);
#endif
		}
		
		int a_needed = a_size, b_needed = b_size;
		
		qsort (a, a_size, sizeof(int) * 2, compare_1);
		qsort (b, b_size, sizeof(int) * 2, compare_0);

		int available = 0, k = 0;
		for (int j = 0; j < a_size; j++) {
#ifdef DEBUG
			printf("a[%d] = %d\n", j, a[j][0]);
#endif
			available++;
			while ((k < b_size) && (b[k][0] < a[j][1])) {
#ifdef DEBUG
				printf("rid of b[%d]\n", k);
#endif
				k++;
			}
			while ((k < b_size) && (b[k][0] >= a[j][1]) && (available > 0)) {
				available--;
#ifdef DEBUG
				printf("reuse for b[%d]\n", k);
#endif
				k++;
				b_needed--;
			}
		}
		
		qsort (a, a_size, sizeof(int) * 2, compare_0);
		qsort (b, b_size, sizeof(int) * 2, compare_1);
		available = 0;
		k = 0;
		for (int j = 0; j < b_size; j++) {
#ifdef DEBUG
			printf("b[%d] = %d\n", j, b[j][0]);
#endif
			available++;
			while ((k < a_size) && (a[k][0] < b[j][1])) {
#ifdef DEBUG
				printf("rid of a[%d]\n", k);
#endif
				k++;
			}
			while ((k < a_size) && (a[k][0] >= b[j][1]) && (available > 0)) {
				available--;
#ifdef DEBUG
				printf("reuse for a[%d]\n", k);
#endif
				k++;
				a_needed--;
			}
		}
		
		//getchar(); // eat char
		
		printf("Case #%d: %d %d\n", i + 1, a_needed, b_needed);
	}
	
	return 0;
}
