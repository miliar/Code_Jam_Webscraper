#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

int pairChar(char c1, char c2) {
	return (((int)c1)&255) | ((((int)c2)&255)<<8);
}

class MyCmp {
public:
	inline bool operator () (const string & x, const string & y) const {
		if(x.size()!=y.size()) {
			return x.size() < y.size();
		}
		return x < y;
	}
};

int main() {
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; ++t) {
		int N;
		scanf("%d", &N);
		vector<string> v;
		for(int n=0; n<N; ++n) {
			char buf[65536+256];
			scanf("%s", buf);
			v.push_back(buf);
		}
		vector<string> v2 = v;
		sort(v2.begin(), v2.end(), MyCmp());
		int cnt = 0;
		for(int n=0; n<N; ++n) {
			if(v2[n]!=v[n]) {
				++cnt;
			}
		}
		printf("Case #%d: %d.000000\n", t + 1, cnt);
	}
	return 0;
}
