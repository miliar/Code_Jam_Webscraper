#include <cstdio>
#include <cmath>
#include <algorithm>
const int MAX_N = 10101;
using namespace std;

int caseAmt;
long long sound[MAX_N];

long long LCM(long long a, long long b) {
	int tmp;
	long long c, d;
	c = a;
	d = b;
	while (d != 0) {
		tmp = d;
		d = c % d;
		c = tmp;
	}
//	printf("(%lld, %lld) GCD = %lld, LCM = %lld\n", a, b, c, (a / c) * b);
	return (a / c) * b;
}

int N;
long long L, H;

void solve2(int caseNum) {
//	printf("Case #%d: ", caseNum);
//	scanf("%d %lld %lld", &N, &L, &H);
//	printf("(%d %lld %lld) ", N, L, H);
//	for(int i = 1; i <= N; i++) scanf("%lld", &sound[i]);
	for(long long i = L; i <= H; i++) {
		bool done = false;
		for(int j = 1; j <= N; j++) {
			if(i % sound[j] == 0 || sound[j] % i == 0) continue;
			done = true;
			break;
		}
		if(!done) {
			printf("%lld\n", i);
			return;
		}
	}
	printf("NO\n");
	return;
}

void solve(int caseNum) {
	printf("Case #%d: ", caseNum);
	scanf("%d %lld %lld", &N, &L, &H);
//	printf("(%d %lld %lld) ", N, L, H);
	for(int i = 1; i <= N; i++) scanf("%lld", &sound[i]);
//	sort(sound + 1, sound + N + 1);
////	for(int i = 1; i <= N; i++) printf("%lld ", sound[i]);
//	int ind = 0;
//	long long J = 1;	//the note jeff will play
//	while(J < L) {
//		ind++;
//		if(ind > N) {
//			printf("NO\n");
//			return;
//		}
//		J = LCM(J, sound[ind]);
//	}
//	while(J <= H) {
//		bool done = false;
//		for(int i = ind + 1; i <= N; i++) {
//			if(J % sound[i] == 0 || sound[i] % J == 0) continue;
//			done = true;
//			break;
//		}
//		if(done) {
//			ind++;
//			if(ind > N) {
//				printf("NO\n");
//				return;
//			}
//			J = LCM(J, sound[ind]);
//		} else {
//			printf("%lld\n", J);
//			return;
//		}
//	}
//	printf("NO\n");
	return;
}

int main() {
	freopen("small.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	scanf("%d", &caseAmt);
	for(int i = 1; i <= caseAmt; i++) {
		solve(i);
		solve2(i);
	}

//	freopen("large.txt", "r", stdin);
//	freopen("largeout.txt", "w", stdout);
//	scanf("%d", &caseAmt);
//	for(int i = 1; i <= caseAmt; i++) solve(i);
	return 0;
}
