#include <queue>
#include <iostream>
#include <vector>

using std::vector;

struct seg
{
	seg() {}
	seg(const long long& l, const long long& c) : len(l), cnt(c) {}
	
	long long len;
	long long cnt;
};

inline bool operator< (const seg& a, const seg&b) {return a.len < b.len;}

int main()
{
	long long tests;
	std::cin >> tests;
	for (long long currtest = 1; currtest <= tests; currtest++)
	{
		long long l, t, n, c;
		std::cin >> l >> t >> n >> c; t /= 2;
		vector<long long> dists(c);
		for (long long i = 0; i < c; i++)
			std::cin >> dists[i];
			
		long long cyclen = 0;
		for (long long i = 0; i < c; i++) cyclen += dists[i];
		
		long long ans = cyclen * (n / c) * 2;
		for (long long i = 0; i < n%c; i++) ans += dists[i] * 2;
		
		if (t < ans/2)
		{
			long long remcycs = (n / c) - (t / cyclen) - 1;
			
			std::priority_queue<seg> heap;
			
			if (remcycs > 0)
				for (long long i = 0; i < c; i++)
					heap.push(seg(dists[i], remcycs));
				
			long long rt = t % cyclen;
			for (long long i = 0; i < (remcycs == -1 ? n%c : c); i++)
				if (rt == 0) heap.push(seg(dists[i], 1));
				else if (rt < dists[i]) {heap.push(seg(dists[i]-rt, 1)); rt = 0;}
				else rt -= dists[i];
				
			if (remcycs != -1) for (long long i = 0; i < n % c; i++) heap.push(seg(dists[i], 1));
			
			while (l > 0 && !heap.empty())
			{
				long long len = heap.top().len, cnt = heap.top().cnt; heap.pop();
				
				if (l >= cnt)
				{
					ans -= cnt * len;
					l -= cnt;
				} else
				{
					ans -= l * len;
					l = 0;
				}
			}
		}
		
		std::cout << "Case #" << currtest << ": " << ans << '\n';
	}

	return 0;
}
