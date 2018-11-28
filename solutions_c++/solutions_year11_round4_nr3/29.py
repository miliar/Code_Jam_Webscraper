#include <iostream>
#include <vector>
using namespace std;

const int maxn = 1000000 + 5;

bool v[maxn];

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    vector<long long> z;
    for (int i = 2; i < maxn; ++i) if (!v[i]) {
        z.push_back(i);
        for (int j = i + i; j < maxn; j += i)
            v[j] = true;
    }
    for (int t2 = 1; t2 <= t1; ++t2) {
        long long N, L = 0, R = 1;
        cin >> N;
        for (int i = 0; i < z.size(); ++i) {
            long long j = 1, k = 0;
            while (j * z[i] <= N) {
                ++k;
                j *= z[i];
            }
            if (k) ++L;
            R += k;
        }
        if (N == 1) L = 1;
        cout << "Case #" << t2 << ": " << R - L << endl;
    }
    
    return 0;
}
