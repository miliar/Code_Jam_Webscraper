#include <cstdio>
#include <cstdlib>
#define max(A, B) (A > B ? A : B)

int T, N, o, b, s, ans;

int main(void) {
	int i, c = 0, x, v1, v2;
	char a, last;
	scanf("%d",&T);
	while(T--) {
		o = b = 1;
		s = ans = last = 0;
		scanf("%d ",&N);
		for(i = 0; i < N; i++) {
			scanf("%c %d ",&a,&x);
			v1 = (a == 'O' ? o : b);
			if(last == a) {
				ans += abs(v1-x) + 1;
				s += abs(v1-x) + 1;
			} else {
				ans += max(abs(v1-x)-s+1,1);
				s = max(abs(v1-x)-s+1,1);
			}
			v1 = x;
			last = a;
			if(a == 'O')
				o = v1;
			else
				b = v1;
		}
		printf("Case #%d: %d\n",++c,ans);
	}
	return 0;
}
