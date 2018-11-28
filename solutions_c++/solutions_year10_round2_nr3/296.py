#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("c-large.in");
ofstream fout("c-large.out");

const int MOD = 100003;

int f[600][600];
int s[600];
int c[600][600];

int main()
{
	memset(c, 0, sizeof c);
	memset(f, 0, sizeof f);
	memset(s, 0, sizeof s);

	c[0][0] = 1;
	for (int i=1; i<550; i++)
	{
		c[i][0] = c[i][i] = 1;
		for (int j=1; j<i; j++)
			c[i][j] = (c[i-1][j-1] + c[i-1][j])%MOD;
	}

	f[2][1] = 1;
	for (int i=3; i<550; i++)
	{
		f[i][1] = 1;
		for (int j=2; j<i; j++)
			for (int k=1; k<j; k++)
				f[i][j] = (f[i][j] + ((long long)f[j][k] * (long long)c[i-j-1][j-k-1])% MOD)%MOD;
	}
	for (int i=2; i<550; i++)
	{
		for (int j=1; j<i; j++)
			s[i] = (s[i] + f[i][j])%MOD;
	}

	int T;
	fin >> T;
	int cases = 0;
	while (T--)
	{
		int n;
		fin >> n;
		fout << "Case #" << ++cases << ": " << s[n] << endl;
	}
	return 0;
}