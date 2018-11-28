#include <iostream>
#include <memory.h>
#include <cmath>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef string answer_type;

const int N = 550;

typedef long long llong;

llong W[N][N];

llong mabs(llong x)
{
	return (x < 0) ? -x : x;
}

struct vt
{
	llong x, y;
	vt(llong _x, llong _y) : x(_x), y(_y)
	{}
	friend vt operator +(vt a, vt b)
	{
		return vt(a.x + b.x, a.y + b.y);
	}
	friend vt operator *(vt a, llong k)
	{
		return vt(a.x * k, a.y * k);
	}
	vt(){}
	friend vt operator *(llong k, vt a)
	{
		return a * k;
	}
	friend vt operator -(vt a, vt b)
	{
		return a + b * (-1);
	}
	llong abs()
	{
		return mabs(x) + mabs(y);
	}
};


//double mass[N][N];
//vt sum[N][N];

vt vsum[N][N];

llong gsum(int y1, int x1, int y2, int x2)
{
	return W[y2][x2] + W[y1 - 1][x1 - 1] - W[y2][x1 - 1] - W[y1 - 1][x2];
}

vt gvsum(int y1, int x1, int y2, int x2)
{
	return vsum[y2][x2] + vsum[y1 - 1][x1 - 1] - vsum[y2][x1 - 1] - vsum[y1 - 1][x2];
}

llong gsum(int y, int x)
{
	return gsum(y, x, y, x);
}

vt gvsum(int y, int x)
{
	return gvsum(y, x, y, x);
}

answer_type solve()
{
	int r, c, d;
	cin >> r >> c >> d;
	memset(vsum, 0, sizeof(vsum));
	char tmp;
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
		{
			cin >> tmp;
			W[i][j] = tmp - '0';
			vsum[i][j] = W[i][j] * vt(i, j) + vsum[i - 1][j] + vsum[i][j - 1] - vsum[i - 1][j - 1];
			W[i][j] = W[i][j] + W[i - 1][j] + W[i][j - 1] - W[i - 1][j - 1];
		}

	int ans = 0;
		
	for (int k = 3; k <= min(r, c); k++)
	{
		for (int i = 1; i <= r - k + 1; i++)
			for (int j = 1; j <= c - k + 1; j++)
			{
				llong sum = gsum(i, j, i + k - 1, j + k - 1);
				llong msum = gsum(i, j) + gsum(i, j + k - 1) + gsum(i + k - 1, j) + gsum(i + k - 1, j + k - 1);
				sum -= msum;
				vt vv = gvsum(i, j, i + k - 1, j + k - 1);
				vt mvv = gvsum(i, j) + gvsum(i, j + k - 1) + gvsum(i + k - 1, j) + gvsum(i + k - 1, j + k - 1);
				vv = vv + (-1) * mvv;
				vv = vv * 2;
				vt mm = vt(2 * i + k - 1, 2 * j + k - 1);
				mm = mm * sum;
				if ((vv + (-1) * mm).abs() == 0)
					ans = max(ans, k);
			}
	}
	stringstream ss;
	
	if (ans == 0)
		ss << "IMPOSSIBLE";
	else
		ss << ans;
	return ss.str();
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
