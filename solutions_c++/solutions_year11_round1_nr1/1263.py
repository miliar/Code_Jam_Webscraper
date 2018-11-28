#include <iostream>
using namespace std;

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n,pd,pg;
		cin >> n >> pd >> pg;
	
		bool poss = false;
		for (int d = 1; d <= n; d++)
		{
			int k = pd*d;
			if (k % 100 == 0)
			{
				k /= 100;
				int won = k;
				int lost = d-k;
				int p = 100-pg;
				for (int g = d; g <= 1000000; g++)
				{
					int r = pg*g;	
					if (r % 100 == 0)
					{
						r /= 100;
						int won1 = r;
						int lost1 = g-r;
						if (won1 >= won && lost1 >= lost) poss = true;
					}
				}
			}
		}
		if (poss) cout << "Case #" << T << ": Possible\n";
		else cout << "Case #" << T << ": Broken\n";
	}
}
					
