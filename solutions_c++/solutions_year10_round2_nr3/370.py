#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <string>

using namespace std;

ifstream in("small.in");
ofstream out("small.out");

int f[510][510];
int C[511][511];
int ft[510];

void work()
{
	for (int n = 0; n < 510; n++) 
	{
		C[n][0] = 1;
		C[n][n] = 1;
		for (int k = 1; k < n; k++)
			C[n][k] = (C[n-1][k-1] + C[n-1][k]) % 100003;
	}
}

int main()
{
	int test,i,n,j;

	work();

	f[1][1] = 1;

	f[2][1] = 1;

	ft[2] = 1;

	for (n = 3; n < 510; n++)
	{
		f[n][1] = 1;
		ft[n] = 1;
		for (i = 2;i < n; i++)
		{
			for (j = 1; j <= i - 1; j++)
				if (i - j - 1<= n - i - 1)
					f[n][i] = (f[n][i] + (f[i][j]*C[n - i - 1][i - j - 1]) % 100003) % 100003;
			ft[n] = (ft[n] + f[n][i]) % 100003;
		}
	}

	in >> test;
	for (int t = 1; t <= test; t++)
	{
		in >> n;
		out << "Case #" << t << ": " << ft[n] << endl;
	}
	return 0;
}