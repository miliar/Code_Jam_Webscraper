#include <iostream>
#define TRUE 1
#define FALSE 0
#define lint long long

using namespace std;

int main()
{
	int ncases, ccase = 0;
	cin >> ncases;
	while (ccase++ < ncases)
	{
		int possible = FALSE;
		lint n, pd, pg;
		cin >> n >> pd >> pg;
		for (lint i=1; i<=n; i++)
		{
			lint w = pd * i / 100;
			if ((100 * w) == (pd * i)){
				possible = !(((pd < 100) && (pg == 100))||((pd > 0) && (pg == 0)));
				if (possible) break;
			}
		}
		cout << "Case #" << ccase << ": " << (possible? "Possible": "Broken") << endl;
	}
	return 0;
}
