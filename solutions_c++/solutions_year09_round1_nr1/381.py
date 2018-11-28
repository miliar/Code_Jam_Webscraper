#include <cstdio>
#include <memory>
#include <iostream>

using namespace std;

const int maxn = 20000000;
const int maxm = 1 << 9;

int tmp, sum, remain, tmp2;
int ans[11];
int final[maxm];
int yes[maxn][11];

inline bool check(int nownum, int & base) {
	if (yes[nownum][base] != -1)
		if (yes[nownum][base] != -2) return yes[nownum][base];
		else {
			yes[nownum][base] = 0; return false;
		}
	yes[nownum][base] = -2;
	sum = 0; tmp2 = nownum;
	while (tmp2) {
		tmp = tmp2 % base;
		sum += tmp * tmp;
		tmp2 /= base;
	}
	yes[nownum][base] = check(sum, base);
	return yes[nownum][base];
}

inline void process() {
	memset(ans, 255, sizeof ans);
	memset(yes, 255, sizeof yes);
	for (int i = 2; i <= 10; ++i) yes[1][i] = 1;
	memset(final, 255, sizeof final);
	remain = maxm;	
	for (int num = 2; num < maxn && remain; ++num) {
		if (num % 10000 == 0) cerr << num << endl;
		if (num == 13) {
			num = ((num << 1) + 1) / 2;
		}
		int j = 0;
		for (int i = 2; i <= 10; ++i)
			if (check(num, i)) {
				ans[i] = num;
				j += 1 << (i - 2);
			}
		for (int i = 0; i < maxm; ++i) if ((i & j) == i)
			if (final[i] == -1) {
				final[i] = num; --remain;
			}
	}
}

inline void print() {
	//for (int i = 2; i <= 10; ++i) printf("base: %d\tans: %d\n", i, ans[i]);
	
	for (int i = 0; i < maxm; ++i) printf("%d, \n", final[i]);
}

int main() {
	freopen("out.txt", "w", stdout);

	process();
	print();

	return 0;
}
