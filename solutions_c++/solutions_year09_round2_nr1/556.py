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

int cases, n, N, caseno;
char a[2000000], b[2000000];

set <string> S;

struct tree {
	double val;
	char a[25];
	int L, R;
}T[200000];

bool isDigit( int a ) {
	return isdigit(a) || a == '.';
}

int call( int &i ) {
	i++;
	
	while( !isDigit( a[i] ) ) i++;
	int k = 0;
	while( isDigit( a[i] ) ) b[k++] = a[i++];
	b[k] = 0;

	sscanf(b, "%lf", &T[N].val);
	bool found = false;
	for( ; ;i++ ) {
		if( isalpha(a[i]) ) {
			found = true;
			break;
		}
		if( a[i] == ')' ) {
			i++;
			break;
		}
	}
	if( found ) {
		k = 0;
		while( isalpha( a[i] ) ) T[N].a[k++] = a[i++];
		T[N].a[k] = 0;
		int x = N++;
		while( a[i] != '(' ) i++;
		T[x].L = call( i );
		while( a[i] != '(' ) i++;
		T[x].R = call( i );
		while( a[i] != ')' ) i++;
		i++;
		return x;
	}
	else {
		T[N].a[0] = '-';
		N++;
		return N - 1;
	}
}

double call( int i, double p ) {
	p *= T[i].val;
	if( T[i].a[0] == '-' ) return p;
	if( S.find( T[i].a ) != S.end() ) return call( T[i].L, p );
	return call( T[i].R, p );
}

int main() {
	freopen("a2.in","r",stdin);
	freopen("a2.ans","w",stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int x, i, q;
		scanf("%d", &x);
		gets(a);
		a[0] = 0;
		while( x-- ) {
			gets(b);
			strcat( a, b );
		}
		N = 0;
		for( i = 0; a[i]; i++ ) {
			if( a[i] == '(' ) {
				call( i );
				break;
			}
		}
		printf("Case #%d:\n", ++caseno);
		scanf("%d", &q);
		while( q-- ) {
			scanf("%s %d", b, &n);
			S.clear();
			for( i = 0; i < n; i++ ) {
				scanf("%s", b);
				S.insert(b);
			}
			printf("%.10lf\n", call( 0, 1 ) + 1e-11 );
		}
	}
	return 0;
}
