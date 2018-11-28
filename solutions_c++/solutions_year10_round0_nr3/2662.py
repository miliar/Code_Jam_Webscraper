#include <stdio.h>
#include <queue>

typedef long long ll;

ll T, R, k, N, i, j, g, s;
std::queue<ll> waitingQ, boardingQ;

int main(void) {
	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt", "w");

	fscanf(fin, "%lld", &T);
	for(i = 1; i <= T; i++) {
		while(!waitingQ.empty()) waitingQ.pop();
		while(!boardingQ.empty()) boardingQ.pop();

		fscanf(fin, "%lld%lld%lld", &R, &k, &N);
		for(j = 0; j < N; j++) {
			fscanf(fin, "%lld", &g);
			waitingQ.push(g);
		}

		s = 0;
		for(j = 0; j < R; j++) {
			g = waitingQ.front();
			boardingQ.push(waitingQ.front());
			waitingQ.pop();
			while(!waitingQ.empty()) {
				if(g + waitingQ.front() <= k) {
					g += waitingQ.front();
					boardingQ.push(waitingQ.front());
					waitingQ.pop();
				}else break;
			}
			s += g;
			while(!boardingQ.empty()) {
				waitingQ.push(boardingQ.front());
				boardingQ.pop();
			}
		}
		fprintf(fout, "Case #%lld: %lld\n", i, s);
	}

	fclose(fout);
	fclose(fin);
	return 0;
}