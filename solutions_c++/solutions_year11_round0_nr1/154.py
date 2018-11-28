#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int n;
		scanf("%d", &n);
		int t = 0;
		int cp[2] = {1, 1}, lt[2] = {0, 0};
		while (n--) {
			int pos;
			int c = 0;
			if (scanf(" O %d", &pos) > 0) {
				c = 0;
			} else if (scanf(" B %d", &pos) > 0) {
				c = 1;
			}
			int nt = t + 1;
			int move = abs(cp[c] - pos) + 1;
			if (nt < lt[c] + move) {
				nt = lt[c] + move;
			}
			lt[c] = nt;
			cp[c] = pos;
			t = nt;
		}
		printf("Case #%d: %d\n", Ti, t);
	}
}
