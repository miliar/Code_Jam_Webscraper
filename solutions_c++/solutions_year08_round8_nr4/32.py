#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <functional>
#include <numeric>
#include <cmath>
#include <utility>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

const int M = 30031;

int f[1005][1<<10];

int main()
{
	ifstream ifs("d.in");
	ofstream ofs("d.out");
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		memset(f, 0, sizeof(f));
		int n, k, d;
		ifs >> n >> k >> d;
		ofs << "Case #" << l+1 << ": ";
		if (d < k)
		{
			ofs << "0\n";
		}
		else 
		{
			f[k-1][(1<<k)-1] = 1;
			int q = (1<<d)-1;
			for (int i = k; i < n; ++i)
			{
				for (int j = 0; j < (1<<d); ++j)
				{
					if (f[i-1][j] > 0)
					{
						if (j & (1<<(d-1)))
						{
							int newj = ((j<<1) & q) | 1;
							f[i][newj] = (f[i][newj]+f[i-1][j]) % M;
						}
						else
						{
							for (int z = 0; z < d; ++z)
								if (j & (1<<z))
								{
									int newj = j & ~(1<<z);
									newj = (newj << 1) | 1;
									f[i][newj] = (f[i][newj]+f[i-1][j]) % M;
								}
						}
					}
				}
			}
			int sum = 0;
			ofs << f[n-1][(1<<k)-1] << endl;
		}

	}
	return 0;
}