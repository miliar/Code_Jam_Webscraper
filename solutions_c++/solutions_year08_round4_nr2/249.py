#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int trisize2(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return abs((y1+y2)*(x2-x1)+(y2+y3)*(x3-x2)-(y1+y3)*(x3-x1));
}

int main()
{
	int N;
	cin >> N;
	for (int tc = 0; tc < N; tc++)
	{
		int n,m,a;
		int x1,y1,x2,y2,x3,y3;
		cin >> n >> m >> a;
		bool fin = false;
		if (a>m*n)
		{
			cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl;
			continue;
		}
		for (int i=1; i*i<=a; i++)
			if (a%i == 0)
				if (((i<=n) && (a/i<=m)))
				{
					fin = true;
					x1 = 0;
					y1 = 0;
					x2 = i;
					y2 = 0;
					x3 = 0;
					y3 = a/i;
				}
				else
				if ((i<=m) && (a/i<=n))
				{
					fin = true;
					x1 = 0;
					y1 = 0;
					x2 = 0;
					y2 = i;
					x3 = a/i;
					y3 = 0;
				}
		if (!fin)
		{
			for (x1=0; x1<=n; x1++)
				for (y1=0; y1<=m; y1++)
					for (x2=0; x2<=n; x2++)
						for (y2=0; y2<=m; y2++)
							for (x3=0; x3<=n; x3++)
								for (y3=0; y3<=m; y3++)
									if (trisize2(x1,y1,x2,y2,x3,y3) == a)
									{
										fin = true;
										goto end;
									}
		}
end:	if (fin)
			cout << "Case #" << tc+1 << ": " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
		else
			cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}

