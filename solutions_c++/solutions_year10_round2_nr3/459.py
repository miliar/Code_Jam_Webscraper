#include <iostream>
#include <cstring>

using namespace std;

const int MAX_N = 504;
const int base = 100003;

int f[MAX_N][MAX_N];
int c[MAX_N][MAX_N];

int main()
{
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for (int i = 1; i <= 500; ++i)
		for (int j = i; j <= 500; ++j)
			c[i][j] = (c[i][j-1] + c[i-1][j-1]) % base;
	
	memset(f, 0, sizeof(f));
	f[1][0] = 1;
	for (int i = 2; i <= 500; ++i)
		for (int j = 1; j <= i-1; ++j)
			for (int k = 0; k <= j-1; ++k)
				if (i - j >= j - k)
					f[i][j] = (f[i][j] + f[j][k] * c[j-k][i-j]) % base;
	
	int nTests;
	cin >> nTests;
	for (int run = 1; run <= nTests; ++run)
	{
		
		int n;
		cin >> n;
		int res = 0;
		for (int i = 1; i <= n-1; ++i)
		{
			res = (res + f[n][i]) % base;
		}
		cout << "Case #" << run << ": " << res << endl;
	}
	return 0;
}
