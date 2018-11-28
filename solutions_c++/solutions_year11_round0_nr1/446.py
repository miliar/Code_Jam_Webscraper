#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int last[2], lastTime[2];
int curTime;
void process(int who, int pos) {
	int t = abs(pos - last[who]) + 1;
	lastTime[who] = max(lastTime[who] + t, curTime + 1);
	last[who] = pos;
	curTime = lastTime[who];
}

int solve() {
	int N; scanf("%d ", &N);

	last[0] = last[1] = 1;
	lastTime[0] = lastTime[1] = 0;
	curTime = 0;

	for (int i = 0; i < N; i++) {
		char who; int pos; scanf("%c %d ", &who, &pos);
		
		process(who == 'O', pos);
	}

	return curTime;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++)
		printf("Case #%d: %d\n", i, solve());

	return 0;
}
