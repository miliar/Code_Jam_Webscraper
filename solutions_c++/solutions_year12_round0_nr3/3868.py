#include <cstdio>
#include <cstdlib>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int a, b;
		long long result = 0;
		scanf("%d%d", &a, &b);
		for (int n=a; n<b; n++) {
			char buf[20];
			sprintf(buf, "%d", n);
			int m;
			do {
				char first=buf[0];
				int i;
				for (i=1; buf[i]; i++)
					buf[i-1] = buf[i];
				buf[i-1] = first;
				m = atoi(buf);
				if (n<m && m<=b) {
					//fprintf(stderr, "%d/%d\n", n, m);
					result++;
				}
			} while (n != m);
		}
		printf("Case #%d: %lld\n", t, result);
	}
	return 0;
}