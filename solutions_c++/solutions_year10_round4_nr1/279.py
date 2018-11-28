#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
using namespace std;

int a[400][400];
int n, i, j, k, x, y;
int best;

bool simetric(int x, int y)
{
	int i, j;
	for(i=0;i<=2*n+10;++i)
		for(j=0;j<=2*n+10;++j)
			if(!((a[x-i][y-j]==-1 || a[x+i][y-j]==-1 || a[x-i][y-j] == a[x+i][y-j]) &&
				   (a[x-i][y-j]==-1 || a[x-i][y+j]==-1 || a[x-i][y-j] == a[x-i][y+j]) &&
				   (a[x-i][y+j]==-1 || a[x+i][y+j]==-1 || a[x-i][y+j] == a[x+i][y+j]) &&
				   (a[x+i][y-j]==-1 || a[x+i][y+j]==-1 || a[x+i][y-j] == a[x+i][y+j])))
					return false;
	return true;
}

int size(int i, int j)
{
	return n + abs(200 - i) + abs(200 - j);
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for(int ti = 1; ti <= t; ++ ti)
	{
		memset(a, -1, sizeof(a));
		cin >> n;
		x = 200 - n + 1;
		y = 200;
		best = 500;
		for(i=0;i<n;++i)
			for(j=y-i;j<=y+i;j += 2)
				cin >> a[x+i][j];
		for(i=n-2, k = 201;i>=0;--i, ++ k)
			for(j=y-i;j<=y+i;j += 2)
				cin >> a[k][j];
		
		for(i=200-n;i<=200+n;++i)
		{
			for(j=200-n;j<=200+n;++j)
				if(simetric(i, j))
					if(size(i, j) < best)
						best = size(i,j);
		}

		cout << "Case #" << ti << ": " << best*best - n*n << endl;
	}
	return 0;
}
