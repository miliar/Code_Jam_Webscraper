#include <cstdio>
#include <vector>

long long runTest(long long r, long long k, const std::vector<long long> &g) {
	std::vector<long long> time(g.size(), -1);
	std::vector<long long> money(g.size());
	time[0] = 0;
	money[0] = 0;
	long long cmoney = 0;
	unsigned int head = 0;
	bool done = false;
	for (long long ctime = 0; ctime<r;) {
		long long count = 0;
		unsigned int i;
		for (i=head; i<g.size() && count+g[i]<=k; i++)
			count += g[i];
		if (i==g.size())
			for (i=0; i<head && count+g[i]<=k; i++)
				count += g[i];
		head = i;
		cmoney += count;
		ctime++;
		if (time[head]!=-1 && !done) {
			done = true;
			if (ctime+2>=r)
				continue;
			long long timeLeft = r - ctime - 2;
			long long loopTime = ctime - time[head];
			long long loopMoney = cmoney - money[head];
			long long loopCount = timeLeft / loopTime;
			ctime += loopTime * loopCount;
			cmoney += loopMoney * loopCount;
		} else {
			time[head] = ctime;
			money[head] = cmoney;
		}
	}
	return cmoney;
}

int main() {
	int t;
	std::scanf("%d", &t);
	for (int i=0; i<t; i++) {
		int r, k, n;
		std::scanf("%d%d%d", &r, &k, &n);
		std::vector<long long> g(n);
		for (int j=0; j<n; j++) {
			int x;
			std::scanf("%d", &x);
			g[j] = x;
		}
		std::printf("Case #%d: %lld\n", i+1, runTest(r, k, g));
	}
	return 0;
}


