#include <iostream>
#include <string>
using namespace std;

int N, K;
string S;
string S2;

int perm[5];
bool used[5];
int best;

void rek(int p) {
	if (p == K) {
		S2 = S;
		for (int i = 0; i < (int) S2.size(); i += K) {
			for (int j = 0; j < K; j++) {
				S2[i+j] = S[i+perm[j]];
			}
		}
		int res = 1;
		for (int i = 0; i < (int) S2.size() - 1; i++) {
			if (S2[i] != S2[i+1]) res++;
		}
		if (best > res) best = res;
		return;
	}
	for (int i = 0; i < K; i++) {
		if (used[i]) continue;
		used[i] = true;
		perm[p] = i;
		rek(p+1);
		used[i] = false;
	}
}

int main() {
	cin >> N;
	for (int tcs = 1; tcs <= N; tcs++) {
		cin >> K >> S;
		memset(used, 0, sizeof(used));
		best = INT_MAX;
		rek(0);
		cout << "Case #" << tcs << ": " << best << endl;
	}
	return 0;
}
