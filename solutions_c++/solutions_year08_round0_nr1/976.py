#include <iostream>
#include <string>

using namespace std;

#define MAXQ 1010
#define MAXS 110
#define MAXL 110

typedef pair<int, int> pi;

string searcher[MAXS], query[MAXQ];

int n, s, q;

void read() {
	scanf(" %d", &s);
	char buf[MAXL];
	for (int i = 0; i < s; i++) {
		scanf(" %[^\n]", &buf);
		searcher[i] = buf;
	}
	scanf(" %d", &q);
	for (int i = 0; i < q; i++) {
		scanf(" %[^\n]", &buf);
		query[i] = buf;
	}
}

int take(int st) {
	int chng = -1, h = -1;
	for (int f = 0; f < s; f++) {
		int j = st;
		while (j < q && query[j] != searcher[f]) 
			j++;
		chng = max(chng, j);
	}
	return chng;
}

void solve(int tst) {
	int to = take(0), next = 0;
	while (to < q) {
		to = take(to);
		next++;
	}
	printf("Case #%d: %d\n", tst, next);	
}		

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &n);
	for (int t = 1; t <= n; t++) {
		read();
		solve(t);
	}
	return 0;
}
