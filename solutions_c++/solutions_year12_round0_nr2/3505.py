#include <cstdio>
#include <algorithm>
using namespace std;
int N, S, P;
int buf[100];

int main(int argc, char const *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, i=0;
	scanf("%d\n", &t);
	while (i++<t) {
		int sum = 0;
		scanf("%d %d %d", &N, &S, &P);
		int n = N;
		while (n--) {
			scanf("%d", buf+n);
		}
		sort(buf, buf+N);
		n=N;
		while (n--) {
			int x = buf[n]%3;
			int y = buf[n]/3;
			//printf("%d %d P:%d\n", x, y, P);
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
				if (x>=2) {
					if(S){
						--S;
						++sum;
					}
				}
			}
		}
		printf("Case #%d: %d\n", i, sum);
	}
	return 0;
}