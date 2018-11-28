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
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;
const int INF = 0x3f3f3f3f;

int main(){
	freopen("B-large-0.in","r",stdin);
	freopen("B-large-0.out", "w", stdout);
	//freopen("data.in","r",stdin);
	//freopen("data.out", "w", stdout);
	int T; scanf("%d\n", &T);
	for(int t=1; t<=T; ++t){
		int n, s, p; scanf("%d %d %d", &n, &s, &p);
		vector <int> v(n);
		for(int i=0; i<n; ++i)
			scanf("%d", &v[i]);
		int res = 0;
		for(int i=0; i<n; ++i){
			int a = v[i]/3, b = v[i] % 3;
			if(a >= p){
				++res; 
				continue;
			}
			if(b == 0){
				if(s > 0 && v[i] >= 2 && v[i] <= 28 && a + 1 >= p)res++, s--;
			}else if(b == 1 && a+1 >= p){
				res++;
			}else if(b == 2){
				if(a + 1 >= p)res++;
				else if(s > 0 && v[i] >= 2 && v[i] <= 28 && a + 2 >= p)res++, s--;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}