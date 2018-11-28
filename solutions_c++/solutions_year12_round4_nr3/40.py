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

int n;

struct interval
{
	int L, R;
}I[2001];

vector <int> e[2001];
int ans[2001];

void solve(int w, int H, int dec)
{
	//cout << I[w].L << " ~ " << I[w].R << ": " << H << " " << dec << endl;
	int x = I[w].R;

	for(int i = 0; i < (int)e[w].size(); i++)
	{
		int t = e[w][i];
		int d1 = dec * (x - I[t].L);
		ans[I[t].L] = H - d1;
		int d2 = dec * (x - I[t].R);
		ans[I[t].R] = H - d2;
		//cout << w << " " << I[w].L << ", " << I[w].R << "  =>  " << t << " " << I[t].L << ", " << I[t].R << endl;
		solve(t, H - d2, dec + 1);
	}
}

void check()
{
	for(int i = 1; i < n; i++)
	{
		double k = -10000;
		int which = 0;
		for(int j = i+1; j <= n; j++)
		{
			double t = double(ans[j] - ans[i]) / double(j - i);
			if(t > k)
			{
				k = t;
				which = j;
			}
		}
		cout << which << " ";
	}
	cout << endl;
}

int MAIN()
{

	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		cin >> n;
		for(int i = 1; i < n; i++)
		{
			cin >> I[i].R;
			I[i].L = i;
		}
		bool impossible = false;
		for(int i = 1; i < n; i++)
			for(int j = i+1; j < n; j++)
				if(I[i].R > I[j].L && I[j].R > I[i].R)
				{
					impossible = true;
					//cout << i << ", " << j << endl;
				}
		I[0].L = 0, I[0].R = n;
		if(impossible)
		{
			//cout << n << endl; /* !!!! */
			cout << "Impossible" << endl;
		}
		else
		{
			for(int i = 0; i < n; i++)
				e[i].clear();
			for(int i = 1; i < n; i++)
			{
				int minLength = 10000000, which = 0;
				for(int j = 0; j < n; j++)
					if(i != j)
						if(I[j].L <= I[i].L && I[i].R <= I[j].R)
						{
							int len = I[j].R - I[j].L;
							if(len < minLength)
							{
								minLength = len;
								which = j;
							}
						}
				e[which].push_back(i);
				//cout << I[which].L << ", " << I[which].R << " -> " << I[i].L << ", " << I[i].R << endl;
			}
			solve(0, 100000000, 0);
			for(int i = 1; i <= n; i++)
			{
				cout << ans[i];
				if(i == n)
					cout << endl;
				else
					cout << " "; 
			}
			//cout << n << endl; /* !!!! */
			//check();
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
