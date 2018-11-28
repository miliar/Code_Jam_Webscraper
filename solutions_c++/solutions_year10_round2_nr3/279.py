#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int C[1000][1000] = {0};
const int M = 100003;
int F[505][505];

int Go(int n, int k)
{
	int& res = F[n][k];
	if (res != -1)
		return res;
	if (k == 1) return res = 1;
	res = 0;
	for (int npos = 1; npos < k; ++npos)
	{
		int cnt = C[n-k-1][k-npos-1];
		if (cnt > 0)
		{
			res = (res + cnt * (long long) Go(k, npos)) % M;
		}
	}
	return res;
}

int main()
{
	memset(F, -1, sizeof(F));
	ifstream ifs("c.in");
	ofstream ofs("c.out");		
	int t;
	ifs >> t;
	for (int i = 0; i < 1000; ++i)
	{
		C[i][0] = 1;
	}
	for (int i = 1; i < 1000; ++i)
	{
		for (int j= 1; j < 1000; ++j)
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % M;
	}
	for (int test = 0; test < t; ++test)
	{
		int n;
		ifs >> n;
		int sum = 0;
		for (int i = 1; i < n; ++i)
			sum = (sum + Go(n, i)) % M;
		ofs << "Case #" << test+1 << ": " << sum << endl;
	}
  	return 0;
}
