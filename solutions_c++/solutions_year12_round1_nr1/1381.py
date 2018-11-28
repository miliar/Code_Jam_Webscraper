#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int a, b;
		cin >> a >> b;
		
		vector<double> p(a);
		for (int i = 0; i < a; i++)
		{
			cin >> p[i];
		}

		double r = b + 2, g = 1, h;
		for (int i = 0; i <= a; i++)
		{
			r = min(r, g * (b - a + 2 * (a - i) + 1) + (1 - g) * (b + 1 + b - a + 2 * (a - i) + 1));
			if (i < a)
			{
				g *= p[i];
			}
		}
		
		/*int maxMask = 1 << a;
		vector<double> e(maxMask);

		for (int mask = 0; mask < maxMask; mask++)
		{
			e[mask] = 1.0;
			for (int i = 0; i < a; i++)
			{
				e[mask] *= (!((mask >> i) & 1)) ? p[i] : 1.0 - p[i];
			}
		}

		double r = ~(1 << 31);

		// keep typing
		r = min(r, e[0] * (b - a + 1) + (1 - e[0]) * (b - a + 1 + b + 1));
		// press enter
		r = min(r, b + 2.0);

		// backspaces
		for (int i = 1; i <= a; i++)
		{
			double t = 0;
			for (int mask = 0; mask < maxMask; mask++)
			{
				bool isValid = mask < (1 << i);
				t += e[mask] * (isValid ? i + b - a + i + 1 : b + 1 + i + b - a + i + 1);
			}
			r = min(r, t);
		}*/

		//cout << "Case #" << tc << ": " << r << endl;
		printf("Case #%d: %.6lf\n", tc, r);
	}

	return 0;
}