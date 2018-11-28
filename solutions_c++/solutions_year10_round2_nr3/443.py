#include <iostream>
using std::cin;
using std::cout;
using std::endl;

const int mod = 100003;
int f[510][510];
int c[510][510];
int n;

int getc(int m, int n)
{
	if(n > m) return 0;
	if(n == 0) return 1;
	if(m == 0) return 1;
	else if(c[m][n] >= 0) return c[m][n];
	else c[m][n] = (getc(m-1, n-1) + getc(m-1, n)) % mod;
	return c[m][n];
}

void work()
{
	cin >> n;
	for(int i=2; i<=n; i++)
	{
		f[i][1] = 1;
		for(int j = 2; j<i; j++)
		{
			if(f[i][j] >= 0) continue;
			f[i][j] = 0;
			for(int k=1; k<j; k++)
				f[i][j] += getc(i-j-1, j-k-1) * f[j][k] % mod;
			//cout << "f[" << i << "][" << j << "]=" << f[i][j] << endl;
		}
	}
	int y = 0;
	for(int j = 1; j < n; j++)
	{
		y = (y + f[n][j]) % mod;
	}
	cout << y << endl;
}

int main()
{
	for(int i = 0; i < 510; i++) for(int j = 0; j<510; j++) f[i][j] = c[i][j] = -1;
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}
