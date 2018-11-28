/*
 * File:   main.cpp
 * Author: Ryan
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX 105

int N; // number of team
bool surprisable[MAX];
bool fullfil[MAX][2];
// fullfil[i][0] for not surprisable
// fullfil[i][1] for surprisable

int max_fullfil_cnt;

/**
 *
 * @param depth increasing
 * @param surprising_seat decreasing
 * @param fullfil_cnt increasing
 */
void walk(int depth, int surprising_seat, int fullfil_cnt)
{
	if (depth >= N) {
		if (0 == surprising_seat && max_fullfil_cnt < fullfil_cnt)
			max_fullfil_cnt = fullfil_cnt;
		return;
	}

	if (surprisable[depth] && surprising_seat >= 0) {
		// assign this team as surprising
		if (fullfil[depth][1])
			walk(depth+1, surprising_seat-1, fullfil_cnt+1);
		else
			walk(depth+1, surprising_seat-1, fullfil_cnt);
	}

	// assign this team as not suprising
	if (fullfil[depth][0])
		walk(depth+1, surprising_seat, fullfil_cnt+1);
	else
		walk(depth+1, surprising_seat, fullfil_cnt);
}

int main()
{
	int kase, serial=1,
		s, // number of surprising team
		p, // threshold from input
		sum,
		a;

	scanf("%d", &kase);
	while (kase--) {
		scanf("%d %d %d", &N, &s, &p);

		for (int i=0; i<N; ++i) {
			scanf("%d", &sum);
//			printf("Team %d (%d): ", i, sum);
			switch (sum % 3) {
				case 0:
					// surprising: sum = a + a+1 + a+2 = 3a+3 = 3(a+1)
					a = sum / 3 - 1;
					if (a >= 0) {
//						printf(" +(%d %d %d)", a, a+1, a+2);
						surprisable[i] = true;
						fullfil[i][1] = (a+2 >= p);
					} else {
						surprisable[i] = false;
					}

					// not surprising: sum = a + a + a = 3a
					a = sum / 3;
//					printf(" -(%d %d %d)", a, a, a);
					fullfil[i][0] = (a >= p);
					break;

				case 1:
					// surprising: sum = a + a+2 + a+2 = 3a+4 = 3(a+1) + 1
					a = (sum - 1) / 3 - 1;
					if (a >= 0) {
//						printf(" +(%d %d %d)", a, a+2, a+2);
						surprisable[i] = true;
						fullfil[i][1] = (a+2 >= p);
					} else {
						surprisable[i] = false;
					}

					// not surprising: sum = a + a + a+1 = 3a+1
					a = (sum - 1) / 3;
//					printf(" -(%d %d %d)", a, a, a+1);
					fullfil[i][0] = (a+1 >= p);
					break;

				case 2:
					// surprising: sum = a + a + a+2 = 3a + 2
					a = (sum - 2) / 3;
//					printf(" +(%d %d %d)", a, a, a+2);
					surprisable[i] = true;
					fullfil[i][1] = (a+2 >= p);


					// not surprising: sum = a + a+1 + a+1 = 3a+2
					a = (sum - 2) / 3;
//					printf(" -(%d %d %d)", a, a+1, a+1);
					fullfil[i][0] = (a+1 >= p);
					break;
			}
//			puts("");
		}

		max_fullfil_cnt = 0;
		walk(0, s, 0);
		printf("Case #%d: %d\n", serial++, max_fullfil_cnt);
	}

	return 0;
}
