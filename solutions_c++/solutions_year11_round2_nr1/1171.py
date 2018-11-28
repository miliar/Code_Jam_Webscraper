#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

struct Team
{
	double p[3];
	int cnt;
};

const int N = 102;
int n;
Team t[N];

char m[N][N];

int main()
{
	freopen("E:/input.txt", "r", stdin);
	freopen("E:/output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 0; k < T; ++k)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				cin >> m[i][j];
		}
		for (int z = 0; z < 3; ++z)
		{
			for (int i = 0; i < n; ++i)
			{
				double sum = 0;
				int cnt = 0;
				for (int j = 0; j < n; ++j)
					if (m[i][j] != '.')
					{
						++cnt;
						if (z == 0)
							sum += (m[i][j] - '0');
						else
						{
							double tmp = t[j].p[z - 1];
							if (z == 1)
							{
								double ans = tmp * t[j].cnt - (m[j][i] - '0');
								ans /= (t[j].cnt - 1);
								sum += ans;
							}
							else
								sum += tmp;
						}
					}
				t[i].p[z] = sum / cnt;
				t[i].cnt = cnt;
			}
			int zz = 3;
		}
		printf("Case #%d:\n", k + 1);
		for (int i = 0; i < n; ++i)
		{
			double res = 0.25 * t[i].p[0] + 0.5 * t[i].p[1] + 0.25 * t[i].p[2];
			printf("%.12lf\n", res);
		}
	}
	return 0;
}