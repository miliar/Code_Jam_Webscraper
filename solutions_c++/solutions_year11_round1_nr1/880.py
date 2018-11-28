#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

typedef long long ll;



//bool myf(mark a, mark b)
//{
//	return ((a.z > b.z)||((a.z == b.z)&&(a.pos < b.pos)));
//}

ll n, i, j, t, pg, pd, w;
bool can;

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
	#endif
	cin >> t;
	for(j = 1; j <= t; j++)
	{
		can = 0;
		cin >> n >> pd >> pg;
		if(((pg == 100)&&(pd < 100))||((pg == 0)&&(pd > 0)))
			cout << "Case #" << j << ": Broken" << endl;
		else
		{
			if(n > 100000)
				n = 100000;
			for(i = 1; i <= n; i++)
			{
				w = (i * pd) / 100;
				if(((i * pd) % 100 == 0)&&(w <= i)&&
					((100*w)%i == 0)&&((100*w)/i==pd))
					can = 1;
			}
				
			if(can)
				cout << "Case #" << j << ": Possible" << endl;
			else
				cout << "Case #" << j << ": Broken" << endl;
		}
	}
	return 0;
}