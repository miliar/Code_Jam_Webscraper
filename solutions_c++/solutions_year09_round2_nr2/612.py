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

int cases, caseno;
char a[100];

int main() {
	freopen("b2.in","r",stdin);
	freopen("b2.ans","w",stdout);

	scanf("%d", &cases);
	while(cases--) {
		int len, i, j;
		scanf("%s", a);
		len = strlen(a);
		for( i = len - 1; i >= 0; i-- ) {
			int mn = 1000000, pos;
			for( j = i + 1; j < len; j++ ) {
				if( a[j] > a[i] ) {
					if( a[j] < mn ) {
						mn = a[j];
						pos = j;
					}
				}
			}
			if( mn < 1000000 ) {
				swap( a[i], a[pos] );
				sort( a+i+1, a+len );
				break;
			}
		}
		if( i == -1 ) {
			a[len++] = '0';
			a[len] = 0;
			int mn = 1000000, pos;
			for( i = 0; i < len; i++ ) {
				if( a[i] > '0' && a[i] < mn ) {
					mn = a[i];
					pos = i;
				}
			}
			swap(a[0], a[pos]);
			sort( a+1, a+len );
		}
		printf("Case #%d: %s\n", ++caseno, a);
	}
	return 0;
}
