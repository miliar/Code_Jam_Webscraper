#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

long long dp[1001];
long long n,m,X,Y,Z;
long long seq[1001];
long long A[1001];
int solve()
{

	int i,j;
	for (i = 0 ; i < n ; i++)
		dp[i] = 1;
	for (i = 1 ; i < n ; i++)
	{
		for (j = i - 1 ;j >= 0 ; j--)
		{
			if (seq[i] > seq[j])
			{
				dp[i] += dp[j];
				dp[i] %= 1000000007;
			}
		}
	}
	int res = 0;
	for (i = 0 ; i < n ; i++)
	{
		res += dp[i];
		res %= 1000000007;
	}
	return res;
}

int main()
{

	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("out.txt","w",stdout);
	int ncase,m1,i;
	cin >> ncase;
	m1 = 0;
	while (ncase--)
	{
		m1++;
		cin >> n >> m >> X >> Y >> Z;
		for (i = 0 ; i < m ; i++)
			cin >> A[i];
		for (i = 0 ; i < n ; i++)
		{
			seq[i] = A[i % m];
			A[i % m] = (X * A[i% m] + Y* (i+1)) % Z;
		}
		int res = solve();
		cout << "Case #" << m1 << ": ";
		cout << res << endl;
		//printf("Case #%d: ",m);
	}
}
