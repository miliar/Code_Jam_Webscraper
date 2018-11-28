/* c-small.cc
 */
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
#include <iostream>
#include <cstdio>
using namespace std;
int T, N;
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	printf("Case #%d: ", t+1);
	cin >> N;
	int all = 0, c;
	vector<int> v;
	for (int i=0; i<N; ++i) {
	    cin >> c;
	    all ^= c;
	    v.push_back(c);
	}
	if (all) {
	    printf("NO\n");
	    continue;
	}
	printf("%d\n",
	       accumulate(v.begin(), v.end(), 0, plus<int>())
	       - *min_element(v.begin(), v.end()));
    }
}
