#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

const int maxn = 512;
const int mod = 1000;
const int m = 19;
const char pattern[m + 1] = "welcome to code jam";
char line[maxn];
int cases, cas = 1, n;
bool possible[32];
int mem[2][m + 10];

void init() {
    memset(possible, false, sizeof(possible));
    for (int i = 0; i < m; ++i) {
        possible[pattern[i] - 'a'] = true;
    }
}

int main() {
    init();
    for (scanf("%d\n", &cases); cases--; ) {
        fgets(line, maxn, stdin);
        n = (int) strlen(line) - 1;
        memset(mem, 0, sizeof(mem));
        int now = 0, next = 1;
        for (int i = 0; i < n; ++i) if (possible[line[i] - 'a']) {
            next = (now ^ 1);
            memcpy(mem[next], mem[now], sizeof(mem[now]));
            if (line[i] == pattern[0]) {
                mem[next][0] = (mem[next][0] + 1) % mod;
            }
            for (int j = 1; j < m; ++j) if (line[i] == pattern[j]) {
                int& res = mem[next][j];
                res = (res + mem[now][j - 1]) % mod;
            }
            now ^= 1;
        }
        printf("Case #%d: %04d\n", cas++, mem[now][m - 1]);
    }
    return 0;
}
