#include <iostream>
using namespace std;

const int maxn = 500;

int f[maxn+1][maxn+1];
int c[maxn+1][maxn+1];

int main()
{
	int tt;
	cin >> tt;
	for (int i=0; i<=maxn; i++)
		for (int j=0; j<=maxn; j++)
		{
			f[i][j] = 0;
			c[i][j] = 0;
		}
	c[0][0] = 1;
	for (int i=1; i<=maxn; i++)
	{
		c[i][0] = 1;
		c[i][i] = 1;
		for (int j=1; j<i; j++)
		{
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 100003;
		}
	}

	f[0][1] = 1;
	for (int i=0; i<=maxn; i++)
	{
		for (int j=2+i; j<=maxn; j++)
		{
			for (int k=0; k<=i; k++)
			{
				f[i][j] = (f[i][j] + f[k][j-i-1] * c[i][i-k]) % 100003;
			}
//			cout << i << '/' << j << ':' << f[i][j] << endl;
		}
	}

	for (int tc=1; tc<=tt; tc++)
	{
		int n;
		cin >> n;
		int x = 0;
		for (int i=0; i<=n-2; i++)
		{
			x = (x + f[i][n] ) % 100003;
		}

		cout << "Case #" << tc << ": " << x << endl;
	}
}


