#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <complex>
#include <queue>
#include <complex>
#include <ctime>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (int)(n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int l,d,n,len;
char a[100002];
vector<string> wss;

int solve()
{
	int res=0;
	rep(i,0,d)
	{
		for(int i1 = 0,i2 = 0;i2<len&&i1<wss[i].size();++i1,++i2)
		{
			if(a[i2]=='(')
			{
				bool fl=0;
				while(a[i2]!=')')
				{
					if(a[i2]==wss[i][i1])
						fl=1;
					i2++;
				}
				if(!fl)
					goto bara;
			}
			else
				if(a[i2]!=wss[i][i1])
					goto bara;
		}
		res++;
		bara:;
	}
	return res;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	#endif

	scanf("%d %d %d ",&l,&d,&n);
	rep(i,0,d)
		scanf("%s",a),wss.PB(a);
	rep(i,0,n)
	{
		scanf("%s",a);
		len = strlen(a);
		int res = solve();
		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}
