/*
TASK:
LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
template<class key>
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)

string str;
int mem[1000][300];
string msg="welcome to code jam";
int get(int i,int j)
{
	if(j==sz(msg))
		return 1;
	if(i==sz(str))
		return 0;
	int &r=mem[i][j];
	if(r!=-1)
		return r;
	r=get(i+1,j);
	if(str[i]==msg[j])
		r+=get(i+1,j+1);
	return r%=10000;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
	int T;
	getline(cin,str);
	sscanf(str.c_str(),"%d",&T);
	rep2(t,1,T)
	{
		getline(cin,str);
		memset(mem,-1,sizeof mem);
		printf("Case #%d: %04d\n",t,get(0,0));
	}
	return 0;
}
