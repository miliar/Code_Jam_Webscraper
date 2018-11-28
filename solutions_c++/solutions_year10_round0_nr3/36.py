#include <cstdio>
typedef long long ll;

ll g[1005];
int next[1005];
ll profit[1005];
ll netprofit[1005];
int path[1005];
int posinpath[1005];

int main() {
    int t;
    scanf("%d", &t);
    int r, k, n;
    for(int casenum = 1; casenum <= t; casenum++) {
	scanf("%d", &r);
	scanf("%d", &k);
	scanf("%d", &n);
	ll gsum = 0;
	for(int i = 0; i < n; i++) {
	    int gi;
	    scanf("%d", &gi);
	    g[i] = (ll)gi;
	    gsum += g[i];
	    posinpath[i] = -1;
	}
	printf("Case #%d: ", casenum);
	if(gsum <= k) {
	    printf("%lld\n", (ll)r * (ll)gsum);
	    continue;
	}
	for(int i = 0; i < n; i++) {
	    gsum = 0;
	    int j = i;
	    while(gsum + g[j] <= k) {
		gsum += g[j];
		j = (j + 1) % n;
	    }
	    profit[i] = gsum;
	    next[i] = j;
	}
        path[0] = 0;
	posinpath[0] = 0;
	netprofit[0] = 0;
	int p = 0;
	int pos = 0;
	ll prof = 0;
	int tail, period;
	while(true) {
	    p++;
	    prof += profit[pos];
	    pos = next[pos];
	    netprofit[p] = prof;
	    if(posinpath[pos] == -1) {
		posinpath[pos] = p;
		path[p] = pos;
	    }
	    else {
		tail = posinpath[pos];
		period = p - tail;
		break;
	    }
	}
	if(r < tail)
	    printf("%lld\n", netprofit[r]);
	else
	    printf("%lld\n", ((r - tail) / period) * (netprofit[p] - netprofit[tail]) + netprofit[tail + (r - tail) % period]);
	//printf("%lld %d %d %d\n", netprofit[p] - netprofit[tail], tail, p, period);
    }
}
