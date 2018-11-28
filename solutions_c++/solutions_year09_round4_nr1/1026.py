#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>

#include <queue>
#include <vector>
#include <string>
#include <iostream>

#include <algorithm>

using namespace std;

class point {
	int i;
	int j;
	point(int i, int j) {
		this->i = i;
		this->j = j;
	}
};


int main(void) {
	int T, N;
	scanf("%d", &T);
	for ( int test = 0; test < T; test++ ) {
		scanf("%d", &N);
		int data[N];
		for ( int i = 0; i < N; i++ ) {
			data[i] = -1;
			getchar();
			for ( int j = 0; j < N; j++ ) {
				char c = getchar();
//				scanf("%c", &c);
				if ( c == '1' && data[i] < j ) {
					data[i] = j;
				}
				else {
					assert(c == '0');
				}
			}
		}
		int cnt = 0;
		for ( int i = 0; i < N; i++ ) {
			for ( int j = i; j < N; j++ ) {
				if ( data[j] <= i ) {
					for ( int k = j; k > i; k-- ) {
						data[k] = data[k-1];
						cnt++;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", test+1, cnt);
	}
	
	return 0;
}
