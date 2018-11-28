#include <iostream>
using namespace std;

//#define DEBUG 1

int main()
{
	int t;
	cin >> t;
	for (int tc=1; tc<=t; tc++)
	{
		unsigned long r,k,n;
		unsigned long *g;
		unsigned long long sum = 0, cs = 0;
		cin >> r >> k >> n;
		unsigned long long *s = new unsigned long long[n];
		g = new unsigned long[n];
		bool hassmall = false;
		for (int i=0; i<n; i++)
		{
			cin >> g[i];
			if (g[i] <= k)
			{
				hassmall = true;
				sum += g[i];
			}
		}

		if (sum <= k)
		{
			cout << "Case #" << tc << ": " << sum * r << endl;
		} else if (!hassmall)
		{
			cout << "Case #" << tc << ": " << 0 << endl;
		} else {
			unsigned long *gx = new unsigned long[n];
			int nn = 0;
			for (int i=0; i<n; i++)
			{
				if (g[i] <= k)
				{
					gx[nn] = g[i];
					nn++;
				}
			}
			delete []g;
			g = gx;
			n = nn;

			int cr = 0;
			int *acc = new int[n];
			for (int i=0; i<n; i++) acc[i] = 0;
			int cg = 0;
			int cp = 0;
			bool found = false;

			while (true)
			{
				cr++;
				if (acc[cg] != 0)
				{
					// Duplicated!
					found = true;
					break;
				}
				int xg = cg;
				while (true)
				{
					cp += g[xg];
					if (cp > k)
					{
						cp = cp - g[xg];
						acc[cg] = cr;
						s[cg] = cs;
						cs += cp;
						break;
					}
					xg = (xg + 1) % n;
				}
				cg = xg;
				cp = 0;
				if (cr == r)
					break;
			}

			if (!found)
			{
				cout << "Case #" << tc << ": " << cs << endl;
			} else {
#ifdef DEBUG
				cout << cg << ' ' << acc[cg] << ' ' << cr << endl;
#endif
				unsigned long long tsum = 0;
				r = r - (acc[cg] - 1);
				tsum += s[cg];
				int diff = cr - acc[cg];
				int rnds = r / diff;
				int left = r % diff;
				tsum += rnds * (cs - s[cg]);

				cs = 0;
				for (int i=0; i<left; i++)
				{
					int xg = cg;
					while (true)
					{
						cp += g[xg];
						if (cp > k)
						{
							cp = cp - g[xg];
							cs += cp;
							break;
						}
						xg = (xg + 1) % n;
					}
					cg = xg;
					cp = 0;
				}
				tsum += cs;
				cout << "Case #" << tc << ": " << tsum << endl;
			}
		}

		delete []g;
		delete []s;
	}
	return 0;
}
