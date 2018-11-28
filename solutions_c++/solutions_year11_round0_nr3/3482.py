#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define eps 1e-8
#define oo 1e9


using namespace std;

int T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, an;
int a[1200], b[200];
char c[10];

int main(){
	scanf("%d", &T);
	for (int rr = 1; rr <= T; rr++){
		memset(b, 0, sizeof(b));
		printf("Case #%d: ", rr);
		scanf("%d", &m);
		for (int i=0; i<m; i++){
			scanf("%d", &a[i]);
			q = a[i]; cnt = 0;
			while (q){
				b[cnt] += (q&1);
				cnt++; q>>=1;
			}
		}
		fi = 0;
		for (int i=0; i<50; i++)
			if ((b[i]&1))
				fi = 1;
		if (fi == 0){
			mi = oo; s = 0;
			for (int i=0; i<m; i++){
				s += a[i];
				if (a[i] < mi)
					mi = a[i];
			}
			printf("%d\n", s - mi);
		} else puts("NO");
	}
	return 0;
}
