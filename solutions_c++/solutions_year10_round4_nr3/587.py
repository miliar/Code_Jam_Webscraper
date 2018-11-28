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

int a[101][101];
int T;
int i, j, n, ok;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int count;
	cin >> T;
	int x1, x2, y1, y2;
	for(int eps=1;eps<=T;++eps)
	{
		memset(a, 0, sizeof(a));
		cin >> n;
		for(i=1;i<=n;++i)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			int Y = y1;
			for(;x1<=x2;++x1)
				for(y1=Y;y1<=y2;++y1)
					a[x1][y1] = 1;
		}

		ok = 1;
		for(count=0;ok;++count)
		{
			ok = 0;
			for(i=100;i>=1;--i)
				for(j=100;j>=1;--j)
					if(a[i][j])
					{
						ok = 1;
						if(!a[i-1][j] && !a[i][j-1])
							a[i][j] = 0;
					}
					else
						if(a[i-1][j] && a[i][j-1])
							a[i][j] = 1;
		}

		cout << "Case #" << eps << ": " << count - 1 << endl;
	}
	return 0;
}
