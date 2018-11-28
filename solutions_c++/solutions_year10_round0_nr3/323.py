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
#include <valarray>
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
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
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
int g[100000];
int arr[1001];
long long total[1001];
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in","rt",stdin);
	freopen("1.out","wt",stdout);
#endif
	int T;
	cin>>T;
	rep(t,T)
	{
		int n,k,r;
		cin>>r>>k>>n;
		rep(i,n)
			cin>>g[i];
		memset(arr,-1,sizeof arr);
		arr[0]=0;
		int c=1,f=0;
		long long tot=0;
		while(1)
		{
			long long s=0;
			int xxx=n;
			while(s+g[f]<=k && xxx--)
			{
				s+=g[f];
				f=++f%n;
			}
			tot+=s;
			total[c]=tot;
			if(arr[f]!=-1)
				break;
			arr[f]=c++;
		}
		long long res;
		if(r<c)
			res=total[r];
		else
		{
			res=total[arr[f]];
			r-=arr[f];
			long long x=tot-total[arr[f]];
			res+=x*(r/(c-arr[f]));
			int z=(r%(c-arr[f]));
			res+=total[arr[f]+z]-total[arr[f]];;
		}
		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}
	return 0;
}
