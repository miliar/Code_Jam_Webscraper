#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> vec1, vec2;
int n;
int main() {
    freopen("A-small-attempt0.in","r", stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while (T--) {
           scanf("%d", &n);
           int x;
           vec1.clear();
           vec2.clear();
           for (int i = 0; i < n; i++) {
                scanf("%d", &x);
                vec1.push_back(x);
           }
           for (int i = 0; i < n; i++) {
                scanf("%d", &x);
                vec2.push_back(x);
           }
           sort(vec1.begin(), vec1.end());
           sort(vec2.begin(), vec2.end());
           int ans = 0;
           for (int i = 0; i < vec1.size(); i++) {
                ans += vec1[i] * vec2[n - 1 - i];
           }
           printf("Case #%d: %d\n", ++cnt, ans);
    }
}
