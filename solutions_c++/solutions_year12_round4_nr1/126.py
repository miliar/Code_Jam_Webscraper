#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int d[10111], l[10111];
int len[10111];

int main()
{
	int T; cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N; cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> d[i] >> l[i];
		}
		int D; cin >> D;

		bool ok = false;
		memset(len, 0, sizeof len);
		len[0] = d[0];
		for (int i = 0; i < N; i++) {
			if (d[i]+len[i] >= D) ok = true;
			for (int j = i+1; j < N; j++) {
				if (d[j] > d[i]+len[i]) break;
				len[j] = max(len[j], min(d[j]-d[i], l[j]));
			}
		}

		printf("Case #%d: %s\n", ti, ok ? "YES" : "NO");
	}
}
