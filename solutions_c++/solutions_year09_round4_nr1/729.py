// C++ Header

// -- Base
#include <iostream>
#include <sstream>
// Data Structure
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <numeric>
#include <algorithm>

// C Header
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstddef>

using namespace std;

// Global Macro

#define FOR(V,I,L) for(int V=(I);V<(L);(V)++)     // for loop macro start from I until < L
#define FORe(V,I,L) FOR(V,I,L+1)
#define FORd(V,I,L) for(int V=(I);V>=(L);(V)--)
#define REP(V,L) FOR(V,0,L)                           // for loop start from 0
#define REPe(V,L) FORe(V,0,L)
#define REPd(V,I) FORd(V,I,0)
#define IT(adt) adt::iterator        // Create Iterator
#define FOR_EACH(I,C) for(I=(C).begin(); I!=(C).end(); ++I)    // for loop for iterator

typedef pair<int ,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int    ui;
typedef long double     ld;

char s[1111][1111];

int N;
pii a[1111];

int main(void) {
	freopen("A-large (1).in", "r", stdin);
	freopen("A-large (1).out", "w", stdout);


	int T; scanf("%d" ,&T);
	int tc=1;
	while(T--) {
		scanf("%d", &N);
		for(int i=1;i<=N;i++) {
			s[i][0]='1';
			scanf("%s", &s[i][1]);
		}

		for(int i=1;i<=N;i++) {
			a[i].first = max(0, strrchr(s[i], '1') - s[i]);
			a[i].second = i;
		}

		//sort(a+1, a+N+1);

		int res=0;
		for(int i=1;i<=N;i++)  {
			int mi = -1;
			int mv = INT_MAX;

			for(int j=1;j<=N;j++) {
				if(a[j].second >= i && a[j].first <= i && mv>a[j].second) {
					mv = a[j].second;
					mi = j;
				}
			}
			int v = mv-i;
			for(int j=1;j<=N;j++) if(i<=a[j].second && a[j].second < mv) a[j].second++;
			a[mi].second = i;

			res += v;
		}
		printf("Case #%d: %d\n", tc++, res);
	}
	return 0;
}
