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
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;
#ifndef M_PI
const long double M_PI = acos((long double) -1);
#endif
#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO = 0;
const long double INF = 1 / ZERO, EPSILON = 1e-12;
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
vector<long long> v;
long double d;
bool ok(long double time)
{
	long double mn=-1e18,mx=1e18;
	int s=0,e=sz(v)-1;
	while(s<e)
	{
		//mn=max(mn,v[s]-time);
		if(v[s]>mn)
		{
			mn=max(mn,v[s]-time);
		}
		else
		{
			if(mn-v[s]>time)
				return false;
		}
		mn+=d;
		if(v[e]<mx)
			mx=min(v[e]+time,mx);
		else
		{
			if(v[e]-mx>time)
				return false;
		}
		mx-=d;
		s++;
		e--;
	}
	if(e<s)
	{
		return mx>mn-d;
	}
	else
	{
		if(mn>mx)
			return false;
		if(v[s]<mn)
			return mn-v[s]<time;
		else if(v[s]>mx)
			return v[s]-mx<time;
		return true;
	}
}
int main() {
	std::ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int T;
	cin >> T;
	rep(t,T) {
		v.clear();
		int n;
		cin>>n>>d;
		while(n--)
		{
			int x,y;
			cin>>x>>y;
			while(y--)
				v.push_back(x);
		}
		sort(all(v));
		long double s=0,e=1e13;
		while(fabs(s-e)>1e-11)
		{
			long double m=(s+e)/2;
			if(ok(m))
				e=m;
			else
				s=m;
		}
		printf("Case #%d: %.9lf\n", t + 1,(double)((s+e)/2));
	}
	return 0;
}
