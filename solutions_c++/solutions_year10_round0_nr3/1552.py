#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;

typedef long long i64;
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;

int main(){
	freopen("data2.in","r",stdin);
	freopen("data.out","w",stdout);
	int T; scanf("%d",&T);
	for(int t=1; t<=T; ++t){
		i64 r,k,n; scanf("%lld %lld %lld",&r, &k, &n);
		vector <i64> v(n);
		i64 profit = 0LL;
		for(int i = 0; i<n; ++i)
			scanf("%lld",&v[i]);
		vector < pair <i64, i64> > mark(n, pair <i64,i64>(-1,0LL));
		int j = 0;
		i64 i;
		for(i=0LL; i<r; ++i){
			if(mark[j].first != -1LL)break;
			mark[j].first = i, mark[j].second = profit; 
			i64 next = 0LL;
			for(int w=0; w < n && next + v[j] <= k; ++w, next += v[j], j=(j+1)%n);
			profit += next;
		}
		if(i == r)printf("Case #%d: %lld\n",t,profit);
		else{
			i64 dr = i - mark[j].first, dprof = profit - mark[j].second;
			i64 rest = r - i;
			profit += (rest/dr)*dprof;
			i = 0LL;
			for(i64 m = rest%dr; i<m; ++i){
				i64 next = 0LL;
				for(int w=0; w<n && next +v[j] <= k; ++w, next += v[j], j=(j+1)%n);
				profit += next;
			}
			printf("Case #%d: %lld\n",t,profit);
		}
	}
	return 0;
}