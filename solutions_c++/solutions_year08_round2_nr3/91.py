#include <iostream>
#include <string>
using namespace std;

int T, K, n, d[100];
int sequ[10000];
int next[10000];

int main() {
	cin >> T;
	for (int tcs = 1; tcs <= T; tcs++) {
		cin >> K >> n;
		for (int i = 0; i < n; i++) cin >> d[i];
		memset(sequ, -1, sizeof(sequ));
		int pos = 0;
		int jmp = 0;
		for (int i = 1; i <= K; i++) {
			while (1) {
				if (jmp == i-1 && sequ[pos] == -1) {
					sequ[pos] = i;
					pos = (pos + 1) % K;
					jmp = 0;
					break;
				} else {
					if (sequ[pos] == -1) jmp++;
					pos = (pos + 1) % K;
				}
				pos = next[pos];
			}
			for (int j = 0; j < K; j++) {
				if (sequ[j] == -1) {
					next[j] = j;
					for (int k = j-1; k >= 0 && sequ[k] != -1; k--) next[k] = j;
				}
			}
		}
		cout << "Case #" << tcs << ":";
		for (int i = 0; i < n; i++) cout << ' ' << sequ[d[i]-1];
		cout << endl;
	}
	return 0;
}
