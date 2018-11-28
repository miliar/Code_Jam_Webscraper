#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int L, H, N;
vector<int> a;

void solve1(int test)
{
	int ans = -1;
	for (int i = L; i <= H; ++i)
	{
		bool h = true;
		for (int j = 0; j < N; ++j)
		{
			if ((a[j] > i && a[j] % i != 0))
			{
				h = false;
				break;
			}
			if (a[j] < i && i % a[j] != 0)
			{
				h = false;
				break;
			}
		}
		if (h)
		{
			ans = i;
			break;
		}
	}
	
	if (ans == -1)
		cout << "Case #" << test + 1 << ": NO" << endl;
	else
		cout << "Case #" << test + 1 << ": " << ans << endl;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int T;
	cin >> T;

	for (int col = 0; col < T; ++col)
	{
		a.clear();
		cin >> N >> L >> H;
		a.resize(N);
		for (int i = 0; i < N; ++i)
			cin >> a[i];
		solve1(col);
	}
	return 0;
}

