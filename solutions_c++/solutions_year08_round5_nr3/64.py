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

int memo[15][(1 << 15)];
int bad[15][15];

int dr[] = {1,2};
const int MOD = 10007;
int dc[] = {2,1};
int H,W;
inline bool isset(int a,int b)
{
	return (a & (1 << b)) != 0;
}
int bc[(1 << 15)];

int dp(int at,int mask)
{
	if(at == H){return 0;}
	int &ret = memo[at][mask];
	if(ret != -1)
	{
		return ret;
	}
	ret = 0;
	for(int i=0;i<(1 << W);++i)
	{
		int q = bc[i];
		int newmask = (1 << W) - 1;
		//check valid
		bool b = true;
		for(int j=1;j+1<W;++j)
		{
			if(isset(i,j))
			{
				newmask &= ~(1 << (j-1));
				newmask &= ~(1 << (j+1));
				if(!isset(mask,j) || (isset(i,j+1) || isset(i,j-1))){b = false;break;}

			}
		}
		if(!b){continue;}
		if(isset(i,0))
		{
			newmask &= ~(1 << 1);
			if(!isset(mask,0)){continue;}
			if(W > 1 && isset(i,1)){continue;}
		}
		if(isset(i,W-1))
		{
			if(W > 1){newmask &= ~(1 << (W-2));}
			if(!isset(mask,W-1)){continue;}
			if(W > 1 && isset(i,W-2)){continue;}
		}
		if(at + 1 != H)
		{
		for(int j=0;j<W;++j)
		{
			if(bad[at+1][j]){newmask &= ~(1 << j);}

		}
		}
		ret >?= q + dp(at+1,newmask);
	}
	return ret;
}

int main(void)
{
	int CASES;
	cin >> CASES;
	bc[0] = 0;
	for(int i=1;i<(1 << 15);++i)
	{
		bc[i] = 1 + bc[i&(i-1)];
	}
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		memset(memo,-1,sizeof(memo));
		memset(bad,0,sizeof(bad));
		cin >> ::H >> ::W;
		vector<string> v;v.clear();
		string s;
		for(int i=0;i<H;++i)
		{
			cin >> s;v.push_back(s);
		}
		reverse(Vall(v));
		forV(i,v)
		{
			forV(j,v[i])
			{
				if(v[i][j] == 'x'){bad[i][j] = 1;}
			}
		}
		int st = 0;
		forV(j,v[0])
		{
			if(v[0][j] != 'x'){st |= (1 << j);}
		}
		int out = dp(0,st);
		cout << "Case #" << _cn << ": " << out << endl;
		cerr << "Case #" << _cn << ": " << out << endl;
	}
	return 0;
}

