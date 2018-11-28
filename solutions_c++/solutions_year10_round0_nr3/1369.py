#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;


void themepark(uint64_t r, uint64_t k, uint64_t n, const vector<uint64_t> &g)
{
	uint64_t i = 0; // pointer to queue head
	uint64_t b = 0; // ppl on board
	uint64_t m = 0; // money made
	
	vector<uint64_t> i_cache(n, -1);
	vector<uint64_t> b_cache(n, -1);

	for (uint64_t j = 0; j < r; j++)
	{
		if (i_cache[i] == -1)
		{
			uint64_t next = i;
			b = 0;
			while (
					!(b > 0 && next == i) && // not looped around
					b < k && // not full
					b + g[next] <= k // can take the next group
			)
			{
				b += g[next];
				next = (next + 1) % n;
			}
		
			i_cache[i] = next;
			b_cache[i] = b;
			m += b;
			i = next;
		}
		else
		{
			m += b_cache[i];
			i = i_cache[i];
		}
	}
	cout << m << endl;
}


int main()
{
	uint64_t t;
	cin >> t;
	if (!cin) return -1;
	
	for (uint64_t i = 0; i < t; i++)
	{
		uint64_t r, k, n;
		cin >> r >> k >> n;
		if (!cin) return -1;
		
		vector<uint64_t> g(n, 0);
		
		for (uint64_t j = 0; j < n; j++)
		{
			cin >> g[j];
		}
		
		cout << "Case #" << (i + 1) << ": ";
		themepark(r, k, n, g);
	}
	
}

