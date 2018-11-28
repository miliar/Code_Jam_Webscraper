#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

void move(int& what, int where) {
	if (where == -1) return;
    if (what < where)
        ++what;
    else if (what > where)
        --what;
}

int solve() {
    int n;
    scanf("%d\n", &n);
    std::deque< std::pair< char, int > > q;
    for (int i = 0; i < n; ++i) {
        char ch;
        int x;
        scanf("%c%d\n", &ch, &x);
        q.push_back(std::make_pair(ch, x));
    }
    std::deque< int > o(n+1), b(n+1);
    o[n] = b[n] = -1;
    for (int i = n-1; i >= 0; --i) {
        if (q[i].first == 'O') {
            o[i] = q[i].second;
            b[i] = b[i+1];
        } else {
            o[i] = o[i+1];
            b[i] = q[i].second;
        }
    }
    std::pair< char, int > x('O', 1), y('B', 1);
    int res = 0;
    while (!q.empty()) {
        if (q.front() == x) {
            q.pop_front();
            move(y.second, b.front());
            b.pop_front();
            o.pop_front();
        } else if (q.front() == y) {
            q.pop_front();
            move(x.second, o.front());
            b.pop_front();
            o.pop_front();
        } else {
            move(y.second, b.front());
            move(x.second, o.front());
        }
        ++res;
    }
    return res;
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: %d\n", i+1, solve());
    }
        
}