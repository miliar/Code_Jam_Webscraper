#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for(int k=1;k<=T;k++) {
		int X, S, R, t, N;
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		queue<int>  b, c, w;
		for(int i=0;i<N;i++) {
			int bb, cc, ww;
			scanf("%d", &bb);scanf("%d%d", &cc, &ww);
			b.push(bb); c.push(cc); w.push(ww);
		}
		int loc=0, d[110], sum=0;
		memset(d, 0, sizeof(d));
		while(loc<X) {
			if (b.front() == loc) {
				d[w.front()] += c.front() - loc;
				loc = c.front();
				w.pop(); c.pop(); b.pop();
			} else loc++;
		}
		for(int i=0;i<=100;i++) sum+=d[i];
		d[0] = X - sum;
		double rest = t, ans = 0.0;
		loc = 0;
		while(loc <= 100) {
			double speed = loc + R;
			double time = 1.0 * d[loc] / speed;
			if (time > rest) {
				ans += rest + (d[loc] - rest*speed) / (loc+S);
				rest = 0.0;
			} else {
				ans += time;
				rest -= time;
			}
			loc++;
		}
		printf("Case #%d: %lf\n", k, ans);
	}
	return 0;
}
