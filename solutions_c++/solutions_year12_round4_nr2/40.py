#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std;

struct circle
{
	long long r;
	long long x, y;
	int index;
}C[1001];

bool byR(circle A, circle B)
{
	return A.r > B.r;
}

bool byIndex(circle A, circle B)
{
	return A.index < B.index;
}

int n, W, L, finish;

long long dist2(long long x1, long long y1, long long x2, long long y2)
{
	long long dx = x1 - x2;
	long long dy = y1 - y2;
	return dx * dx + dy * dy;
}

bool check(long long x, long long y, long long r)
{
	for(int i = 1; i <= finish; i++)
		if(dist2(x, y, C[i].x, C[i].y) < (r + C[i].r) * (r + C[i].r))
			return false;
	return true;
}

int MAIN()
{

	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		cin >> n >> W >> L;
		for(int i = 1; i <= n; i++)
			cin >> C[i].r, C[i].index = i;
		sort(C + 1, C + 1 + n, byR);
		int curX = 0;
		int curY = 0, dir = +1;
		C[1].x = 0, C[1].y = 0;
		for(int i = 2; i <= n; i++)
		{
			int d = C[i].r + C[i-1].r;
			finish = i-1;
			if(dir == 1)
			{
				if(curX + d > W)
				{
					curY += d;
					dir = -1;
				}
				else
					curX += d;
			}
			else
			{
				if(curX - d < 0)
				{
					curY += d;
					dir = 1;
				}
				else
					curX -= d;
			}
			if(curY > L)
			{
				cout << "WRONG!" << endl;
				continue;
			}
			int lef = curY - 1, rig = L, mid;
			if(check(curX, rig, C[i].r) == false)
			{
				cout << "WRONG!" << endl;
				continue;
			}
			while(rig - lef > 1)
			{
				mid = (rig + lef) / 2;
				if(check(curX, mid, C[i].r))
					rig = mid;
				else
					lef = mid;
			}
			curY = rig;
			C[i].x = curX;
			C[i].y = curY;
		}


		sort(C + 1, C + 1 + n, byIndex);
		for(int i = 1; i <= n; i++)
		{
			cout << C[i].x << " " << C[i].y;
			if(i == n)
				cout << endl;
			else
				cout << " ";
		}

	}
	return 0;
}

int main()
{
	#ifdef LOCAL_TEST
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//int START_TIME = clock();
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int RUN_RESULT = MAIN();
	/*#ifdef LOCAL_TEST
	cout << endl;
	cout << "[Time Used] " << clock() - START_TIME << " ms." << endl;
	#endif*/
	return RUN_RESULT;
}
