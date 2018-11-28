#include <iostream>
#include <queue>

long solve(long r, long k, std::queue<long> q)
{
	long result = 0;
	while (r--) {
		int p = 0;
		std::queue<long> qc;		// on rollercoaster
		while ((p + q.front() <= k) && (!q.empty())) { // add more people
			p += q.front();
			qc.push(q.front());
			q.pop();
		}
		result += p;	// money
		while (!qc.empty()) {		// remove people
			q.push(qc.front());
			qc.pop();
		}
	}
	return result;
	
}

int main()
{
	long t, r, k, n, g;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::queue<long> q;
		std::cin >> r >> k >> n;
		for (int j = 0; j < n; j++) {
			std::cin >> g;
			q.push(g);
		}
		std::cout << "Case #" << i+1 << ": " << solve(r, k, q) << std::endl;
	}
	return 0;
}
	
