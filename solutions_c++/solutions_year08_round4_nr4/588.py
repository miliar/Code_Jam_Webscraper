/* kaneko-D.cc
 */
#include <vector>
#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int N, k;
string S;
int main()
{
    cin >> N;
    for (int t=0; t<N; ++t) {
	cin >> k >> S;
	int ret = S.size();
	vector<int> v(k);
	for (int i=0; i<k; ++i) v[i] = i;
	do {
	    string s2 = S;
	    for (size_t i=0; i<S.size(); ++i) {
		s2[i] = S[v[i%k]+(i/k)*k];
	    }
	    char prev = ' ';
	    int count = 0;
	    for (size_t i=0; i<s2.size(); ++i) {
		if (s2[i] != prev) {
		    prev = s2[i];
		    ++count;
		}
	    }
	    ret = min(ret, count);
	} while (next_permutation(v.begin(), v.end()));
	printf("Case #%d: %d\n", t+1, ret);
    }
}



