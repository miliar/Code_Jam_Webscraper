#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
template<class T> string i2s(T x) { ostringstream o; o<<x; return o.str(); }

int id(char c) {
    switch (c)
	{
	case 'Q': return 0;
	case 'W': return 1;
	case 'E': return 2;
	case 'R': return 3;
	case 'A': return 4;
	case 'S': return 5;
	case 'D': return 6;
	case 'F': return 7;
	default: return -1;
	}
}

map<char, char> comb[8];
set<char> oppo[8];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, C, D, N;
    char s[200];
    
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
	for (int i = 0; i < 8; ++i) {
	    comb[i].clear();
	    oppo[i].clear();
	}
	scanf("%d", &C);
	for (int i = 0; i < C; ++i) {
	    scanf("%s", s);
	    int id1 = id(s[0]);
	    int id2 = id(s[1]);
	    comb[id1][ s[1] ] = s[2];
	    comb[id2][ s[0] ] = s[2];
	}
	scanf("%d", &D);
	for (int i = 0; i < D; ++i) {
	    scanf("%s", s);
	    int id1 = id(s[0]);
	    int id2 = id(s[1]);
	    oppo[id1].insert(s[1]);
	    oppo[id2].insert(s[0]);
	}
	scanf("%d %s", &N, s);
	vector<char> ans;
	for (int i = 0; i < N; ++i) {
	    ans.push_back(s[i]);
	    int sz = ans.size();
	    if (sz <= 1)
		continue;
	    int id1 = id(ans[sz-1]);
	    if (comb[id1].count(ans[sz-2]) != 0) {
		char newc = comb[id1][ ans[sz-2] ];
		ans.pop_back();
		ans.pop_back();
		ans.push_back(newc);
	    } else {
		bool ok = true;
		for (int j = 0; j < sz - 1; ++j) {
		    if (oppo[id1].find(ans[j]) != oppo[id1].end()) {
			ok = false;
			break;
		    }
		}
		if (!ok)
		    ans.clear();
	    }
	}
	printf("Case #%d: [", cas);
	for (int i = 0; i < ans.size(); ++i) {
	    if (i < ans.size() - 1)
		printf("%c, ", ans[i]);
	    else
		printf("%c]\n", ans[i]);
	}
	if (ans.size() == 0)
	    puts("]");
    }
    return 0;
}
