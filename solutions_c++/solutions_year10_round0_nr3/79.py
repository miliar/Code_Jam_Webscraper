#include <cstdio>
#include <cstring>

unsigned t;
unsigned rides;
unsigned cap;
unsigned grNum;

unsigned groups[1024];
unsigned nextGroup[1024];
unsigned ridePrice[1024];

void CalculateRides() {
	unsigned currGr = 0;
	unsigned nextGr = 0;
	unsigned currCap = groups[0];

	for (unsigned grIndex = 0; grIndex < grNum; grIndex++) {

		currGr = grIndex;

		if (grIndex > 0) {
			if (nextGroup[grIndex - 1] == grIndex) {
				nextGr = currGr;
				currCap = groups[currGr];
			}
			else {
				nextGr = (nextGroup[grIndex - 1] + grNum - 1) % grNum;
				currCap = ridePrice[grIndex - 1] - groups[grIndex - 1];
			}
		}

		while (currCap <= cap) {
			nextGr = (nextGr + 1) % grNum;
			if (nextGr == currGr || currCap + groups[nextGr] > cap) {
				ridePrice[currGr] = currCap;
				nextGroup[currGr] = nextGr;
				break;
			}

			currCap += groups[nextGr];
		}
	}
}

long long MakeRides(unsigned beg_idx, unsigned times) {
	long long res = 0LL;
	unsigned curr_gr = beg_idx;
	for (unsigned i = 0; i < times; i++) {
		res += ridePrice[curr_gr];
		curr_gr = nextGroup[curr_gr];
	}

	return res;
}

int vis[1024];

int main() {

	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%u", &t);
	for (unsigned i = 1; i <= t; i++) {
		scanf("%u %u %u", &rides, &cap, &grNum);
		for (unsigned j = 0; j < grNum; j++) {
			scanf("%u", &groups[j]);
		}

		CalculateRides();

		memset(vis, 0, sizeof(vis));
		int cg = 0;
		int cnt = 1;
		while (vis[cg] == 0) {
			vis[cg] = cnt;
			cnt++;
			cg = nextGroup[cg];
		}

		long long ans = 0LL;
		unsigned beg_it = vis[cg] - 1;
		unsigned it_len = cnt - vis[cg];
		long long it_cnt = (rides - beg_it) / it_len;
		unsigned last_it = (rides - beg_it) % it_len;

		ans += MakeRides(0, beg_it);
		long long circ_price = MakeRides(cg, it_len);
		circ_price *= it_cnt;
		ans += circ_price;
		ans += MakeRides(cg, last_it);

		printf("Case #%u: %lld\n", i, ans);
	}

	return 0;
}
