#include <iostream>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n, k;
		scanf("%d %d", &n, &k);

		bool res = true;

		for (int i = 0; i < n; ++i)
		{
			if ( ! (k & (1<<i)) )
			{
				res = false;
				break;
			}
		}
		
		if ( res )
		{
			printf("Case #%d: ON\n", t+1);
		}
		else
		{
			printf("Case #%d: OFF\n", t+1);
		}

	}


	return 0;
}