#include <stdio.h>
#include <memory.h>
#include <assert.h>

int data[1001];
bool flag[1001];

int T;
int R, k, N;

int first_round = 0;
long long first_money = 0;
int period_round = 0;
long long period_money = 0;
int index = 0;

void init()
{
	first_round = 0;
	first_money = 0;
	period_round = 0;
	period_money = 0;
	index = 0;

	memset(flag, 0, sizeof flag);
	int i = 0;
	do {
		flag[i] = true;
		int r = 0;
		while (r + data[i] <= k) {
			r += data[i];
			i = (i + 1) % N;
		}
		first_money += r;
		first_round++;
	} while (!flag[i]);

	index = i;
	
	do {
		int r = 0;
		while (r + data[i] <= k) {
			r += data[i];
			i = (i + 1) % N;
		}
		period_money += r;
		period_round++;
	} while (i != index);

	assert(period_round <= first_round);
}

int main()
{
	scanf(" %d", &T);
	for (int _ = 1; _ <= T; _++) {
		scanf(" %d %d %d", &R, &k, &N);
		long long total = 0;
		for (int i = 0; i < N; i++) {
			scanf(" %d", data + i);
			total += data[i];
		}
		if (total <= k)
			printf("Case #%d: %lld\n", _, total * R);
		else {
			init();
			long long money = 0;
			int i = 0;
			if (R >= first_round) {
				money += first_money;
				R -= first_round;
				i = index;
			}
			if (R >= period_round) {
				money += period_money * (R / period_round);
				R -= (R / period_round) * period_round;
			}
			while (R--) {
				int r = 0;
				while (r + data[i] <= k) {
					r += data[i];
					i = (i + 1) % N;
				}
				money += r;
			}
			printf("Case #%d: %lld\n", _, money);
		}
	}
	return 0;
}

