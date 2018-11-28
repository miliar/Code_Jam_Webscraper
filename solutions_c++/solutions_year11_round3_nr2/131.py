#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
typedef long long ll;
int p[100000];
int a[1100];
ll dist[1000100];
ll rem[1000100];
int main()
{
	int T;
	scanf("%d",&T);
	for (int test=1; test<=T; ++test)  {
		memset(p, sizeof(p), 0);
		memset(a, sizeof(a), 0);
		memset(dist, sizeof(dist), 0);
		memset(rem, sizeof(rem), 0);
		ll L, t, N, C;
		scanf("%lld%lld%lld%lld",&L,&t,&N,&C);
		for (int i=0; i<C; ++i) {
			scanf("%d",&a[i]);
		}
		int k = 0;
		bool done = false;
		while (!done) {
			for (int i=0; i<C; ++i) {
				if (k*C+i+1 <= N)
					dist[k*C+i+1] = a[i];
				else {
					done = true;
					break;
				}
			}
			k++;
		}

		ll curtime = 0;
		int b1pos = 0;
		int i=1;
		for (; i<=N; ++i) {
			if (t <= 2*dist[i]) {
				curtime += t;
				dist[i] -= t/2;
				break;
			}
			else {
				curtime += 2*dist[i];
				t-=2*dist[i];
			}
		}
		int r = 0;
		for (;i<=N; ++i) {
			rem[r] = dist[i];
			r++;
		}
		sort(rem, rem+r);
		for (i=r-1; i>=0; --i) {
			if (L) {
				curtime += rem[i];
				L--;
			}
			else {
				curtime += 2 * rem[i];
			}
		}

		printf("Case #%d: %lld\n", test, curtime);

	}
	return 0;
}
