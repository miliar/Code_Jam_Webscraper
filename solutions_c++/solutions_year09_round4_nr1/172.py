#include <iostream>
#include <string>

using namespace std;

const int MAX_N = 44;

string a[MAX_N];
int b[MAX_N];
int n, res;

void init()
{
	for (int i = 0; i < n; ++i)
	{
		int j;
		for (j = n - 1; j >= 0; --j)
			if (a[i][j] == '1') break;
		b[i] = j + 1;
	}
}

void solve()
{
	init();
	res = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int j = i; j < n; ++j)
			if (b[j] <= i + 1)
			{
				res += (j - i);
				for (int k = j; k > i; --k)
					b[k] = b[k - 1];
				break;
			}
	}
	
}

int main()
{
	int T;
	cin >> T;
	for (int run = 1; run <= T; ++run)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
			
		solve();
		
		cout << "Case #" << run << ": " << res << endl;
	}
	
	return 0;
}
