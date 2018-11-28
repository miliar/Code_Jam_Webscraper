#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void solve()
{
	string file = "B-large";
	freopen((file + ".in").c_str(), "rt", stdin);
	freopen((file + ".out").c_str(), "wt", stdout);

	int T, t, N, n, S, p;
	string line;
	cin >> T >> ws;
	t = 1;
	while(T--)
	{
		cout << "Case #" << t++ << ": ";
		cin >> N >> S >> p;
		int y = 0;
		while(N--)
		{
			cin >> n;
			int q = n / 3;
			if(q >= p) y++;
			else if(p * 3 - n < 3) y++;
			else if(S > 0 && (p * 3 - n < 5 && p <= n))
			{
				y++;
				S--;
			}
		}
		cout << y << endl;
	}
}