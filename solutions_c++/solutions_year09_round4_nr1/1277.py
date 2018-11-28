#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)
#define MSET(a, b) memset(a, b, sizeof(a))
#define forr(i, a, b) for(int i=a;i<b;i++)

const int INF = 0x3f3f3f3f; const int NEGINF = 0xc0c0c0c0;
const double EPS = 1e-10;

int cmp(double x, double y=0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

char bla[200];
int v[200];

int main() {
	TRACE(setbuf(stdout, NULL));
	int T, N, _42=1;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %d", &N);
		forr(i, 0, N) {
			scanf(" %s", bla);
			int num = 0;
			forr(j, 0, N) {
				if (bla[j] == '1') num = j;
			}
			v[i] = num;
		}
		int ans = 0;
		forr (i, 0, N) {
			int cont =0;
			forr (j, 0, i) {
				if (v[j] < v[i]) cont++;
			}
			if (v[i] - cont < 0) ans += 0;
			else ans += (v[i] - cont);
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
	return 0;
}
