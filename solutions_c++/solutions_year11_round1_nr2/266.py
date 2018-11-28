#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <cassert>
using namespace std;
typedef pair<int, string> pp;
int finds(string str, vector<string>::iterator s, vector<string>::iterator e) {
	for(typeof(s) it=s;it!=e;it++) {
		if (*it == str) return it-s;
	}
	return e-s;
}
pp solve(char ord[], vector<string> dic, int loc, int val) {
	pp res(-1, "");
	if (dic.size() <= 1) return make_pair(val, dic[0]);
	char c = ord[loc];
	map<int, vector<string> > m;
	for(int i=0;i<dic.size();i++) {
		int sgn = 0;
		for(int j=0;j<dic[0].length();j++) {
			if (dic[i][j] == c)
				sgn |= 1 << j;
		}
		m[sgn].push_back(dic[i]);
	}
	if (m.count(0) && m[0].size() == dic.size()) return solve(ord, dic, loc+1, val);
	for(typeof(m.begin()) it = m.begin();it != m.end();it++) {
		pp cmp;
		if (it->first)
			cmp = solve(ord, it->second, loc+1, val);
		else
			cmp = solve(ord, it->second, loc+1, val+1);
		if (cmp.first > res.first) {
			res = cmp;
		} else if (cmp.first == res.first) {
			if (finds(res.second, dic.begin(), dic.end()) > finds(cmp.second, dic.begin(), dic.end()))
				res = cmp;
		}
	}
	return res;
}
int main() {
	int T, M, N;
	scanf("%d", &T);
	for(int t=0;t<T;t++) {
		scanf("%d%d\n", &M, &N);
		char tmp[32];
		vector<string> dic[11];
		vector<string> arb;
		for(int i=0;i<M;i++) {
			scanf("%s", tmp);
			dic[strlen(tmp)].push_back(string(tmp));
			arb.push_back(string(tmp));
		}
		printf("Case #%d: ", t+1);
		for(int i=0;i<N;i++) {
			scanf("%s", tmp);
			int maxp = -1; string ans("");
			for(int l=1;l<11;l++) {
				if (dic[l].empty()) continue;
				pp k = solve(tmp, dic[l], 0, 0);
				if (maxp < k.first) {
					maxp = k.first;
					ans = k.second;
				} else if (maxp == k.first && finds(ans, arb.begin(), arb.end()) > finds(k.second, arb.begin(), arb.end()) )
					ans = k.second;
			}
			printf("%s%c", ans.c_str(), i==N-1?'\n':' ');
		}
	}
	return 0;
}
