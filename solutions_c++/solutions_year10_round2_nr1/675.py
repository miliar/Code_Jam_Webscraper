/*
	Author       :	Jan
	Problem Name :
	Algorithm    :
	Complexity   :
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <sstream>

using namespace std;

int cases, caseno, n, m, res, N1, N2;
char a[2000000], b[2000000];

map <string, int> S;

map < pair <int, int>, int > M;

int getStringId(  char *a ) {
	if( S.find(a) == S.end() ) S[a] = ++N1;
	return S[a];
}

int getDirectoryId(  int idx, int parent, bool flag ) {
	pair <int, int> x = make_pair( idx, parent );
	if( M.find(x) == M.end() ) {
		M[x] = ++N2;
		if( !flag ) res++;
	}
	return M[x];
}

void addToSet( char *a, bool flag ) {
	int i, j, k;
	int parentId = 0;

	for( i = 0; a[i]; i++ ) {
		if( a[i] == '/' ) {
			k = 0;
			for( j = i + 1; a[j]; j++ ) {
				if( a[j] == '/' ) break;
				b[k++] = a[j];
			}
			b[k] = 0;
			k = getStringId(b);
			parentId = getDirectoryId(k, parentId, flag);
			i = j - 1;
		}
	}
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i;
		res = 0;
		N1 = N2 = 0;
		scanf("%d %d", &n, &m);

		M.clear();
		S.clear();
		for( i = 0; i < n; i++ ) {
			scanf("%s", a);
			addToSet(a, true);
		}
		for( i = 0; i < m; i++ ) {
			scanf("%s", a);
			addToSet(a, false);
		}
		printf("Case #%d: %d\n", ++caseno, res);
	}
	return 0;
}
