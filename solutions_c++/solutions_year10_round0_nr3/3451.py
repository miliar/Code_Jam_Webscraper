#include<algorithm>
#include<cmath>
#include<iostream>
#include<iterator>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	// Meaningful variable names.
	int T, R, k, N, g, peo, pos, tmp, m, tp;
	cin >> T;
	for (int i=1; i<=T; ++i)
	{
		vector<int> groups;
		tp = 0;
		cin >> R >> k >> N;
		for (int j=0; j<N; ++j)
		{
			cin >> g;
			groups.push_back(g);
			tp += g;
		}
		
		pos = 0;
		m = 0;
		if (tp > k)
		{
			for (int r=0; r<R; ++r)
			{
				peo=0;
				while ((tmp = peo+groups[pos]) <= k)
				{
					peo = tmp;
					pos = (pos+1) % N;
				}
				m += peo;
			}
		}
		else
			m = R * tp;
		cout << "Case #" << i << ": " << m << endl;
	}
	
	return 0;
}