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

int memo[1010][1010];
bool mark[1010][1010];

int f(const vector <int> &v, int i, int w, int a, int b){
	if(i+w == (int) v.size()){
		if(a == b && i > 0 && w > 0)
			return 0;
		else 
			return -1;
	}
	int &best = memo[i][w];
	//if(mark[i][w])return true;
	//mark[i][w] = true;
	int t0 = f(v,i+1,w,a^v[i+w],b);
	int t1 = f(v,i,w+1,a,b^v[i+w]);
	if(t1 > -1)t1 += v[i+w];
	best = max(t0,t1);
	return best;
}

int main(){
	freopen("C-small-0.in","r",stdin);
	freopen("C-small-0.out","w",stdout);
	int T; scanf("%d\n", &T);
	for(int t=1; t<=T; ++t){
		int n; scanf("%d\n", &n);
		vector <int> v(n);
		for(int i=0; i<n; ++i){
			scanf("%d", &v[i]);
		}
		memset(mark,false,sizeof(mark));
		int res = f(v, 0, 0, 0, 0);
		if(res == -1){
			printf("Case #%d: NO\n", t);
		}else printf("Case #%d: %d\n",t, res);
	}
	return 0;
}