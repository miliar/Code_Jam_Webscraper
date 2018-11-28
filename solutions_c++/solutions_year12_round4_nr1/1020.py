#include <iostream>
#include <iomanip>
#include <queue>
#include <vector>
#include <set>

using namespace std;

int main()
{
	freopen("inp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t, d[10011], l[10011];
	//set< int > v[10011];
	int v[10011];
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		int n, D;
		cin >> n;
		for (int j=0;j<n;j++)
			cin >> d[j] >> l[j];
		cin >> D;		
		int can = 0;
		for (int y=0;y<n;y++)
			v[y] = D+1;
		v[0] = 0;
		for (int y=0;y<n && !can;y++)
		{
			if (v[y]!=D+1)
			{
				int x = v[y];
				if (D <= 2*d[y]-x)
				{
					can = 1;
					break;
				}
				for (int h=y+1;h<n;h++)
					if (d[h]<=2*d[y]-x)
					{
						if (l[h]>=d[h]-d[y])
							v[h] = min(v[h], d[y]);
						else
							v[h] = min(v[h], d[h]-l[h]);
					}
			}
		}
		cout << "Case #" << i << ": ";
		if (can)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}