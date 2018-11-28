#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

char s[5][5];
int T;
bool flag;

char get(int x) {
    return s[x >> 2][x & 3];
}

void push(vector<int>& t, char c) {
    if (c != 'T') {
        t.push_back(c);
    }
}
void check(int a, int b, int c, int d) {
    if (flag)
        return;
    vector<int> t;
    push(t, get(a));
    push(t, get(b));
    push(t, get(c));
    push(t, get(d));
    sort(t.begin(), t.end());
    if (t.front() == t.back() && t.front() != '.') {
        printf("%c won\n", t.front());
        flag = 1;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        flag = 0;
        for (int i = 0; i < 4; ++i) {
            scanf("%s", s[i]);
        }
        printf("Case #%d: ", test);
        for (int i = 0; i < 4; ++i) {
            check(i * 4, i * 4 + 1, i * 4 + 2, i * 4 + 3);
            check(i, i + 4, i + 8, i + 12);
        }
        check(0, 5, 10, 15);
        check(3, 6, 9, 12);
        if (!flag) {
            for (int i = 0; i < 16; ++i)
                if (get(i) == '.') {
                    puts("Game has not completed");
                    flag = 1;
                    break;
                }
            if (!flag) {
                puts("Draw");
            }
        }
    }
    return 0;
}

