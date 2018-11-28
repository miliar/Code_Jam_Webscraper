#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <stack>
#include <sstream>
#include <cmath>
#include <deque>
#include <bitset>
#include <string>
using namespace std;

const int mod = 100003;
const int MAX = 501;
int a[MAX][MAX];
const int n = 500;

int c[MAX][MAX], know[MAX][MAX];
int sol[MAX];

int C(int n, int k)
{
	if(k > n || k < 0 || n < 0)
		return 0;

	if(know[n][k])
		return c[n][k];
	
	know[n][k] = 1;
	return (c[n][k] = (C(n-1, k-1) + C(n-1, k)) % mod);
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	c[0][0] = 1; know[0][0] = 1;
	int i, j, k;
	for(i=2;i<=n;++i)
	{
		a[i][1] = 1;
		for(j=2;j<i;++j)
			for(k=1;k<j;++k)
			{
				a[i][j] = (a[i][j] + (a[j][k] * C(i-j-1, j-k-1)) % mod) % mod;
			}
	}

	for(i=1;i<=n;++i)
	{
		sol[i] = 0;
		for(j=1;j<=n;++j)
			sol[i] = (sol[i] + a[i][j]) % mod;
	}


	int t, x;
	cin >> t;
	for(int TI = 1; TI <= t; ++ TI)
	{
		cin >> x;
		cout << "Case #" << TI << ": " << sol[x] << endl;
	}
	return 0;
}
