#include <string>
#include <vector>
#include <map>

#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;
typedef map<pair<char, char>, char> List;

int main() {
	int T;
	freopen("B-large.in", "r", stdin);
	scanf("%d", &T);
	char buf[101];
	for (int k = 1; k <= T; k++) {
		List combine, opposed;
		int C, D, N;
		scanf("%d", &C);
		for (int i = 0; i < C; i++) {
			scanf("%s", buf);
			combine[make_pair(buf[0], buf[1])] = buf[2];
			combine[make_pair(buf[1], buf[0])] = buf[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; i++) {
			scanf("%s", buf);
			opposed[make_pair(buf[0], buf[1])] = ' ';
			opposed[make_pair(buf[1], buf[0])] = ' ';
		}
		scanf("%d", &N);
		scanf("%s", buf);
		vector<char> res;
		for (int i = 0; i < N; i++) {
			if (res.empty()) {
				res.push_back(buf[i]);
				continue;
			}
			if (combine.find(make_pair(buf[i], res[res.size() - 1])) != combine.end()) {
				char tmp = combine[make_pair(buf[i], res[res.size() - 1])];
				res.pop_back();
				res.push_back(tmp);
				continue;
			}
			bool ok = false;
			for (int j = 0; j < res.size(); ++j) {
				if (opposed.find(make_pair(buf[i], res[j])) != opposed.end()) 
					ok = true;
			}
			if (ok)
				res.clear();
			else
				res.push_back(buf[i]);
		}
		if (res.empty()) 
			printf("Case #%d: []\n", k);
		else {
			printf("Case #%d: [%c", k, res[0]);
			for (int i = 1; i < res.size(); i++) 
				printf(", %c", res[i]);
			printf("]\n");
		}
	}
	return 0;
}
