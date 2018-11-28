/* small-B.cc
 */
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int T;
string N;
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	cout << "Case #" << t+1 << ": ";
	cin >> N;
	if (next_permutation(N.begin(), N.end())) {
	    cout << N << endl;
	    continue;
	}
	sort(N.begin(), N.end());
	size_t p=0;
	while (N[p] == '0')
	    ++p;
	N.erase(N.begin(), N.begin()+p);
	cout << N[0] << string(p+1, '0') << N.substr(1) << endl;
    }
}
// 1:53
