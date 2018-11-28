#include <cstdio>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>

using namespace std;

const int maxl = 26;
const int maxn = 1000000;

int combine[maxl][maxl];
set<int> oppo[maxl];
int stack[maxn];
map<int, int> rec;

void solve() {
	memset(combine, 255, sizeof(int) * maxl * maxl);
	//memset(oppo, 255, sizeof(int) * maxl);
	for (int i = 0; i < maxl; i++)
		oppo[i].clear();
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char c1, c2, c3;
		scanf(" %c %c %c", &c1, &c2, &c3);
		c1 = toupper(c1);
		c2 = toupper(c2);
		c3 = toupper(c3);
		assert(isalpha(c1) && isalpha(c2) && isalpha(c3));
		assert(combine[c1 - 'A'][c2 - 'A'] == -1);
		combine[c1 - 'A'][c2 - 'A'] = combine[c2 - 'A'][c1 - 'A'] = c3 - 'A';
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char c1, c2;
		scanf(" %c %c", &c1, &c2);
		c1 = toupper(c1);
		c2 = toupper(c2);
		assert(isalpha(c1) && isalpha(c2));
		//assert(oppo[c1 - 'A'] == -1 && oppo[c2 - 'A'] == -1);
		//oppo[c1 - 'A'] = c2 - 'A';
		//oppo[c2 - 'A'] = c1 - 'A';
		oppo[c1 - 'A'].insert(c2 - 'A');
		oppo[c2 - 'A'].insert(c1 - 'A');
	}
	scanf("%d", &n);
	int top = -1;
	rec.clear();
	for (int i = 0; i < n; i++) {
		char c;
		scanf(" %c", &c);
		c = toupper(c);
		assert(isalpha(c));
		int d = c - 'A';
		if (top >= 0 && combine[stack[top]][d] != -1) {
			if (--rec[stack[top]] == 0) rec.erase(stack[top]);
			stack[top] = combine[stack[top]][d];
			rec[d = stack[top]]++;
		} else {
			stack[++top] = d;
			rec[d]++;
		}
		for (set<int>::iterator itr = oppo[d].begin(); itr != oppo[d].end(); itr++)
			if (rec.find(*itr) != rec.end()) {
				top = -1;
				rec.clear();
				break;
			}
	}
	printf("[");
	if (top >= 0) printf("%c", stack[0] + 'A');
	for (int i = 1; i <= top; i++)
		printf(", %c", stack[i] + 'A');
	printf("]\n");
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}