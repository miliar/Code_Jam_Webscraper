#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "B-small-attempt0.in.txt"
#define OUTPUTFILENAME "output.txt"

long n, m, area;

void init()
{
	cin >> n >> m >> area;
}

void solve(int testnumber)
{
	for (int a = 0; a <= n; a++)
		for (int b = 0; b <= m; b++)
		{
			if (a * b == area)
			{
				cout << "Case #" << testnumber << ": 0 0 " << a << " 0 0 " << b << endl;
				return;
			}
			else
				if (a * b > area)
					for (int c = 1; c <= b; c++)
					{
						int d = (a * b - area) / c;
						if (a * b - c * d == area)
						{
							cout << "Case #" << testnumber << ": 0 0 " << a << ' ' << c << ' ' << d << ' ' << b << endl;
							return;
						}
					}
		}
	cout << "Case #" << testnumber << ": IMPOSSIBLE" << endl;
}	

int main()
{
	int testnumber;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> testnumber;
	for (int i = 0; i < testnumber; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}