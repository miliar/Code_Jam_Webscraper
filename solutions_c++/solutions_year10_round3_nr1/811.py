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
	int T; scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int n; scanf("%d", &n);
		vector < pair <int, int> > v(n);
		for(int i=0; i<n; ++i)
			scanf("%d %d",&v[i].first, &v[i].second);
		int res = 0;
		for(int i=0; i<n; ++i){
			for(int j=i+1; j<n; ++j){
				if((v[i].first > v[j].first && v[i].second < v[j].second) || (v[i].first < v[j].first && v[i].second > v[j].second))++res;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}