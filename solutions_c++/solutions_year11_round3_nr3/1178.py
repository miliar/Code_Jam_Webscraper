/* c-small.cc
 */
#include <boost/foreach.hpp>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;
int T, N, L, H, A[11234], B[11234], C[11234];
vector<int> u;
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	fill(B, B+H-L+1, 0);
	cin >> N >> L >> H;
	for (int i=0; i<N; ++i) {
	    cin >> A[i];
	    int a = A[i];
	    u.clear();
	    for (int j=2; j<=a; ++j) {
		while (a % j == 0) u.push_back(j), a/=j;
	    }
	    fill(C, C+H+1, 0);
	    C[1] = 1;

	    for (size_t j=0; j<u.size(); ++j) {
		for (int k=H; k>0; --k)
		    if (k*u[j]<=H && C[k]) C[k*u[j]]++;
	    }
	    for (int j=L-(L%A[i]); j<=H; j+=A[i]) C[j]++;
	    for (int j=L; j<=H; ++j) if (C[j]) ++B[j-L];
	}
	printf("Case #%d: ", t+1);
	int q = find(B, B+H-L+1, N) - B;
	if (q+L<=H) printf("%d\n", q+L);
	else printf("NO\n");
    }
}
