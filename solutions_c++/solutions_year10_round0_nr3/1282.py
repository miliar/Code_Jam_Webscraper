#include <iostream>
#include <vector>
using namespace std;

typedef struct 
{
	int size;
	unsigned int length;
	unsigned long long price;
	int met;
	unsigned long long revenue;
} data;

unsigned long long solve()
{
	int r = 0, k = 0, n = 0;

	// input
	cin >> r >> k >> n;
	vector<data> g(n);
	for (int i = 0; i < n; ++i)
		cin >> g[i].size;
	// prepare
	for (int i = 0; i < n; ++i)
	{
		unsigned long long sum = 0;
		unsigned int count = 0;

		while (1)
		{
			unsigned int size = g[(i + count) % n].size;
			if (sum + size <= k && count < n)
			{
				sum += size;
				++count;
			} else
				break;
		}
		g[i].length = count;
		g[i].price = sum;
		g[i].met = -1;
		g[i].revenue = 0;
	}

	unsigned long long revenue = 0;
	unsigned int pos = 0;

	while (r > 0) {
		// cout << "r = " << r << " pos = " << pos << " rev = " << revenue << endl;
		// cout << "\tsize = " << g[pos].size << " ";
		// cout << "length = " << g[pos].length << " ";
		// cout << "price = " << g[pos].price << " ";
		// cout << "met = " << g[pos].met << " ";
		// cout << "rev = " << g[pos].revenue << endl;

		if (g[pos].met != -1 && g[pos].met - r < r)
		{
			int diff = g[pos].met - r;
			unsigned rev = revenue - g[pos].revenue;
			revenue += rev * (r / diff);
			r %= diff;
		}
		else
		{
			g[pos].met = r--;
			g[pos].revenue = revenue;
			revenue += g[pos].price;
			pos = (pos + g[pos].length) % n;
		}
	}

	return revenue;
}

int main()
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}
