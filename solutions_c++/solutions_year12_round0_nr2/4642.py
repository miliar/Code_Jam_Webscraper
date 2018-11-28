#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#define eps 1e-8
#define oo 1<<29
#define LL long long

using namespace std;

int T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, an, p;
int a[200];

int main(){
	scanf("%d", &T);
	for (int rr = 1; rr <= T; rr++){
		cnt = 0;
		printf("Case #%d: ", rr);
		scanf("%d%d%d", &m, &s, &p);
		for (int i=0; i<m; i++)
			scanf("%d", &a[i]);
		for (int i=0; i<m; i++){
			if ((a[i] + 2)/3 >= p)
				cnt++;
			else if ((a[i] + 4)/3 >= p && s > 0 && a[i] >= 2)
				cnt++, s--;
		}
		printf("%d\n", cnt);
	}
	return 0;
}
