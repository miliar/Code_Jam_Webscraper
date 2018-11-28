#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int n, s, q;
map<string, int> st;
vector<int> vc;
int hash[128][1024];

int bfs() {
	memset(hash, 0, sizeof(hash));
	queue<int> qe, qs, qm;
	for (int i = 1; i <= s; ++i) {
		qe.push(i);
		qs.push(0);
		qm.push(0);
	}
	while (!qe.empty()) {
		int ce = qe.front();
		int cs = qs.front();
		int cm = qm.front();
		qe.pop(); qs.pop(); qm.pop();
	//	printf("%d, %d, %d\n", ce, cs, cm);
		while (cs < q && ce != vc[cs]) {
			hash[ce][cs] = true;
			cs++;
		}
		if (cs == q) return cm;
		for (int i = 1; i <= s; ++i) {
			if (i != ce && !hash[i][cs]) {
				qe.push(i);
				qs.push(cs);
				qm.push(cm + 1);
			//	printf("push %d, %d, %d\n", i, cs, cm+1);
			}
		}
	}
	return -1;
}
int main() {
	char str[1024];
	scanf("%d", &n);
	for (int k = 0; k < n; ++k) {
		st.clear();
		vc.clear();
		scanf("%d ", &s);
		for (int i = 0; i < s; ++i) {
			gets(str);
			st[string(str)] = i + 1;
		}
		scanf("%d ", &q);
		for (int i = 0; i < q; ++i) {
			gets(str);
			vc.push_back(st[string(str)]);
		}
		printf("Case #%d: %d\n", k + 1, bfs());
	}
}

