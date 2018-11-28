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
#define SMALL
//#define LARGE

int a[1<<12];
int calc(int st,int en)
{

	//if(st==en)return a[st]>0;
	bool f= 0;
	for(int i = st ; i < en ; i++)
	{
		if(a[i]>0)
		{
			f = 1;
			break;
		}
	}
	if(f)
	{
		for(int i = st ; i < en ; i++)
			a[i]--;
		return calc(st,st+(en-st)/2)+calc(st+(en-st)/2,en)+1;
	}
	return 0;
}

int main()
{
#ifdef SMALL
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("b-large.in","rt",stdin);
	freopen("b-large.out","wt",stdout);
#endif


	int n,tt,t=0,res= 0,tmp ;
	scanf("%d",&tt);

	while(tt--)
	{
		res = 0;
		scanf("%d",&n);
		int tms = 1<<n;
		memset(a,0,sizeof a);
		for(int i= 0 ; i < tms ; i++)
		{
			scanf("%d",a+i);
			a[i]=n-a[i];
		}
		for(int i = n-1 ; i >= 0 ; i--)
		for(int j =0 ; j < (1<<i) ; j++)
			scanf("%d",&tmp);
		res=  calc(0,1<<n);

		printf("Case #%d: %d\n",++t,res);

	}
	return 0;
}
