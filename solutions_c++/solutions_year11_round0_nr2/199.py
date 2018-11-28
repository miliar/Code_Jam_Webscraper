#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

int trans[26][26];
int die[26];
int ans[200], *at, cnt[26], mask;
char seq[200];

void clear_ans() {
	fill(cnt, cnt + 26, 0);
	mask = 0;
	at = ans;
}

void pop_ans() {
	--at;
	--cnt[*at];
	if (cnt[*at] == 0)
		mask &= ~(1 << *at);
}

void push_ans(int x) {
	if (mask & die[x]) {
		clear_ans();
	} else {
		*at++ = x;
		++cnt[x];
		if (cnt[x] == 1)
			mask |= 1 << x;
	}
}

string solve() {
	for (int i = 0; i < 26; ++i) {
		for (int j = 0; j < 26; ++j)
			trans[i][j] = -1;
		die[i] = 0;
	}
	{
		int C;
		for (cin >> C; C-- > 0;) {
			char op[10];
			cin >> op;
			int a = op[0] - 'A', b = op[1] - 'A', c = op[2] - 'A';
			trans[a][b] = trans[b][a] = c;
		}
	}
	{
		int D;
		for (cin >> D; D-- > 0;) {
			char op[10];
			cin >> op;
			int a = op[0] - 'A', b = op[1] - 'A';
			die[a] |= 1 << b;
			die[b] |= 1 << a;
		}
	}
	int N;
	cin >> N >> seq;
	clear_ans();
	for (char* p = seq; p < seq + N; ++p) {
		int v = *p - 'A';
		if (at > ans && trans[at[-1]][v] != -1) {
			int x = trans[at[-1]][v];
			pop_ans();
			push_ans(x);
		} else {
			push_ans(v);
		}
	}
	ostringstream ret;
	for (int* p = ans; p < at; ++p) {
		if (p == ans)
			ret << '[';
		else
			ret << ", ";
		ret << static_cast<char>('A' + *p);
	}
	if (at == ans) ret << '[';
	ret << ']';
	return ret.str();
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
