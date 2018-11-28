#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define PB push_back

void rusz(int &kto, int &gdzie) {
	if (kto == gdzie) return;
	if (kto < gdzie) ++kto;
	else --kto;
}

void testcase() {
	queue<int> o, b;
	vector<char> seq;
	int n;
	scanf("%d", &n);
	REP(i,n) {
		char buf[5];
		int but;
		scanf("%s%d", buf, &but);
		if (buf[0] == 'O')
			o.push(but);
		else b.push(but);
		seq.PB(buf[0]);
	}
	o.push(-1);
	b.push(-1);
	int pressed = 0;
	int currentO = 1, currentB = 1;
	int result = 0;
	while (pressed < n) {
		++result;
		if (seq[pressed] == 'O') {
			if (currentO == o.front()) {
				++pressed;
				o.pop();
			} else {
				rusz(currentO, o.front());
			}
			rusz(currentB, b.front());
		} else {
			if (currentB == b.front()) {
				++pressed;
				b.pop();
			} else {
				rusz(currentB, b.front());
			}
			rusz(currentO, o.front());
		}
	}
	printf("%d\n", result);
}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d: ", ++v);
		testcase();
	}
}
