#include <iostream>
using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>

const int T_SIZE = 100;
const int N_SIZE = 100;

int main (void)
{
	int i,j, T, N, P, Pre_O, Pre_B, TOTAL, TIME, dist;
	char c, P_ORDER[N_SIZE];
	int O_BTN [N_SIZE], B_BTN [N_SIZE], o_cnt, b_cnt;

	scanf ("%d", &T);
	for (i = 1; i <= T; i++) {

		printf ("Case #%d: ",i);
		scanf ("%d ", &N);
		for (j = o_cnt = b_cnt = 0; j < N; j++) {
			scanf ("%c %d ", &c, &P);
			if (c == 'O') {
				P_ORDER[j] = 'O';
				O_BTN[o_cnt] = P;
				o_cnt++;
			} else {
				P_ORDER[j] = 'B';
				B_BTN[b_cnt] = P;
				b_cnt++;
			}
		}
		O_BTN[o_cnt] = 0;
		B_BTN[b_cnt] = 0;

		for (j = TOTAL = o_cnt = b_cnt = 0,
			 Pre_O = Pre_B = 1; j < N; j++) {
			switch (P_ORDER[j]) {
			case 'O':
				if (Pre_O <= O_BTN[o_cnt]) {
					TIME = O_BTN[o_cnt] - Pre_O + 1;
				} else {
					TIME = Pre_O - O_BTN[o_cnt] + 1;
				}
				TOTAL += TIME;
				Pre_O = O_BTN[o_cnt];
				if (Pre_B <= B_BTN[b_cnt]) {
					dist = B_BTN[b_cnt] - Pre_B;
				} else {
					dist = Pre_B - B_BTN[b_cnt];
				}
				if (dist >= TIME) {
					Pre_B += (Pre_B <= B_BTN[b_cnt]) ? TIME : -TIME;
				} else {
					Pre_B = B_BTN[b_cnt];
				}
				o_cnt++;
				break;
			case 'B':
				if (Pre_B <= B_BTN[b_cnt]) {
					TIME = B_BTN[b_cnt] - Pre_B + 1;
				} else {
					TIME = Pre_B - B_BTN[b_cnt] + 1;
				}
				TOTAL += TIME;
				Pre_B = B_BTN[b_cnt];
				if (Pre_O <= O_BTN[o_cnt]) {
					dist = O_BTN[o_cnt] - Pre_O;
				} else {
					dist = Pre_O - O_BTN[o_cnt];
				}
				if (dist >= TIME) {
					Pre_O += (Pre_O <= O_BTN[o_cnt]) ? TIME : -TIME;
				} else {
					Pre_O = O_BTN[o_cnt];
				}
				b_cnt++;
				break;
			default: fprintf (stderr, "error\n"); exit (-1);
			}
		}
		printf ("%d\n", TOTAL);
	}

	return 0;
}


