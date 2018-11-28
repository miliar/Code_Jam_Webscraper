#include <cstdio>
#include <map>
#define let(i,a) __typeof(a)i=a
using namespace std;

int N, T, NA, NB;

int main() {
	scanf("%d\n", &N);
	for (int case_num = 1; case_num <= N; case_num++) {
		scanf("%d\n%d %d\n", &T, &NA, &NB);
		map<int, int> A, B; A.clear(); B.clear();
		for (int i = 0; i < NA + NB; i++) {
			int h1, m1, h2, m2;
			scanf("%02d:%02d %02d:%02d", &h1, &m1, &h2, &m2);
			m1 += h1 * 60; m2 += h2 * 60; m2 += T;
			if (i < NA) { A[m1]++; B[m2]--; }
			else { A[m2]--; B[m1]++; }
		}
		printf("Case #%d:", case_num);
		int sum = 0, max = 0;
		for (let(it, A.begin()); it != A.end(); it++) {
			sum += it->second;
			if (max < sum) max = sum;
		}
		printf(" %d", max);
		sum = 0, max = 0;
		for (let(it, B.begin()); it != B.end(); it++) {
			sum += it->second;
			if (max < sum) max = sum;
		}
		printf(" %d\n", max);
	}
	return 0;
}
