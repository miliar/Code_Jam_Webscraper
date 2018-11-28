#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("inp.txt", "r", stdin);	
	freopen("outp.txt", "w", stdout);
	int t, scor[111];
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		int n, s, p;
		cin >> n >> s >> p;
		int x = 0, y1 = 0, y2 = 0, z = 0, w = 0;
		for (int j=0;j<n;j++)
		{
			cin >> scor[j];
			if (scor[j] >= p + 2*max(0, p-2))
			{
				x++;
				if (scor[j] <= 28 && scor[j] >= 2)
				{
					y2++;
					if (scor[j] < 3*p-2)
						y1++;
				}
			}
			else
			{
				z++;
				if (scor[j] <=28 && scor[j]>=2)
					w++;
			}
		}
		int ans = -1;
		if (s >= y1 && s <= y2)
			ans = x;
		else if (s < y1)
			ans = x + s - y1;
		else
		{
			if (y2+w>=s)
				ans = x;
			else
				ans = x - s + w + y2;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}