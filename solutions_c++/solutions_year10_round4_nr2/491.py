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

using namespace std;

long long T;
int P;
int M[2000];
int pr[11][2000];
long long mon;
long long dp[11][1025][11];

bool ok()
{
	rep(i, 1 << P) if (M[i]!=0) return 0;
	return 1;
}

long long solve(int stage, int numb, int mins)
{
	if (dp[stage][numb][mins]!=-1) return dp[stage][numb][mins];
	long long re = 0;
	if (stage==0)
	{
		if (M[numb*(1<<(stage+1))]-mins<=0 && M[numb*(1<<(stage+1))+1]-mins<=0) return dp[stage][numb][mins]=0;
		else return dp[stage][numb][mins]=pr[0][numb];
	}
	bool fl = 0;
	rep(i, 1<<(stage+1))
	{
		if (M[numb*(1<<(stage+1)) + i]-mins==stage+1) { fl = 1; break; }
	}
	re = pr[stage][numb] + solve(stage-1, 2*numb, mins+1) + solve(stage-1, 2*numb+1, mins+1);
	if (!fl)
	{
		re = min(re, solve(stage-1, 2*numb, mins) + solve(stage-1, 2*numb+1, mins));
	}
	return dp[stage][numb][mins] = re;
}

int main()
{
    fstream fin("B-large.in",fstream::in);
    fstream fout("B-large.out",fstream::out);
    fin >> T;
	long long per = 0;
	string tmp;
    for(int j=1;j<=T;j++)
    {
		memset(dp, -1, sizeof(dp));
		fin >> P;
		rep(i, 1 << P) 
		{
			fin >> M[i];
			M[i] = P - M[i];
		}
		rep(i, P)
			rep(k, 1 << (P-i-1))
			{
				fin >> pr[i][k];
			}
		mon = solve(P-1, 0, 0);
		fout << "Case #" << j << ": " << mon << "\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}