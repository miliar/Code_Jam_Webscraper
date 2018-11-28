/*
ID: mythic_1
PROG: C
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
#define SMALL
//#define LARGE

int main()
{
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
	int t,N,H,L;
	cin>>t;
	for(int tt = 1 ; tt<= t; tt++)
	{
		vector<ll> v;
		cin>>N>>L>>H;
		v.clear();
		v.resize(N);
		for(int k = 0 ; k < N ; k++)
			cin>>v[k];
		bool f = true;
		cout<<"Case #"<<tt<<": ";
		for(int i = L ; i <= H ; i++)
		{
			f = true;
			for(int j = 0 ; j < N ; j++)
			{
				if((i>v[j])&&(i%v[j]))
				{
					f = false;
					break;
				}
				if((i<v[j])&&(v[j]%i))
				{
					f = false;
					break;
				}
			}
			if(f){
				cout<<i<<endl;
				break;
			}
		}
		if(!f)
			cout<<"NO\n";
	}

	return 0;
}
