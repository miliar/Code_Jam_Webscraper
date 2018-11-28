#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int p, k, l;
        vector<int> freq;
        scanf("%d %d %d", &p, &k, &l);
        for (int i = 0; i < l; i++) {
            int f;
            scanf("%d", &f);
            freq.push_back(f);
        }
        sort(freq.begin(), freq.end());
        int sum = 0;
        for (int i = l-1, pos = 0; i >= 0; pos++) {
            for (int num = 0; num < k && i >= 0; num++, i--) {
                sum += (pos+1) * freq[i];
            }
        }
        printf("Case #%d: %d\n", cas, sum);
    }
}
