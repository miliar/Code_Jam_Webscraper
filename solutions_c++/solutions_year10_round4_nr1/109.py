#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

bool Simmetric(vector <vector <int> > &arr, int x, int y, int side)
{
	for (int i=  0; i < side; i ++)
		for (int j = 0; j < side; j ++)
		{
			int sx = i + (x-i)*2;
			if (sx >= side || sx < 0)
				continue;

			if (arr[sx][j] == -1 || arr[i][j] == -1)
				continue;

			if (arr[sx][j] != arr[i][j])
				return false;
		}
	for (int i=  0; i < side; i ++)
		for (int j = 0; j < side; j ++)
		{
			int sy = j + (y-j)*2;
			if (sy >= side || sy < 0)
				continue;

			if (arr[i][j] == -1 || arr[i][sy] == -1)
				continue;

			if (arr[i][j] != arr[i][sy])
				return false;
		}
	return true;
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;

	for (int t = 1; t <= tests; t ++)
	{
		int k;
		cin >> k;
		int side = 2*k-1;
		vector <vector <int> > arr(side, vector <int>(side,-1));
		for (int i = 0; i < k; i ++)
		{
			for (int j = 0; j <= i; j ++)
			{
				int x;
				cin >> x;
				arr[i][k-i-1+2*j] = x;
			}
		}
		for (int i = 0; i < k-1; i ++)
		{
			for (int j = 0; j < k-i-1; j ++)
			{
				int x;
				cin >> x;
				arr[i+k][i+1+2*j] = x;
			}
		}
		int ans = 1000000;
		for (int x = 0; x < side; x ++ )
			for (int y = 0; y < side; y ++)
			{
				if (Simmetric(arr,x,y,side))
				{
					int dx = abs(x-side/2);
					int dy = abs(y-side/2);
					ans = min (ans,dx+dy+k); 
				}
			}
		int res = ans*ans-k*k;

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
