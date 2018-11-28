#include <iostream>
#include <vector>
#include <cmath>


using namespace std;


int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int res = 0;

		int N, S, P;
		cin >> N >> S >> P;

		int glimit = max(0, 3 * P - 2);
		
		for (int i = 0; i < N; i++)
		{
			int val;
			cin >> val;

			if (val < P)
				continue;

			if (val >= glimit)
			{
				res++;
				continue;
			}

			if (val < 3 * P - 4)
				continue;

			if (S == 0)
				continue;
			S--;
			res++;
		}

		cout << "Case #" << t << ": " << res << endl;
	}


	return 0;
}