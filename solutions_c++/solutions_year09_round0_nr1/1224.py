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

char name[5001][20];
char a[2000000];

int caseno, L, D, N;

bool canTake[20][30];

int main() {
	freopen("a2.in","r",stdin);
	freopen("a2.ans","w",stdout);

	int i, j;

	scanf("%d %d %d", &L, &D, &N);
	for( i = 0; i < D; i++ ) {
		scanf("%s", name[i]);
	}
	while( N-- ) {
		scanf("%s", a);
		int len = strlen(a);
		j = 0;
		memset( canTake, 0, sizeof(canTake) );
		for( i = 0; i < len; i++ ) {
			if( a[i] == '(' ) {
				i++;
				while( a[i] != ')' ) {
					canTake[j][ a[i] - 97 ] = true;
					i++;
				}
			}
			else canTake[j][ a[i] - 97 ] = true;
			j++;
		}
		int cnt = 0;
		for( i = 0; i < D; i++ ) {
			for( j = 0; j < L; j++ ) {
				if( !canTake[j][ name[i][j] - 97 ] ) break;
			}
			if( j == L ) cnt++;
		}
		printf("Case #%d: %d\n", ++caseno, cnt);
	}
	return 0;
}
