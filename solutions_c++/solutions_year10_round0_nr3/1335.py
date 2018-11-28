#include <iostream>
using namespace std;

int main()
{
	int T, R, k, N;
	int i, j, l, m, table[1000] = {0}, cnt;
	long long rc;
	int cost;

	cin >> T;

	for(i = 0; i < T; ++i)
	{
		cin >> R >> k >> N;

		for(j = 0; j < N; ++j)
			cin >> table[j];

		cost = 0;
		m = 0;
		for(l = 0; l < R; ++l)
		{
			rc = 0;
			cnt = 0;
			for(;;++m, ++cnt)
			{
				rc += table[m%N];
				if(rc > k || cnt >= N){ rc -= table[m%N]; break; }
			}
			cost += rc;
		}

		cout << "Case #" << i+1 << ": " << cost << endl;
	}
	return 0;
} 