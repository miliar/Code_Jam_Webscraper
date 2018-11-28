#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

vector<string> dic;
char in[256];
bool hash[16][32];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int L, D, N;
    while (scanf("%d %d %d", &L, &D, &N) != EOF) {
        dic.clear();
        for (int i = 0; i < D; ++i) {
            scanf("%s", in);
            dic.push_back(string(in));
        }
        for (int i = 0; i < N; ++i) {
            scanf("%s", in);
            memset(hash, false, sizeof(hash));
            string tmp(in);
            int cnt = 0;
            for (int j = 0; j < tmp.size(); ++j) {
                if (tmp[j] == '(') {
                    int x = j + 1;
                    while (x < tmp.size() && islower(tmp[x])) {
                        hash[cnt][tmp[x] - 'a'] = true;
                        ++x;
                    }
                    j = x;
                    ++cnt;
                }
                else if (tmp[j] >= 'a' && tmp[j] <= 'z') {
                    hash[cnt++][tmp[j] - 'a'] = true;
                }
            }
            int ans = 0;
            for (int j = 0; j < dic.size(); ++j) {
                bool ok = true;
                for (int k = 0; k < dic[j].size(); ++k) {
                    if (!hash[k][dic[j][k] - 'a']) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    ++ans;
                }
            }
            printf("Case #%d: %d\n", i + 1, ans);
        }
    }
    return 0;
}
