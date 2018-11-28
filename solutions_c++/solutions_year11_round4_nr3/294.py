#include <cstdio>

int T;
int primes[1000000];
int num[10000010];
int pcount;
__int64 N;

void Open() {
	freopen ("P3.in", "r", stdin);
	freopen ("P3.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

__int64 log(__int64 a, __int64 num) {
	__int64 ans = 0;
	while (num >= a) {
		__int64 tmp = a, count = 1;
		__int64 ltmp;
		while (tmp <= num) ltmp = tmp, tmp *= tmp, count*=2;
		tmp /= ltmp, count /= 2;
		num /= tmp;
		ans += count;
	}
	return ans;
}

void init() {
	scanf ("%I64d", &N);
}

void getAllPrimes() {
	for (int i = 1; i <= 1000000; i++) num[i] = 1;
	for (int i = 2; i <= 1000000; i++) {
		if (num[i] == 0) continue;
		int j = i * 2;
		while (j <= 1000000) num[j] = 0, j += i;
	}

	pcount = 0;
	for (int i = 2; i <= 1000000; i++)
		if (num[i] == 1) primes[pcount++]  = i;
}

__int64 work() {
	__int64 ans = 0;
	for (int i =0; i < pcount; i++) {
		__int64 tmp = (__int64)primes[i];
		ans += log(tmp, N) - 1;
		if ((tmp * tmp) > N) break;
	}
	return ans;
}

void output(int caseNo, __int64 ans) {
	printf ("Case #%d: %I64d\n", caseNo, ans + 1);
}

void process() {
	getAllPrimes();
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		init();
		output(caseNo, work());
	}
}

int main() {
	Open();
	process();
	Close();
	return 0;
}