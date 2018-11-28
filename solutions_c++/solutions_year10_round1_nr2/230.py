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
int D,I,M,N;
int arr[102];
int dp [2][256][102];
int calc(bool f,int lst,int cur)
{
	if(cur == N)return 0;
	int& r = dp[f][lst][cur];
	if(r!=-1)return r;
	r = calc(f,lst,cur+1)+D;
	int mx = f?min(255,lst+M):255;
	int mn = f?max(0,lst-M):0;
	for(int i = mn;i<=mx ;i++)
	{
		if(f&&abs(lst-arr[cur])>M)
			r = min(r,calc(f,i,cur)+I);
		r = min(r,calc(1,i,cur+1)+abs(i-arr[cur]));
	}
	return r;
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("b.out","wt",stdout);
	int t = 0;
	scanf("%d",&t);
	for(int i = 0 ; i < t; i++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&N);
		for(int j = 0 ; j < N ; j++)
			scanf("%d",arr+j);
		memset(dp,-1,sizeof dp);
		printf("Case #%d: %d\n",i+1,calc(0,0,0));

	}


	return 0;
}
