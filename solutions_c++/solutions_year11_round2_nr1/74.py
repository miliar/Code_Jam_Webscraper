#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <set>
#include <iostream>
#include <queue>
using namespace std;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t  <= tc; t ++)
	{
		int n;
		cin >> n;
		vector <string> a(n);
		for (int i = 0; i < n; i ++)
			cin >> a[i];
		vector <pair<int,int> > wp(n);
		vector <double > owp(n,0);
		vector <double > oowp(n,0);
		for (int i =  0; i < n; i ++)
		{
			int w = 0;
			int g = 0;
			for (int j = 0; j < n; j ++)
			{
				if (a[i][j] != '.')
					g ++;
				if (a[i][j] == '1')
					w ++;
			}
			wp[i] = make_pair(w,g);
		}
		for (int i =  0; i < n; i ++)
		{
			double w = 0;
			int g = 0;
			for (int j = 0; j < n; j ++)
			{
				if (a[i][j] != '.')
				{
					g ++;
					int one = 0;
					if (a[i][j] == '0')
						one = 1;
					w += (double)(wp[j].first - one)/(wp[j].second-1);
				}
			}
			owp[i] = (double)w/g;
		}

		for (int i =  0; i < n; i ++)
		{
			double w = 0;
			int g = 0;
			for (int j = 0; j < n; j ++)
			{
				if (a[i][j] != '.')
				{
					g ++;
					w += owp[j];
				}
			}
			oowp[i] = (double)w/g;
		}
		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < n; i ++)
			printf("%.9lf\n", 0.25*(double)wp[i].first/wp[i].second + 0.5*owp[i] + 0.25 * oowp[i]);

	}

	return 0;
}
