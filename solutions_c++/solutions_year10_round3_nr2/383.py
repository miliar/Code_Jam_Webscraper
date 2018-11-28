/*
ID: mythic_1
PROG: b
LANG: C++
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <valarray>
#include <set>
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

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large (3).in","rt",stdin);
	freopen("b.out","wt",stdout);

#endif
	int t,n,a,b,c;
		cin >> t;
		for (int i = 0; i < t; ++i) {
			cin >> a >> b >> c;
			int cnt = 0;
			while ( b > a ){
				cnt++;
				b = (b+c-1)/c;
			}
			int res = (int)ceil(log2(cnt));
			printf("Case #%d: %d\n",i+1,res);

		}

		return 0;

	return 0;
}
