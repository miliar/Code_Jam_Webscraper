#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 1005;
const double err = 1e-8;

int T;
int X, S, R, run_time, N;

struct state {
	int w, len;
	inline bool operator < (const state &o) const {
		return (w < o.w);
	}
} mem[MAXN];
int L;

int main() {
	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d %d %d %d",&X,&S,&R,&run_time,&N);
		R -= S;
		L = 0;
		int totlen = X;
		
		double rt = run_time;
		
		for(int a, b, c, i = 0 ; i < N ; i++) {
			scanf("%d %d %d",&a,&b,&c);
			mem[L++] = ((state){c + S, b - a});
			totlen -= (b - a);
		}
		mem[L++] = ((state){S, totlen});
		sort(mem, mem + L);
		
		double ans = 0.0;
		
		for(int i = 0 ; i < L && rt > err; i++) {
			double wt = (double)mem[i].len / ((double)mem[i].w + R);
			if (wt < rt + err) {
				mem[i].w += R;
				rt -= wt;
			}	else {
				ans = (mem[i].len - rt * R) / ((double)mem[i].w);
				mem[i] = mem[L - 1];
				L--;
				break;
			}
		}
		
		for(int i = 0 ; i < L ; i++) {
			ans += ((double)mem[i].len) / (mem[i].w);
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
	return 0;
}
