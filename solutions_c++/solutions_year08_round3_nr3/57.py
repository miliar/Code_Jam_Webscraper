#include <vector>
#include <cstdlib>
#include <cstdio>
#include <map>
using namespace std;

int main() {
    int num; scanf("%d", &num);
    for (int cas = 1; cas <= num; cas++) {
        int n, m, X, Y, Z;
        scanf("%d %d %d %d %d", &n, &m, &X, &Y, &Z);
        int A[100];
        for (int i = 0; i < m; i++) scanf("%d", &A[i]);
       
        long long ans = 0;
        map<int, long long> pos; // == aantal seqs met laatste getal==key
        for (int i = 0; i < n; i++) {
            int val = A[i % m];
        //    printf("%d\n", A[i % m]);
            for (map<int, long long>::iterator it = pos.begin(); it != pos.end(); ++it) {
                if (it->first < val) pos[val] += it->second;
                else break;
            }
            pos[val]++;
            pos[val] %= 1000000007;
            A[i % m] = ((long long) X * A[i % m] + (long long) Y * (i + 1)) % Z;
        }
        for (map<int, long long>::iterator it = pos.begin(); it != pos.end(); ++it) {
            ans += it->second;
            ans %= 1000000007;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
