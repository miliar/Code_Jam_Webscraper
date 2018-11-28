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
#define MP(a,b) make_pair((a),(b))
#define dpExp MP(a,b)

using namespace std;

int memo[20000][3];


vector<pair<int,int> > vq;
int Z;
int dp(int at,int valwant)
{
	if(at > (Z-1)/2){return ((at < vq.size() && vq[at].first == valwant))?(0):(1000000);}
	int &ret = memo[at][valwant];
	if(ret != -1){return ret;}
	ret = 10000000;
	bool chg = vq[at].second;
	bool isand = vq[at].first;
	if(isand)
	{
		if(valwant)
		{
			ret <?= dp(2*at,1) + dp(2*at+1,1);
		}
		else
		{
			ret <?= dp(2*at,0) + dp(2*at+1,1);
			ret <?= dp(2*at,0) + dp(2*at+1,0);
			ret <?= dp(2*at,1) + dp(2*at+1,0);
		}
		if(chg)
		{
		if(!valwant)
		{
			ret <?=1 + dp(2*at,0) + dp(2*at+1,0);
		}
		else
		{
			ret <?=1 +  dp(2*at,0) + dp(2*at+1,1);
			ret <?=1 + dp(2*at,1) + dp(2*at+1,1);
			ret <?=1+ dp(2*at,1) + dp(2*at+1,0);
		}

		}
	}
	else
	{
		if(chg)
		{
		if(valwant)
		{
			ret <?= 1 + dp(2*at,1) + dp(2*at+1,1);
		}
		else
		{
			ret <?=1 + dp(2*at,0) + dp(2*at+1,1);
			ret <?= 1+  dp(2*at,0) + dp(2*at+1,0);
			ret <?=1 + dp(2*at,1) + dp(2*at+1,0);
		}
		}
		if(!valwant)
		{
			ret <?=dp(2*at,0) + dp(2*at+1,0);
		}
		else
		{
			ret <?=dp(2*at,0) + dp(2*at+1,1);
			ret <?=dp(2*at,1) + dp(2*at+1,1);
			ret <?=dp(2*at,1) + dp(2*at+1,0);
		}

	}
	return ret;
}



int main(void)
{
	int CASES;
	cin >> CASES;
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		int M,V;
		cin >> M >> V;
		vector<pair<int,int> > v;v.clear();
		v.push_back(make_pair(0,0));
		int q,qq;
		for(int i=0;i<(M-1)/2;++i)
		{
			cin >> q >> qq;
			v.push_back(make_pair(q,qq));			
		}
		for(int i=0;i<(M+1)/2;++i)
		{
			cin >> q;
			v.push_back(make_pair(q,-1));
		}
		memset(memo,-1,sizeof(memo));
		Z = M;
		vq = v;
		int x = dp(1,V);
		if(x > 100000)
		{
		cout << "Case #" << _cn << ": IMPOSSIBLE" <<endl;
		cerr << "Case #" << _cn << ": IMPOSSIBLE" <<endl;

		}
		else
		{
		cout << "Case #" << _cn << ": " << x << endl;
		cerr << "Case #" << _cn << ": " << x << endl;
		}
	}
	return 0;
}

