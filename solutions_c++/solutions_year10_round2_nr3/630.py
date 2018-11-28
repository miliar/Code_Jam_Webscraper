#include <fstream>
using namespace std;

ifstream cin("C-small-attempt1.in");
ofstream cout("C-small-attempt1.out");

long long fC(long long a, long long b)
{
	long long x = 1;
	int i;
	for (i = 0; i < b; i++)
		x = ( x * (a - i) / (i + 1) ) % 100003;
	return x;
}
int t, i, n, j, k, y;
long long a[510][510] = {0};
long long f[510];
long long C[510][510];

int main()
{
	cin >> t;
	a[2][1] = 1;
	for (i = 0; i <= 500; i++)
		for (j = 0; j <= 500; j++)
			C[i][j] = fC(i, j);
	f[2] = 1;
	for (i = 3; i <= 500; i++)
	{	
		f[i] = a[i][1] = 1;
		for (j = 2; j < i; j++)
		{
			for (y = 1; y < j; y++)
	
				a[i][j] += (a[j][y] * C[i - j - 1][j - y - 1]) % 100003;
			f[i] = (f[i] + a[i][j]) % 100003;
		}
	}
	
	for (k = 1; k <= t; k++)
	{
		cin >> n;
		cout << "Case #" << k << ": " << f[n] << endl;
	}
	return 0;
}