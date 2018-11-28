#include <iostream>
#include <fstream>
using namespace std;

long long a[1000];
long long s[1000];
long long d[1000];

int main() {
    ifstream fin("C-small-attempt3.in");
    int cases;
    fin >> cases;
    for (int t = 1; t <= cases; t++) {
        int n, m;
        long long x, y, z;
        fin >> n >> m >> x >> y >> z;
        for (int i = 0; i < m; i++) fin >> a[i];
        for (int i = 0; i < n; i++) {
            s[i] = a[i % m];
            a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
        }
        long long result = n;
        for (int i = 0; i < n; i++) d[i] = 1;
        for (int l = 2; l <= n; l++) {
            bool ok = true;
            for (int i = 0; i < n; i++) {
                d[i] = 0;
                for (int j = i + 1; j < n; j++)
                    if (s[i] < s[j]) {
                        d[i] += d[j];
                        d[i] %= 1000000007;
                    }
                if (d[i] > 0) {
                    ok = false;
                    result += d[i];
                    result %= 1000000007;
                }
            }
            if (ok) break;
        }
        cout << "Case #" << t << ": " << result << "\n";
    }
}
