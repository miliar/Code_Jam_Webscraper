#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;


int main()
{
#if 1
	ifstream cin("b.in");
	ofstream cout("b.out");
#else
	ifstream cin("a.txt");
#endif
	int n, m, a;

	int z;
	cin>>z;
	for (int tc = 1 ; tc <= z ; tc++)
	{
		cout<<"Case #"<<tc<<": ";
		cin>>n>>m>>a;

		int x1 = 0;
		

		bool found = false;
		for (int y2 = 0 ; y2 <= m ; y2++)
			for (int x2 = 0 ; x2 <= n && !found ; x2++)
				for (int x3 = 0 ; x3 <= n && !found ; x3++)
					for (int y3 = 0 ; y3 <= m && !found ; y3++)
					{
						if (x3 - x2 == 0) continue;
						if ((a-x2*y3)%(x3 - x2)) continue;
						int y1 = (x2*y3 - a)/(x3 - x2);

						if (y1 < 0) y1 = -y1;
						if (y1 < 0 || y1 > m) continue;
						if (abs(x1*y2 - y1*x2 + y1*x3 - x1*y3 + x2*y3 - x3*y2) != a) continue;


						found = true;
						cout<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<' '<<x3<<' '<<y3<<endl;
				
					}
		if (!found) cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

