#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
#define pb push_back
#define mp make_pair
#define X first
#define Y second

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
/*
X = x0, Y = y0
print X, Y
for i = 1 to n-1
  X = (A * X + B) mod M
  Y = (C * Y + D) mod M
  print X, Y
*/
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{
		int n; cin >> n;
		LL A, B, C, D, x0, y0, M;
		cin >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector< pair<LL, LL> > a;

		LL X = x0;
		LL Y = y0;
		a.pb(mp(X, Y));
		for(int i = 1; i <= n -1; ++i)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			a.pb(mp(X, Y));
		}

		LL q[3][3];
		memset(q, 0, sizeof q);
		for(int i = 0; i < n; ++i)
			q[a[i].X % 3][a[i].Y % 3]++;

		LL res = 0;
		for(int i1 = 0; i1 < 3; ++i1)
		for(int j1 = 0; j1 < 3; ++j1)
		for(int i2 = 0; i2 < 3; ++i2)
		for(int j2 = 0; j2 < 3; ++j2)
		for(int i3 = 0; i3 < 3; ++i3)
		for(int j3 = 0; j3 < 3; ++j3)
			if((i1 + i2 + i3) % 3 == 0 && 
				(j1 + j2 + j3) % 3 == 0 && q[i1][j1] && q[i2][j2] && q[i3][j3])
			{
				if((i1 != i2 || j1 != j2) && (i1 != i3 || j1 != j3) &&
					(i3 != i2 || j3 != j2))
					res += q[i1][j1] * q[i2][j2] * q[i3][j3];
				else
				{
			/*		if((i1 == i2 && j1 == j2) && (i1 != i3 || j1 != j3) &&
					(i3 != i2 || j3 != j2))
						res += q[i1][j1] * (q[i1][j1] - 1) * q[i3][j3];
					else
						if((i1 != i2 || j1 != j2) && (i1 == i3 && j1 == j3) &&
							(i3 != i2 || j3 != j2))
								res += q[i1][j1] * (q[i2][j2]) * (q[i3][j3] - 1);
						else
							if((i1 != i2 || j1 != j2) && (i1 != i3 || j1 != j3) &&
							(i3 == i2 && j3 == j2))
								res += q[i1][j1] * (q[i2][j2]) * (q[i3][j3] - 1);
							else
								res += q[i1][j1] * (q[i2][j2] - 1) * (q[i3][j3] - 2);
								*/
				}
			}
		for(int i1 = 0; i1 < 3; ++i1)
		for(int j1 = 0; j1 < 3; ++j1)
		for(int i2 = 0; i2 < 3; ++i2)
		for(int j2 = 0; j2 < 3; ++j2)
			if((i1 + i1 + i2) % 3 == 0 && (j1 + j1 + j2) % 3 == 0  && (i1 != i2 || j1 != j2))
				res += q[i1][j1] * (q[i1][j1] - 1) * q[i2][j2];
		for(int i1 = 0; i1 < 3; ++i1)
		for(int j1 = 0; j1 < 3; ++j1)
			res += q[i1][j1] * (q[i1][j1] - 1) * (q[i1][j1] - 2);
		//cnt /= 3;
		res /= 6;

		cout << "Case #" << z << ": " << res << endl;
	}


	return 0;
}