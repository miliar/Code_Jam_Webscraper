#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

#define pb pus_back
#define sz(v) ((int)v.size())

int D[200][200];
int val[200];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	cin >> T;
	int N, S, p;
		int ans = 0;
	for (int t = 1; t <= T; ++t) {
		ans = 0;
		cin >> N >> S >> p;
		for (int i = 1; i <= N; ++i)
			cin >> val[i];
		for (int i = 0; i <= N + 10; ++i)
			for (int j = 0; j < S + 10; ++j)
				D[i][j] = 0;
		for (int i = 1; i <= N; ++i) {
			bool UnExp = false,
				Exp = false;
			for (int a = p; a <= 10; ++a) {
				for (int b = max(a - 2, 0); b <= a; ++b)
					for (int c = max(a - 2, 0); c <= a; ++c) {
						if (a + b + c != val[i])
							continue;
						if (min(b,c) >= a - 1)
							UnExp = true;
						else
							Exp = true;
					}
			}
			for (int s = 0; s <= S; ++s)
					D[i][s] = D[i-1][s];
			if (UnExp) {
				for (int s = 0; s <= S; ++s)
					D[i][s] = D[i-1][s] + 1;
			}
			if (Exp) {
				for (int s = 1; s <= S; ++s)
					D[i][s] = max(D[i-1][s-1] + 1, D[i][s]);
			}
		}
		printf("Case #%d: %d\n",t, D[N][S]);
	}
			
	return 0;
}