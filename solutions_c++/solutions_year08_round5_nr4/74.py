//some code in here may be from Abdenego's library
//at http://shygypsy.com/tools/
//(you will see a comment near the relevant code if that's
//the case!)
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define V(type) vector< type >
#define Vall(t) t.begin(),t.end()
#define llint long long
#define forV(var, vec) for(int var=0;var<vec.size();var++)
#define for0(var, lim) for(int var=0;var<lim;var++)
#define for1(var,lim) for(int var=1;var<lim;var++)
#define btw(x,a,b) ((x) >= (a) && (x) <= (b))
#define permute(vec) next_permutation( vec.begin(),vec.end())
#define MP make_pair
#define dpExp MP(a,b)

using namespace std;

int memo[400][400];
int bad[400][400];

int dr[] = {1,2};
const int MOD = 10007;
int dc[] = {2,1};
int H,W;
int dp(int r,int c)
{
	if(r == H && c == W){return 1;}
	int &ret = memo[r][c];
	if(ret != -1)
	{
		return ret;
	}
	ret = 0;
	for(int t=0;t<2;++t)
	{
		int NR = r + dr[t];
		int NC = c + dc[t];
		if(NR <= H && NC <= W && !bad[NR][NC])
		{ret += dp(NR,NC);ret %= MOD;}
	}
	return ret;
}

int main(void)
{
	int CASES;
	cin >> CASES;
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		memset(memo,-1,sizeof(memo));
		cin >> ::H >> ::W;
		int R;
		cin >> R;
		memset(bad,0,sizeof(bad));
		for(int i=0;i<R;++i)
		{
			int x,y;
			cin >> x >> y;
			bad[x][y] = 1;
		}
		int out = dp(1,1);

		cout << "Case #" << _cn << ": " << out << endl;
		cerr << "Case #" << _cn << ": " << out << endl;
	}
	return 0;
}

