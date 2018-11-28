/* d-small.cc
 */
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
int T, N, A[1024];
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> N;
	for (int i=0; i<N; ++i) cin >> A[i];
	int sum = 0;
	for (int i=0; i<N; ++i) sum += (A[i] != (i+1));
	printf("Case #%d: %d.000000\n", t+1, sum);
    }
}
