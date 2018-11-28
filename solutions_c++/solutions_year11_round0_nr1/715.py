#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {

freopen("in.txt", "r", stdin);

int i, N, p[2], t[2], nextp, cur, k, K;
char tmpc;

cin >> K;

for (k=1; k<=K; k++) {
	cin >> N;

	t[0] = t[1] = 0; p[0] = p[1] = 1;
	for (i=0; i<N; i++) {
		cin >> tmpc;
		cin >> nextp;

		if (tmpc == 'O') cur = 0;
		else cur = 1;

		t[cur] = max(t[cur] + abs(nextp - p[cur]), t[1-cur]) + 1;
		p[cur] = nextp;
	}
	cout << "Case #" << k << ": " << max(t[0], t[1]) << endl;
}

return 0;
}
