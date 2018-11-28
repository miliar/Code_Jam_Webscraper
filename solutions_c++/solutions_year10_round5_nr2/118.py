#include<cstdio>
#include<algorithm>
#include<cstring>
#include<functional>

using namespace std;

int DP[10001];

int main(){
	int N;
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		long long L;
		scanf("%lld%d", &L, &N);
		for (int i = 1 ; i <= 10000; ++i) DP[i] = 1<<29;
		int S[N];
		for (int i = 0 ; i < N; ++i) scanf("%d", S+i);
		for (int i = 1; i <= 10000; ++i)
			for (int j = 0 ; j < N; ++j)
				if (i - S[j] >= 0)
					DP[i] = min(DP[i], DP[i-S[j]] + 1);
		long long ans = 1LL<<60;
		for (int i = 1 ; i <= 10000; ++i)
			if (DP[i] != 1<<29)
				for (int j =i; j <= 10000; ++j)
					if (DP[j] != 1<<29)
						if ((L - j) % i == 0)
							ans = min(ans, (long long)(L-j)/i * DP[i] + DP[j]);
		if (ans == 1LL<<60) puts("IMPOSSIBLE");
		else printf("%lld\n", ans);
	}
	return 0;
}
