/* a-small.cc
 */
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
int T;
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	int a = 0, b[2] = {0}, c[2] = {0}, N, p;
	char r;
	cin >> N;
	for (int i=0; i<N; ++i) {
	    cin >> r >> p; --p;
	    bool black = (r == 'B');
	    a = std::max(a, c[black] + abs(b[black] - p))+1;
	    b[black] = p;
	    c[black] = a;
	}
	printf("Case #%d: %d\n", t+1, a);
    }
}
