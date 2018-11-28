#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;

vector<LL> rotate_num(LL n)
{
	set<LL> ret;
	LL t = n;
	LL x = n;
	int ndigits = 0;
	LL tenpow = 1;
	while(t)
	{
		tenpow*=10;
		ndigits++;
		t/=10;
	}
	tenpow/=10;
	int i;
	//cout<<"Num : "<<n<<endl;
	for(i = 0; i < ndigits; i++)
	{
		LL right = x%10;
		x /= 10;
		x += right * tenpow;
		ret.insert(x);
		//cout<<x<<endl;
	}
	vector<LL> vret(ret.begin(), ret.end());
	return vret;
}
LL solve(LL a, LL b)
{
	LL i, j, k;
	LL ret = 0;
	for(i = a; i <= b; i++)
	{
		vector<LL> rot = rotate_num(i);
		for(j = 0; j < SZ(rot); j++)
		{
			if(rot[j] > i && rot[j] <= b)
				ret++;
		}
	}
	return ret;
}
int main()
{
	int tes;
	GI(tes);
	int c = 0;
	while(tes--)
	{
		c++;
		int a, b;
		GI(a);
		GI(b);
		LL ans = solve(a, b);
		printf("Case #%d: %lld\n", c, ans);
	}
	return 0;
}
		


