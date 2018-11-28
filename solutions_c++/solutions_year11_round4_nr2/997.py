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
const long double M_PI=acos((long double)-1);
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

long long arr1[502][502];
long long sum1[502][502];
//long long arr2[502][502];
//long long sum2[502][502];
long long getSum(int t,int l,int b,int r,long long sum[502][502])
{
	return sum[b][r]-sum[t-1][r]-sum[b][l-1]+sum[t-1][l-1];
}
bool ok(int t,int l,int k,long long sum[502][502],long long arr[502][502])
{
	int ll=-k+1;
	int tt=-k+1;
	long long s1=0;
	long long s2=0;
	rep(i,k)
	{
		s1+=getSum(t+(i==0||i==k-1),l+i,t+k-1-(i==0||i==k-1),l+i,sum)*ll;
		s2+=getSum(t+i,l+(i==0||i==k-1),t+i,l+k-1-(i==0||i==k-1),sum)*tt;
		ll+=2;
		tt+=2;
	}
	return s1==0 && s2==0;

}
//bool ok(int t,int l,int k,long long sum[502][502],long long arr[502][502],int bs)
//{
//	int b=t+k-1;
//	int r=l+k-1;
//	long long sm=getSum(t,l,b,r,sum)-arr[t][l]-arr[t][r]-arr[b][l]-arr[b][r];
//	long long ar=k*k-4;
//	return 2*sm==(2*bs+k)*ar;
//}
int main() {
	std::ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int T;
	scanf("%d",&T);
	rep(tt,T) {
		int r, c, d;
		scanf("%d%d%d",&r,&c,&d);
		memset(sum1, 0, sizeof sum1);
		rep2(i,1,r)
			rep2(j,1,c) {
				//cin >> arr[i][j];
			int x;
				scanf(" %1d",&x);
				arr1[i][j]=d+x;
				//arr2[i][j]=j*(x);
				sum1[i][j] = arr1[i][j] + sum1[i][j - 1] + sum1[i - 1][j] - sum1[i
						- 1][j - 1];
				//sum2[i][j] = arr2[i][j] + sum2[i][j - 1] + sum2[i - 1][j] - sum2[i
				//						- 1][j - 1];
			}
		rrep2(k,min(r,c),3) {
			rep2(t,1,r-k+1)
				rep2(l,1,c-k+1) {
					//int tt=t+k/2+k%2;
					//int ll=l+k/2+k%2;
					//int sumTop=getSum(t,l,t+k/2-1,l+k-1)-arr[t][l]-arr[t][l+k-1];
					//int sumBottom=getSum(tt,l,tt+k/2-1,l+k-1)-arr[tt+k/2-1][l]-arr[tt+k/2-1][l+k-1];
					//int sumLeft=getSum(t,l,t+k-1,l+k/2-1)-arr[t][l]-arr[t+k-1][l];
					//int sumRight=getSum(t,ll,t+k-1,ll+k/2-1)-arr[t][ll+k/2-1]-arr[t+k-1][ll+k/2-1];
					//if(sumTop==sumBottom && sumLeft==sumRight)
					//{
					//	printf("Case #%d: %d\n", tt + 1, k);
					//	goto next;
					//}
					if(ok(t,l,k,sum1,arr1) )
					{
						printf("Case #%d: %d\n", tt + 1, k);
						goto next;
					}
				}
		}

		printf("Case #%d: %s\n", tt + 1, "IMPOSSIBLE");
		next:;
		cerr << tt << endl;
	}
	return 0;
}
