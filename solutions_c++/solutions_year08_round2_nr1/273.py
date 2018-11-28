#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

long long num[3][3], ans;

int main ()
{
	int tests, test;
	long long n, A, B, C, D, x0, y0, M, X, Y;
	cin >> tests;
	for (test = 1; test <= tests; ++test) {
		memset(num, 0, sizeof(num));
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		X = x0; Y = y0;
		num[X%3][Y%3]++;
		for (int i = 1; i < n; ++i) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			num[X%3][Y%3]++;
		}

		ans = 0;
		/*
		ans += num[0][0] * (num[0][0]-1) * (num[0][0]-2) / 6;
		ans += num[1][1] * (num[1][1]-1) * (num[1][1]-2) / 6;
		ans += num[2][2] * (num[2][2]-1) * (num[2][2]-2) / 6;
*/
		for (int a0 = 0; a0 < 3; ++a0)
		for (int b0 = 0; b0 < 3; ++b0)
			for (int a1 = a0; a1 < 3; ++a1)
			for (int b1 = 0; b1 < 3; ++b1)
			{
				if (a1 == a0 && b1 < b0) continue;
				for (int a2 = a1; a2 < 3; ++a2)
				for (int b2 = 0; b2 < 3; ++b2)
				{
					if (a2 == a1 && b2 < b1) continue;

					if ((a0+a1+a2)%3 == 0 && (b0+b1+b2)%3 == 0)
					{
						if (a0 == a1 && a1 == a2 && b0 == b1 && b1 == b2) {
							if (num[a0][b0]>1)
							ans += num[a0][b0] * (num[a0][b0]-1) * (num[a0][b0]-2) / (long long)6;
						}

						else if (a0 == a1 && b0 == b1) {
							if (num[a0][b0]>0)
							ans += num[a0][b0] * (num[a0][b0]-1) * num[a2][b2] /(long long) 2;
						}
						else if (a0 == a2 && b0 == b2) {
							if (num[a0][b0]>0)
							ans += num[a0][b0] * (num[a0][b0]-1) * num[a1][b1] /(long long) 2;
						}
						else if (a1 == a2 && b1 == b2) {
							if (num[a1][b1]>0)
							ans += num[a1][b1] * (num[a1][b1]-1) * num[a0][b0] /(long long) 2;
						}
						else
							ans += num[a0][b0] * num[a1][b1] * num[a2][b2];
					}
				}
			}

			cout << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}