#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <utility>
#include <numeric>
#include <set>
#include <map>
#include <iostream>

using namespace std;


#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)
#define DEBUG(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define MSET(c, v) memset(c, v, sizeof(c))
#define FOR(i,a,b) for (int i=(a); i < (b); i++)

/////

typedef long long LL;
typedef pair<LL,LL> point;

vector<point> trees;

LL N, n, A, B, C, D, x_0, y_0, M;

int main () {
	scanf(" %lld" , &N);
	for (int _42 = 1; _42 <= N; _42++) {
		trees.clear();
		scanf(" %lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x_0, &y_0, &M);
		LL _X = x_0, _Y = y_0;
		trees.push_back( point(_X,_Y) );
		for (int i=1; i < n; i++) {
			_X = (A*_X + B) % M;
			_Y = (C*_Y + D) % M;
			trees.push_back( point(_X,_Y) );
		}
		LL ans = 0;

		FOR(i,0,n) FOR(j,i+1,n) FOR(k,j+1,n) {
			LL X = (LL)trees[i].first + (LL)trees[j].first + (LL)trees[k].first;
			LL Y = (LL)trees[i].second + (LL)trees[j].second + (LL)trees[k].second;
			if (X%3 != 0) continue;
			if (Y%3 != 0) continue;
			//WATCH(trees[i].first); WATCH(trees[j].first); WATCH(trees[k].first);
			ans++;
		}



		printf("Case #%d: %lld\n", _42, ans);
	}


	return 0;
}



