#include <cstdio>
#include <vector>
using namespace std;

int t, it, maj[1000], i, r, cap, n, occur[1000], bidon, begin, earn, times;

void print(vector<int>& in) {
	for(int i = 0; i < in.size(); ++i) {
		printf("%d ", in[i]);
	} putchar('\n');
}

int main() {
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		printf("Case #%d: ", it);
		scanf("%d%d%d", &r, &cap, &n);
		for(i = 0; i < n; scanf("%d", maj + i++));

		for(earn = i = times = 0; times < r; ++times) {
			bidon = 0;
			begin = i;
			do {
				bidon += maj[i];
				if(++i == n) { i = 0; }
				if(i == begin) { break; }
			} while(bidon + maj[i] <= cap);
			earn += bidon;
		}
		printf("%d\n", earn);
	}
	return 0; }
