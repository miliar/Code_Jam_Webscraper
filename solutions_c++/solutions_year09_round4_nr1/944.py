#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

void solve() {
    int N;
    char buf[512];
    vector<int> v;

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", buf);
        int j = N-1;
        while (j > 0) {
            if (buf[j] == '1') break;
            j--;
        }
        v.push_back(j);
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        for (vector<int>::iterator j = v.begin(); j != v.end(); ++j) {
            if (*j <= i) {
                ans += j - v.begin();
                v.erase(j);
                break;
            }
        }
    }

    printf("%d\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d: ", i+1);

        solve();
    }

    return 0;
}
