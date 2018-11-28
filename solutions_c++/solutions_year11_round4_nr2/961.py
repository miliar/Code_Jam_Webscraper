#include <cstdio>
#include <iostream>
#include <algorithm>

#define N 500
#define eps (1e-2)

using namespace std;

int w[N][N];

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int r, c, d;
		cin >> r >> c >> d;
		//cout << r << " " << c << " " << d << endl;
		for (int j = 0; j < r; j++)
			for (int k = 0; k < c; k++)
			{
				char sym;
				cin >> sym;
				w[j][k] = int(sym - '0') + d;
				//cout << w[j][k] << " ";
			}

		bool ok = false;

		for (int ans = min(r, c); ans >= 3; ans--)
		{		
			for (int x1 = 0; x1 + ans <= r; x1++)
			{
				for (int y1 = 0; y1 + ans <= c; y1++)
				{
					int sum = 0, vx = 0, vy = 0;

					for (int a = x1; a < x1 + ans; a++)
						for (int b = y1; b < y1 + ans; b++)
							if ( (a != x1 && a != x1 + ans - 1) || (b != y1 && b != y1 + ans - 1) )
     						{
     							vx += a * w[a][b];
     							vy += b * w[a][b];
     							sum += w[a][b];					
     						}		
				//	cout << ans << " " << x1 << " " << y1 << " " << xc1 << " " << yc1 << endl;

					if ( vx * 2 == (2 * x1 + ans - 1) * sum && vy * 2 == (2 * y1 + ans - 1) * sum )					
						ok = true;					
				}			
				if (ok) break;
			}

			if (ok)
			{
				cout << "Case #" << i + 1 << ": " << ans << endl;
				break;
			}
		}

		if (!ok)
			cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";

	}	
	return 0;
}

