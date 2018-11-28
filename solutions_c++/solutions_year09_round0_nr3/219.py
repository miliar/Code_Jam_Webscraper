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

string w="welcome to code jam";
#define MOD 10000
int mem[5001][50],n;
char a[10001];

int f(int i1,int i2)
{
	if(i2 == w.size())
		return 1;
	if(i1>=n)
		return 0;
	int&r = mem[i1][i2];
	if(r!=-1)
		return r;
	r=0;
	if(a[i1]==w[i2])
		r= (f(i1+1,i2+1)%MOD)+r%MOD;
	r = (f(i1+1,i2)%MOD) + r%MOD;
	return r%MOD;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("c.in","rt",stdin);
	freopen("c.out","wt",stdout);
#endif
int t;
	scanf("%d ",&t);
	rep(tt,0,t)
	{
		gets(a);
		memset(mem,-1,sizeof(mem));
		n = strlen(a);
		int res = f(0,0);
		printf("Case #%d: %04d\n",tt+1,res%MOD);
	}

	return 0;
}