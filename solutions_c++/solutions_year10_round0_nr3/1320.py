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

#define i64 __int64

i64 sv[1005], A[1005], svq[1005];

int cases, caseno, n, R, K;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("a.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		int i;
		i64 res = 0;
		queue <int> Q;
		scanf("%d %d %d", &R, &K, &n);
		for( i = 0; i < n; i++ ) {
			scanf("%I64d", &A[i]);
			Q.push(i);
		}
		memset( sv, -1, sizeof(sv) );
		for( i = 0; i < R; i++ ) {
			int z = Q.front();
			if( sv[z] != -1 ) {
				while(!Q.empty()) Q.pop();
				Q.push(svq[z]);
				res += sv[z];
			}
			else {
				queue <int> temp;
				i64 x = 0;
				while( !Q.empty() ) {
					x += A[Q.front()];
					if( x <= K ) {
						temp.push(Q.front());
						Q.pop();
					}
					else {
						x -= A[Q.front()];
						break;
					}
				}
				res += x;
				while( !temp.empty() ) {
					Q.push( temp.front() );
					temp.pop();
				}
				sv[z] = x;
				svq[z] = Q.front();
			}
		}
		printf("Case #%d: %I64d\n", ++caseno, res);
	}
	return 0;
}
