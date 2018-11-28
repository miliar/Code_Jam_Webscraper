#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <string.h>

using namespace std;

int main()
{
//#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
//#endif

	int n, a, s, p, i, j, k, z1, z2, ans=0, t;
	vector<int> v;

	cin >> t;
	for (int ti = 0; ti < t; ti++)
	{
		cin >> n >> s >> p;
		
		ans = 0;
		if (p == 0)
		{
			cout << "Case #" << ti+1 <<": " << n << endl;
			string recs;
			getline(cin, recs);
		}
		else 
		{
			for (int i = 0; i <n; i++)
			{
				cin >> k;
				int mx;
				int r = 1;
				if (k == 0)
				{
					mx = 0;
				}
				else if (k == 1)
				{
					mx = 1;
				}
				else
				{
					r = k % 3;
					if (r == 0)
					{
						mx = k / 3;
					}
					else
						mx = k / 3 + 1;
				}

				if (mx >= p)
					ans++;
				else
				{
					if (s > 0)
					{
						if (r != 1)
						{
							if (mx + 1 >= p && mx + 1 <= 10)
							{
								ans++;
								s--;
							}
						}
					}
				}
			}
			
			cout << "Case #" << ti+1 <<": " << ans << endl;
		}
	}

	return 0;
}