#include <cstdio>
#include <string>
#include <cstdlib>
using namespace std;

const int MAXN = 64;

int casenum, N, K;
long long T[MAXN];

const char res[][4] = {"OFF", "ON"};

int main() {
	
	int ans;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &casenum);
	for (int ca = 1; ca <= casenum; ca++) {
		scanf("%d %d", &N, &K);
		T[1] = 1;
		for (int i = 2; i <= N; i++) T[i] = 2*T[i-1] + 1;
		printf("Case #%d: ", ca);
		
		ans = 0;
		if (K < T[N]) ans = 0;
		else if (K == T[N]) ans = 1;
		else {
			K -= T[N];
			if (K % (T[N]+1) == 0) ans = 1;
			else ans = 0;
		}
		printf("%s\n", res[ans]);
	}
	return 0;
}
