#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
bool ok(int a,int b) {
	int cnta = 0;
	int cntb = 0;
	int x = 1;
	int A = a , B = b;
	while (a) {
		a /= 10;
		cnta ++;
		x *= 10;
	}
	x /= 10;
	while (b) {
		b /= 10;
		cntb ++;
	}
	if (cnta != cntb) return false;
	for (int i = 0 ; i < cnta ; i ++) {
		int aa = A % 10;
		A /= 10;
		A += aa * x;
		if (A == B) return true;
	}
	return false;
}
int main() {
	freopen("C-small-attempt7.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		int A , B;
		scanf("%d%d",&A,&B);
		int cnt = 0;
		for (int a = A ; a <= B ; a ++) {
			for (int b = a + 1 ; b <= B ; b ++) {
				if (ok(a , b)) cnt ++;
			}
		}
		printf("Case #%d: %d\n",cas , cnt);
	}
	return 0;
}