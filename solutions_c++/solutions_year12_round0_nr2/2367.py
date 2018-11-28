#include <cstdio>
#include <algorithm>
	using namespace std;

int N, S, P;
int m[100];

int main(int argc, char const *argv[])
{
	int t, i=0;
	scanf("%d\n", &t);
	while (i++<t) {
		int sum = 0;
		scanf("%d %d %d", &N, &S, &P);
		int n = N;
		while (n--) {
			scanf("%d", m+n);
		}
		sort(m, m+N);
		n=N;
		while (n--) {
			int x = m[n]%3;
			int y = m[n]/3;
			if (y>=P) {
				++sum;
			} else if (y==(P-1)) {
				if (x==0) {
					if (y==0) {
						continue;
					}
					if (S) {
						--S;
					}else{
						--sum;
					}
				}
				++sum;
			} else if (y==(P-2)) {
				if (x==2 && S) {
					--S;
					++sum;
				}
			}
		}
		printf("Case #%d: %d\n", i, sum);
	}
	return 0;
}