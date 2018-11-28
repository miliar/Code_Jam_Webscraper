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

int f(vector < pair <char, int> > &v, int n){
	int res = 0, r0=1,r1=1, gap = 0;
	char robot = v[0].first;
	int next = 0;
	
	for(int i=0; i<n; ++i){
		if(robot == v[i].first){
			if(robot == 'O'){
				next += abs(r0 - v[i].second)+1;
				r0 = v[i].second;
			}else{
				next += abs(r1 - v[i].second)+1;
				r1 = v[i].second;
			}
		}else{
			res += next;
			gap = next;
			robot = v[i].first;
			if(robot == 'O'){
				next = max(0,abs(r0 - v[i].second)-gap)+1;
				r0 = v[i].second;
			}else{
				next = max(0,abs(r1 - v[i].second)-gap)+1;
				r1 = v[i].second;
			}
		}
	}
	res += next;
	return res;
}

int main(){
	freopen("A-large-0.in","r",stdin);
	freopen("A-large-0.out", "w", stdout);
	int T; scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int n; scanf("%d", &n);
		vector < pair<char, int> > v(n);
		for(int i=0; i<n; ++i){
			scanf(" %c %d", &v[i].first, &v[i].second);
		}
		int res = f(v,n);
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}