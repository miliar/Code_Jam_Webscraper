#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, N, S, p, t;

vector<int> v(3);

main()
{
	cin >> T;
	int i, c;
	for (int caso = 1; caso <=T; ++caso)
	{
		c = 0;
		int s = 0;
		cin >> N >> S >> p;
		for (i = 0; i < N; ++i)
		{
			cin >> t;
			v[0] = t/3;
			t -= v[0];
			v[1] = t/2;
			v[2] = t - v[1];
			sort(v.begin(), v.end());
			if (v[2] >= p)
				++c;
			else if (S)
			{
				++v[2];
				--v[1];
				if (v[1] < 0)
					continue;	
				sort(v.begin(), v.end());
				if(v[2] - v[0] <= 2)
				{
					if (v[2] >= p)
					{
						--S;
						++c;
					}
				}
			}
		}
		cout << "Case #" << caso << ": " << c << endl;
	}
}








