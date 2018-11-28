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
		int n; 
		i64 k; scanf("%d %lld",&n, &k);
		bool ok;
		if(n == 1){
			if(k>=1 && k%2 == 1)ok = true;
			else ok = false;
		}else{
			i64 mask = (1 << n) - 1;
			ok = mask == (k & mask);
		}
		if(ok)printf("Case #%d: ON\n",t);
		else printf("Case #%d: OFF\n",t);
	}
	return 0;
}