#include <iostream>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

typedef vector<int> VI;
typedef map<int,int> MII;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int n, k, p;
		cin >> n >> k >> p;
		MII m[n];
		int full = (1 << k)-1;
		m[k-1][full] = 1;
		for (int i=k; i<n; i++) // fill positions k to n-1
		{
			for (MII::iterator it = m[i-1].begin(); it != m[i-1].end(); ++it)
			{
				int mask = it->first;
				int num = it->second;
				//cout << i << " " << num << ": " << mask << endl;
				if ((mask >> p))
					continue;
				for (int j=0; j<p; j++)
				{
					if ((mask >> j) & 1)
					{
						int rem = (1 << j);
						rem = ~rem; // TODO check
						int newmask = mask & rem;
						newmask = (newmask << 1) | 1;
						m[i][newmask] = (m[i][newmask] + num) % 30031;
						//cout << " enter " << i << " " << newmask << " +" << num << endl;
					}
				}
			}
		}
		cout << "Case #" << kase << ": ";
		cout << m[n-1][full] << endl;
	}
	return 0;
}
