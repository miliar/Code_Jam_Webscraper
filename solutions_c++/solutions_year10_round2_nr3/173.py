#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)
#define MOD 100003

using namespace std;

long long T;
long long n;
long long dp[505][505];
long long re;
long long bin[505][505];

long long f(int nn, int rank)
{
	if (dp[nn][rank]!=-1) return dp[nn][rank];
	long long ret = 0, mn;
	for(int i=1;i<rank;i++)
	{
		if (rank - i <= nn - rank) 
		{
			if (nn - rank - rank + i > 0) mn = bin[nn - rank - 1][rank - i - 1];
			else mn = 1;
			ret += mn*f(rank, i);
		}
		ret %= MOD;
	}
	return dp[nn][rank] = ret;
}

int main()
{
    fstream fin("C-large.in",fstream::in);
    fstream fout("C-large.out",fstream::out);
    fin >> T;
	long long per = 0;
	string tmp;
	bin[1][0] = bin[1][1] = 1;
	for(int i=2;i<504;i++)
	{
		bin[i][0] = 1;
		for(int j=1;j<i;j++)
		{
			bin[i][j] = bin[i-1][j] + bin[i-1][j-1];
			bin[i][j] %= MOD;
		}
		bin[i][i] = 1;
	}
	rep(i,504) rep(j,504) dp[i][j] = -1;
	for(int i=2;i<=504;++i)
		dp[i][1] = 1;
    for(int j=1;j<=T;j++)
    {
		fin >> n;
		re = 0;
		for(int i=1;i<n;i++)
		{
			re += f(n, i);
			re %= MOD;
		}
		fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
