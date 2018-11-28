#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n, s, p;
		cin >> n >> s >> p;
		int p2 = p * 3;
		int c = 0;
		for (int j = 0; j < n; j++)
		{
			int r;
			cin >> r;
			if (r + 2 >= p2)
				c++;
			else if (s > 0)
				if (r + 4 >= p2)
				{
					int dif = p2 - r;
					if (p - 2 >= 0)
						s--, c++;
				}
		}
		cout << "Case #" << i + 1 << ": " << c << endl;
	}
}