#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int i,j,k,cases,_case;
char seq[100000];
char n[100000];
int len;
vector<int> p;

int main() {
	scanf("%d", &cases);
	for (_case = 1; _case <= cases; _case++) {
		printf("Case #%d: ", _case);

		scanf("%d%*c", &k);
		scanf("%s", seq);
		len = strlen(seq);

		p.clear();
		for (i = 0; i < k; i++) {
			p.push_back(i);
		}

		int best = 12345678;
		do {
			for (i = 0; i < len; i++) {
				n[i] = seq[((i/k) * k) + p[i % k]];
			}
			char prev;
			prev = ' ';
			int cnt = 0;
			for (i = 0; i < len; i++) {
				if (n[i] != prev) {
					cnt++;
				}
				prev = n[i];
			}
			if (cnt < best) best = cnt;
		} while (next_permutation(p.begin(), p.end()));

		printf("%d\n", best);
	}
	return 0;
}

