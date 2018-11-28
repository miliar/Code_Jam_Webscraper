#include <fstream>
#include <iostream>
#include <set>
using namespace std;

ifstream inf("C-large.in");
ofstream outf("Output.txt");

const int MAXN = 2000001;
//int sums[MAXN];

inline void int_to_arr(int n, int res[], int *len) {
    int tl = 0;
    while (n > 0) {
        res[tl++] = n%10;
        n /= 10;
    }
    for (int i = 0; i < tl/2; i++)
        swap(res[i], res[tl-1-i]);
    *len = tl;
}

inline int arr_to_int(int n[], int len, int k) {
    int res = 0;
    for (int i = k; i < len; i++)
        res = res*10 + n[i];
    for (int i = 0; i < k; i++)
        res = res*10 + n[i];
    return res;
}

int main() {
    int t; inf >> t;
    int A, B, ans, k, m;
    int n, num[10], len;
    for (int T = 1; T <= t; T++) {
        inf >> A >> B;
        ans = 0;
        for (n = A; n <= B; n++) {
            set<int> was;
            num[10], len;
            int_to_arr(n, num, &len);
            for (k = 1; k < len; k++) if (num[k] != 0) {
                m = arr_to_int(num, len, k);
                if (n < m && m >= A && m <= B && was.count(m) == 0) ++ans, was.insert(m);
            }
        }
        outf << "Case #" << T << ": " << ans << "\n";
    }
}
