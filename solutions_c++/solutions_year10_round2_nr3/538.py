#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int C;
	cin >> C;
	for (int c = 0; c < C; ++c)
	{
		int n;
		scanf("%d", &n);

		int cnt = 0;
		for (int m = 1; m < (1<<(n-1)); ++m)
		{
			if ( m & (1<<(n-2)) )
			{
				int tmp = n-2;
				while ( 1 )
				{
					if ( !(m & (1<<tmp)) ) break;
					int k = 0;
					for (int i = tmp; i >= 0; --i)
					{
						if (m & (1<<i)) k++;
					}
					tmp = (k == 1) ? 1 : k-2;
					if ( k == 1 )
					{
						if ( tmp == 1 )
						{
							cnt++;
							cnt %= 100003;
						}
						break;
					}
				}				

			}
		}

		printf("Case #%d: %d\n", c+1, cnt);

	}



	return 0;
}