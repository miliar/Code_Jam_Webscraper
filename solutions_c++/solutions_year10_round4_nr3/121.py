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


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;

	for (int t = 1; t <= tests; t ++)
	{
		long long p;
		cin >> p;
		vector < vector <vector <bool> > >  arr(2, vector <vector<bool > > (5000, vector<bool> (5000,false)));

		int bacts = 0;
		for (int i=  0; i< p; i ++)
		{
			int x1,y1,x2,y2;
			cin >> x1>>y1>>x2>>y2;
			for (int x = x1; x <= x2; x ++)
				for (int y = y1; y <= y2; y ++)
					if (!arr[0][x][y])
					{
						bacts++;
						arr[0][x][y] = true;
					}
		}
		int r = 103;
		int res = 0;
		int now=0;
		while (bacts > 0)
		{
			for (int i=  1; i < r; i ++)
				for (int j = 1; j < r; j ++)
				{
					arr[1-now][i][j]= arr[now][i][j];
					if (arr[now][i][j])
					{
						if (!arr[now][i-1][j] && !arr[now][i][j-1])
						{
							arr[1-now][i][j] = false;
							bacts --;
						}
							
					}
					else
					{
						if (arr[now][i-1][j] && arr[now][i][j-1])
						{
							arr[1-now][i][j] = true;
							bacts ++;
						}
					}
				}
			r ++;
			res ++;
			now = 1-now;
		}

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
