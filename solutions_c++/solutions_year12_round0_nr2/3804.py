#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int N, S, p;

		cin >> N >> S >> p;

		int ok = 0;
		int ns = 0;
		for (int i = 0; i < N; i++)
		{
			int k;
			cin >> k;

			k -= p;
			if (k < 0)
				continue;
			if (k / 2 >= p-1)
				ok++;
			if (k / 2 == p-2)
				ns++;
		}

		cout << "Case #" << t << ": " << ok + min(S, ns) << endl;
	}
}