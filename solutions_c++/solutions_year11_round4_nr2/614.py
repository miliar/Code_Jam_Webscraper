#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int R, C, D;
int data[510][510];
char in[510][510];

bool check (int x, int y, int size)
{
	if (x+size-1 >= R || y+size-1 >= C)
		return false;

	int ex = x + size-1;
	int ey = y + size-1;

	double cx = (double)(x + ex) / 2;
	double cy = (double)(y + ey) / 2;

	double sumx = 0, sumy = 0;

	for (int i=x ;i<=ex ;i++)
	{
		for (int j=y ;j<=ey ;j++)
		{
			if (i==x && j==y)
				continue;
			if (i==x && j==ey)
				continue;
			if (i==ex && j==y)
				continue;
			if (i==ex && j==ey)
				continue;
			sumx += ((double)i - cx) * (D + data[i][j]);
			sumy += ((double)j - cy) * (D + data[i][j]);
		}
	}


	return fabs(sumx) <1e-15 && fabs(sumy) < 1e-15;
}

void solve_case ()
{
	cin >> R >> C >> D;
	for (int i=0 ;i<R ;i++)
	{
		cin >> in[i];
		for (int j=0 ;j<C ;j++)
			data[i][j] = in[i][j] - '0';
	}

	int ans = -1;

	for (int k=min(R, C) ;k>=3 ;k--)
	{
		for (int i=0 ;i<R ;i++)
		{
			for (int j=0 ;j<C ;j++)
			{
				if (check (i, j, k))
				{
					ans = k;
					break;
				}
			}

			if (ans>0)
				break;
		}

		if (ans>0)
			break;
	}

	if (ans>0)
		cout << ans;
	else
		cout << "IMPOSSIBLE";
	cout << endl;
}

int main ()
{
	int total_cases;

	cin >> total_cases;
	for (int cases=1 ;cases<=total_cases ;cases++)
	{
		cout << "Case #" << cases << ": ";
		solve_case ();
	}

	return 0;
}
