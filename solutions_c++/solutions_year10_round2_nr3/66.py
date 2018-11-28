#include <iostream>

using namespace std;

const int base = 100003;
int c[501][501];
long long f[501][501];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin >> T;
	c[0][0] = 1;
	for (int i = 1;i <= 500; i++)
	{
		c[i][0] = 1;
		for (int j = 1; j <= i; j++) c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % base;
	}
	for (int i = 2; i <= 500; i++)
		for (int j = 1; j < i; j++)
		{
			if (j == 1) f[i][j] = 1;
			else{
				for (int k = j - 1; k > 0; k--)
					if (i - j >= j - k) f[i][j] = (f[i][j] + f[j][k] * c[i - j - 1][j - k - 1]) % base;
			}
		}
	int n;
	for (int t = 0; t < T; t++)
	{
		int s = 0;
		cin >> n;
		for (int i = 1; i < n; i++) s = (s + f[n][i]) % base; 
		cout << "Case #" << t + 1 <<": "<<s <<"\n";
	}
}
