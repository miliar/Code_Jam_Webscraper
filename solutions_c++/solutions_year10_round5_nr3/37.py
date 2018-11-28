#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

vector<int> num;
static const int OFFSET = 1000000+200000;


int main(void) {
	int testNum;
	// cin >> testNum;
	scanf("%d", &testNum);
	for (int testNo = 1; testNo <= testNum; testNo++) {
		num.assign(OFFSET * 2, 0);
		int c;
		for (scanf("%d", &c); c--; ) {
			int p, v;
			scanf("%d%d", &p, &v);
			num[p + OFFSET] = v;
		}
		long long res = 0;
		int lastEmpty = 0;
		for (int pos = lastEmpty + 1; pos != 2*OFFSET - 1; pos++) {
			if (num[pos] == 0) {
				num[pos] = lastEmpty - pos;
				lastEmpty = pos;
			} else {
				while (num[pos] > 1) {
					num[pos] -= 1;
					++num[pos + 1];
					res += pos - lastEmpty;
					if (num[lastEmpty + 1] == 1) {
						num[lastEmpty + 1] = num[lastEmpty]-1;
						num[lastEmpty] = 1;
						++lastEmpty;
					} else {
						--num[pos];
						int newLastEmpty = num[lastEmpty] + lastEmpty;
						num[lastEmpty] = 1;
						lastEmpty = newLastEmpty;
					}
				}
				if (num[pos] == 0) {
					num[pos] = lastEmpty - pos;
					lastEmpty = pos;
				}
			}
		}
		printf("Case #%d: %lld\n", testNo, res);
	}
	return 0;
}
