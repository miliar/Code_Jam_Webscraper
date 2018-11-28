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

vector <int> getDigits(int x){
	vector <int> res;
	do{
		res.push_back(x % 10);
		x /= 10;
	}while(x > 0);
	reverse(all(res));
	return res;
}

set < pair <int, int> >mark;

int f(const int a, const int b, int k){
	vector <int> d = getDigits(k);
	int res = 0;
	for(int i=1, n=(int)d.size(); i<n; ++i){
		if(d[i] == 0)continue;
		int next = 0;
		for(int j=i, w=0; w<n; ++w, (j += 1) %= n){
			(next *= 10) += d[j];
		}
		if(next > k && next <= b){
			if(mark.insert( make_pair(k, next)).second)
				res++;
		}
	}
	return res;
}

int main(){
	freopen("C-large-0.in","r",stdin);
	freopen("C-large-0.out", "w", stdout);
	//freopen("data.in","r",stdin);
	//freopen("data.out", "w", stdout);
	int T; scanf("%d\n", &T);
	for(int t=1; t<=T; ++t){
		int a, b; scanf("%d %d", &a, &b);
		int res = 0;
		mark.clear();
		for(int i=a; i<b; ++i){
			res += f(a, b, i);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}