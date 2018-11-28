#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long int64;

class Cache {
public:
	Cache()
		: lastR(-1)
		, lastVal(-1)
		, val(-1)
		, posOff(-1)
		, jumpVal(-1)
		, jumpSteps(-1)
	{}

	int posOff;
	int lastR;
	int jumpSteps;

	int64 val;
	int64 lastVal;
	int64 jumpVal;
};

int64 solve(int r, const int k, vector<int>& gs)
{
	vector<Cache> cache;
	cache.resize(gs.size());

	int pos = 0;
	int64 val = 0;
	while (r > 0) {
		Cache& c = cache[pos];

		// Loop detected
		if (c.jumpVal != -1) {
			int n = r / c.jumpSteps;
			if (n > 0) {
				val += n * c.jumpVal;
				r -= n * c.jumpSteps;
				if (r == 0) break;
			}
		}

		// Cached
		if (c.val != -1) {
			val += c.val;
			pos += c.posOff;

			// Compute loop
			if (c.jumpVal == -1) {
				c.jumpSteps = c.lastR - r;
				c.jumpVal = val - c.lastVal;
			}
		}
		
		// Not cached
		else {
			int64 tmp = 0;
			int load = 0;
			int i = 0;
			int next = gs[pos];
			int sz = gs.size();
			while (load+next <= k && i < sz) {
				load += next;
				i++;
				next = gs[(pos+i) % sz];
			}
			pos += i;
			val += load;

			c.val = load;
			c.posOff = i;
			
			c.lastR = r;
			c.lastVal = val;
		}

		r--;
		pos = pos % gs.size();
	}

	return val;
}

int main()
{
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	int n;
	in >> n;

	for (int i=0; i<n; i++) {
		int r, k, n;
		in >> r >> k >> n;
		vector<int> gs(n);
		for (int j=0; j<n; j++) {
			in >> gs[j];
		}
		int64 result = solve(r, k, gs);

		out << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}
