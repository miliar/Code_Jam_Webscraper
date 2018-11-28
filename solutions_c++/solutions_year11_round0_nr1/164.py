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

vector<int> blue, org;
vector< pair<char, int> > all;
int N, pos;
char s[10];

void move(vector<int>& v, int ind, int& ps) {
    if (ps < v[ind]) ps++;
    if (ps > v[ind]) ps--;
}

int go() {
    int ind = 0, ind1 = 0, ind2 = 0;
    int bp = 1, op = 1, ret = 0;
    while (ind1 < blue.size() || ind2 < org.size()) {
	if (all[ind].first == 'B' && all[ind].second == bp) {
	    ind++;
	    ind1++;
	    if (ind2 < org.size())
		move(org, ind2, op);
	} else if (all[ind].first == 'O' && all[ind].second == op) {
	    ind++;
	    ind2++;
	    if (ind1 < blue.size())
		move(blue, ind1, bp);
	} else {
	    if (ind2 < org.size())
		move(org, ind2, op);
	    if (ind1 < blue.size())
		move(blue, ind1, bp);
	}
	//printf("blue: %d org: %d ind1: %d ind2: %d\n", bp, op, ind1, ind2); 
	ret++;
    }
    return ret;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
	scanf("%d", &N);
	blue.clear();
	org.clear();
	all.clear();
	for (int i = 0; i < N; ++i) {
	    scanf("%s %d", s, &pos);
	    if (s[0] == 'O') {
		org.push_back(pos);
		all.push_back(make_pair('O', pos));
	    } else {
		blue.push_back(pos);
		all.push_back(make_pair('B', pos));
	    }
	}
	printf("Case #%d: %d\n", cas, go());
    }
    return 0;
}
