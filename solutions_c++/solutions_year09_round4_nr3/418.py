#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iterator>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <complex>
#include <bitset>
#include <valarray>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))
#define CPY(A,B) memcpy(A,B,sizeof(A))

//fix the file name here!
#define fname "C-small-attempt0"

ifstream in;
ofstream out;

int N, k;
int P[16][25];

int bitc(int n) { int r=0; while(n){r++;n&=(n-1);} return r;}

int cc[1<<16];
bool can(int mask)
{
	if(cc[mask] != -1) return cc[mask];
	FOR(i,0,k)
	{
		int ba = -1;
		FOR(j,0,N) if(mask&(1<<j))
		{
			if(P[j][i] <= ba) return cc[mask] = 0;
			ba = P[j][i];
		}
	}
	return cc[mask] = 1;
}

int dp[1<<16];
int mcount(int nmask)
{
	if(dp[nmask] != -1) return dp[nmask];
	int bmask = nmask;
	dp[bmask] = INT_MAX;
	while(nmask)
	{
		if(can(nmask)) dp[bmask] <?= mcount(bmask^nmask) + 1;
		nmask = (bmask&(nmask-1));
	}
	assert(dp[bmask] != INT_MAX);
	return dp[bmask];
}

int tmp[25];

void do_case(int case_no)
{
	in >> N >> k;
	FOR(i,0,N) FOR(j,0,k) in >> P[i][j];
	FOR(i,0,N)
	{
		int mi = i;
		FOR(j,i+1,N) if(P[j][0] < P[mi][0]) mi=j;
		CPY(tmp,P[i]);
		CPY(P[i],P[mi]);
		CPY(P[mi],tmp);
	}
	SET(cc,-1); cc[0] = 1;
	SET(dp,-1); dp[0] = 0;
	int res = mcount((1<<N)-1);
	cout << "Case #" << case_no << ": " << res << endl; // Change this in case the output requires it!
	out << "Case #" << case_no << ": " << res << endl; // Change this in case the output requires it!
}

int main()
{
	in.open(fname ".in");
	out.open(fname ".out");
	int T;
	in >> T; // Change this in case the input requires it!
	FOR(te,1,T+1) do_case(te);
	in.close();
	out.close();
	return 0;
}
