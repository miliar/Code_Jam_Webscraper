
#include <iostream>

using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int kase=1; kase<=N; kase++)
	{
		int n;
		long long A, B, C, D, x, y, M;
		cin >> n >> A >> B >> C >> D >> x >> y >> M;
		int num[3][3];
		memset(num, 0, 3*3*sizeof(int));
		for (int i=0; i<n; i++)
		{
			num[x%3][y%3]++;
			x = (A * x + B) % M;
			y = (C * y + D) % M;
		}
		long long sol = 0;
		for (int v1=0; v1<9; v1++)
			for (int v2=v1; v2<9; v2++)
				for (int v3=v2; v3<9; v3++)
				{
					int x1 = v1 / 3;
					int y1 = v1 % 3;
					int x2 = v2 / 3;
					int y2 = v2 % 3;
					int x3 = v3 / 3;
					int y3 = v3 % 3;
					if ((x1+x2+x3)%3)
						continue;
					if ((y1+y2+y3)%3)
						continue;
					long long mult = 1;
					long long fac1 = num[x1][y1];
					long long fac2 = num[x2][y2];
					if (x2 == x1 && y2 == y1)
					{
						fac2--;
						mult = 2;
					}
					long long fac3 = num[x3][y3];
					if (x3 == x2 && y3 == y2)
					{
						fac3--;
						mult = 2;
					}
					if (x3 == x1 && y3 == y1)
					{
						fac3--;
						mult = 6;
					}
					sol += (fac1 * fac2 * fac3) / mult;
				}
		cout << "Case #" << kase << ": " << sol << endl;
	}
}
