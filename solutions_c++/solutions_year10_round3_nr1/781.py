#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define oo 1<<28
#define eps 1e-13
#define fl(x,y) ((x)+(eps)<(y))
#define fle(x,y) ((x)<(y)+(eps))
#define feq(x,y) (fabs((x)-(y))<(eps))

int N;
int a[1005], b[1005];
int main() {
	int T; scanf("%d", &T);
	for (int Cas = 1; Cas <= T; ++Cas) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d%d", &a[i], &b[i]);
		}
		int cnt = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if ((a[j] < a[i]) && b[j] > b[i] || a[j] > a[i] && b[j] < b[i]) ++cnt;
			}
		}
		printf("Case #%d: ", Cas);
		printf("%d\n", cnt/2);
	}
	return 0;
}
