#include <iostream>
#include <vector>
#include <string>
using namespace std;
const int NMAX = 250;
//int tmp[NMAX][NMAX];
//int a[NMAX][NMAX];
vector<vector<int> > a, tmp;
bool Step()
{
	bool fl = false;
	for (int i = 1; i < NMAX; ++i)
		for (int j = 1; j < NMAX; ++j)
		{
			if (a[i - 1][j] && a[i][j - 1])
				tmp[i][j] = 1;
			else if (!a[i - 1][j] && !a[i][j - 1])
				tmp[i][j] = 0;
			else
				tmp[i][j] = a[i][j];
			if (tmp[i][j] == 1)
				fl = true;
		}
	a.swap(tmp);//memcpy(a, tmp, sizeof(int) * NMAX * NMAX);		
	return fl;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int tcc = 0; tcc < tc; ++tcc)
	{
		int r;
		cin >> r;
		a = vector<vector<int> > ();
		a.resize(NMAX);
		for (int i = 0; i < NMAX; ++i)
			a[i].resize(NMAX);
		tmp = a;
		//memset(a, sizeof(a), 0);
		int x1, y1, x2, y2;
		for (int t = 0; t < r; ++t)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			//--x1; --y1; --x2; -- y2;
			for (int i = x1; i <= x2; ++i)			
				for (int j = y1; j <= y2; ++j)
					a[i][j] = 1;
		}
		int ans = 0;
		while (Step())
		{
			++ans;
		}
		cout << "Case #" << (tcc + 1) << ": " << ans + 1 << endl;
	}
	return 0;
}