#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int tests, N, B[102], Bmax, End, Queue[10010], QHead, QTail, Dist[101], tmp, Mark[101], True[101];
long long L;

int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int cases = 1; cases <= tests; ++ cases) {
		cin >> L >> N;
		Bmax = 0;
		for (int i = 0; i < N; ++ i) { cin >> B[i]; Bmax = max(Bmax, B[i]); }
		sort(B, B + N);
		End = L % Bmax;
		cout << "Case #" << cases << ": ";
		if (End == 0)
			cout << L / Bmax << endl;
		else {
			memset(Dist, 0x3F, sizeof(Dist));
			memset(Mark, 0, sizeof(Mark));
			Queue[QTail = 0] = 0; QHead = 1; Dist[0] = 0; True[0] = 0;
			while (QHead != QTail) {
				int now = Queue[QTail ++];
				for (int i = 0; i < N; ++ i) {
					int dest = (now + B[i]) % Bmax;
					int weight = 1 - ((now + B[i]) / Bmax);
					if (Dist[dest] > Dist[now] + weight) {
						Dist[dest] = Dist[now] + weight;
						Mark[dest] = Mark[now] + B[i];
						True[dest] = True[now] + 1;
						Queue[QHead ++] = dest;
					}
				}
			}
			if (Dist[End] == 0x3F3F3F3F) puts("IMPOSSIBLE");
			else {
				//cout << Mark[End] << " " << Bmax << endl;
				cout << True[End] + ((L - Mark[End]) / Bmax) << endl;
			}
		}
	}
	return 0;
}
