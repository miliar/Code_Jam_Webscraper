#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef long long ll;
typedef unsigned long long ull;

#define REP(i,s,n) for(int (i)=(s), _n=(n);(i) < _n;++(i))
#define FOR(i,s,n) for(int (i)=(s), (_n)=(n);(i) <= (_n);++(i))
#define rep(i,n) REP(i,0,n)

#define ji first
#define ro second
#define pb push_back
#define All(v) (v).begin(), (v).end()

#define MAX 100005

double p[MAX];

int main() {
	int TT; scanf("%d", &TT);
	FOR(T,1,TT) {
		int a, b; scanf("%d%d", &a, &b);
		double semua = 1.0;
		int c = b-a+1;
		rep(i,a) { 
			scanf("%lf", &p[i]); 
			semua *= p[i]; 
		}
		
		double best = (double) semua * c + ((1.0-semua)* (c+b+1));
		for(int i=a-1, k = 1;i >= 0;--i,++k) {
			semua /= p[i];
			best = min(best, (double) semua * (2*k + c) + (1.0-semua) * (2*k + c + b+1));
		}
		best = min(best, (double) b+2.0);
		printf("Case #%d: %.6lf\n", T, best);
	}
	return 0;
}
