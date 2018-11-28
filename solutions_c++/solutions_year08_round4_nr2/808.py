// B.cpp
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int C;
	cin >> C;
	for (int cnt = 1; cnt <= C; cnt++)
	{
		long long N, M, A;
		cin >> N >> M >> A;
		cout << "Case #" << cnt << ": ";
		if (N * M < A)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			bool found = false;
			long long xR, yR;
			for (int x = 1; x <= N; x++)
			{
				if (A % x == 0 && A / x <= M)
				{
					// Found Solution
					xR = x;
					yR = A / x;
					found = true;
				}
			}
			if (found)
			{
				cout << "0 0 0 " << yR << " " << xR << " " << yR << endl;
			}
			else
			{
				int xR1, yR1, xR2, yR2;
				for (int x = 0; x <= N; x++)
					for (int y = 0; y <= M; y++)
						for (int x2 = 0; x2 <= x; x2++)
							for (int y2 = 0; y2 <= M; y2++)
								if (abs(x2*y - x*y2) == A)
								{
									xR1 = x;
									yR1 = y;
									xR2 = x2;
									yR2 = y2;
									found = true;
									break;
								}
				if (found)
					cout << "0 0 " << xR1 << " " << yR1 << " " << xR2 << " " << yR2 << endl;
				else
					cout << "IMPOSSIBLE" << endl;
			}
		}
	}
}

