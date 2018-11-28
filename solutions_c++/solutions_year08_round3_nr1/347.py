#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <cstdio>
using namespace std;

int main()
{
	int N;
	scanf("%d", &N);
	for (int c = 0; c < N; ++c) {
		int P,K,L;
		scanf("%d%d%d", &P, &K, &L);
		vector<int> v;
		int realL = 0;
		for (int i = L; --i >= 0; ) {
			int tmp;
			scanf("%d", &tmp);
			v.push_back(tmp);
			if (tmp > 0)
				++realL;
		}
		if (P*K < L) {
			printf ("Case #%d: Impossible\n", c + 1);
		} else {
			sort(v.begin(), v.end());
			long long mult = 1;
			int cnt = K;
			long long out = 0;
			for (int i = v.size(); --i >= 0; ) {
				out += mult * v[i];
				if (--cnt == 0) {
					cnt = K;
					++mult;
				}
			}
			printf ("Case #%d: %lld\n", c + 1, out);
		}
	}
	return 0;
}

