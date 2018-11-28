
#include <iostream>

using namespace std;

long long unsigned int i(int a)
{
	return 100/a;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t < T+1; t++)
	{
		long long unsigned int M;
		int pd, pt;
		cin >> M >> pd >> pt;

		bool possible = false;
		if (pt < 100 && pt > 0)
		{
			/*if (M >= 100)
			{
				possible = true;
			} else*/
			{
				int a = 1;
				int p = pd;
				if (p % 2 == 0) { a *= 2; p /= 2; }
				if (p % 2 == 0) { a *= 2; p /= 2; }
				if (p % 5 == 0) { a *= 5; p /= 5; }
				if (p % 5 == 0) { a *= 5; p /= 5; }
				if (M >= (100/a)) possible = true;
				//cout << "possibility as: " << pd << " " << a << " " << (100/a) << " " << possible << endl;
			}
		} else if (pt == 100 && pd == 100)
		{
			possible = true;
		} else if (pt == 0 && pd == 0)
		{
			possible = true;
		}

		cout << "Case #" << t << /* " (" << M << " " << pd << " " << pt << ")" << */ ": " << (possible? "Possible" : "Broken") << endl;
	}
}

