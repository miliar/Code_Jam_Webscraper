#include<cstdio>
#include<cmath>

using namespace std;

int free(long long n, long long pd, long long pg) {
	if(pg == 100 && pd == 100) return 1;
	if(pg == 100 && pd < 100) return 0;
	if(pg == 0 && pd > 0) return 0;
	if(pg == 0 && pd == 0) return 1;
	if(n >= 100) return 1;

	for(int i = 1; i <= n; i++) {
		if((pd * i) % 100 == 0) return 1;
	}

	return 0;
}

int main() {
	int T = 0;
	scanf("%d", &T);

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		long long n = 0, pd = 0, pg = 0;
		scanf("%lld %lld %lld", &n, &pd, &pg);

		int res = free(n, pd, pg);

		printf("Case #%d: ", caseNum);
		if(res == 1)
			printf("Possible\n");
		else
			printf("Broken\n");
	}

	return 0;
}
