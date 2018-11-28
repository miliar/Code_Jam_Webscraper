#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int tree[1 << 21];
int table[1000001];

void add(int pos, int value) {
	int now = pos + (1 << 20);
	while (now != 0) {
		tree[now] += value;
		now >>= 1;
	}
}

int findpos(int pos) {
	int now = 1;
	while (now < (1 << 20)) {
		if (tree[now * 2] >= pos) {
			now = now * 2;
		} else {
			pos -= tree[now * 2];
			now = now * 2 + 1;
		}
	}
	return now - (1 << 20);
}

int sum(int pos) { // get [1..pos]
	int ret = 0;
	int now = pos + (1 << 20);
	while (now != 0) {
		if (now % 2 == 0) {
			ret += tree[now];
			now--;
		}
		now /= 2;
	}
	return ret;
}

int main() {
	int T;
	int K, N;
	scanf("%d", &T);
	
	for (int cn = 1; cn <= T; ++cn) {
		memset(tree, 0, sizeof(tree));
		memset(table, -1, sizeof(table));

		scanf("%d", &K);
		for (int i = 0; i < K; ++i)
			add(i, 1);

		int last = 0, target;
		for (int i = 1; i <= K; ++i) {
			add(last, -1);
			table[last] = i;

			if (i == K) break;

			int s = sum(last);
			int step = (i + 1) % (K - i);
			if (s + step > (K - i)) {
				target = s + step - (K - i);
			} else {
				target = s + step;
				if (target == 0) target = K - i;
			}

			last = findpos(target);

		}

		scanf("%d", &N);
		vector <int> a(N);

		printf("Case #%d:", cn);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &a[i]);
			printf(" %d", table[a[i] - 1]);
		}
		printf("\n");
	}
}

