#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int T, m, n, cnt;
long long l, k, c, p;

int main(){
	scanf("%d", &T);
	for (int tt = 1; tt<=T; tt++){
		cnt = 0;
		printf("Case #%d: ", tt);
		scanf("%lld%lld%lld", &l, &p, &c);
		while (l<p){
			l*=c;
			++cnt;
		}
		if (cnt <= 1) puts("0");
		else {
			l = 1, p = 0;
			while (l < cnt) l *= 2, ++p;
			printf("%lld\n", p);
		}
	}
	return 0;
}
