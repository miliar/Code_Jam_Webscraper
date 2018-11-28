#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <cmath>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		long long n, pd, pg;
		cin >> n >> pd >> pg;
	
		string ret;
		if ( pg == 100 and pd < 100 ) ret = "Broken";
		else if ( pg == 0 and pd > 0 ) ret = "Broken";
		else if ( pd == 0 ) ret = "Possible";
		else
		{
			bool ok = 0;
			for (int i = 1; i <= min(n, 100LL); ++i)
			{
				if ((i*pd) % 100 == 0)
				{
					ok = 1;
					//cout << i << endl;
				}
			}
			if (ok) ret = "Possible";
			else ret = "Broken";
		}
	
		cout << "Case #" << C << ": " << ret << endl;
	}
}
