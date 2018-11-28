#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
#define X first
#define Y second
#define PII pair<int, int>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

using namespace std;

int main() {
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 0; icase < ncase; ++icase) {
        int n;
        long long A, B, C, D, x0, y0, M;
        scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
        vector<long long> x(n);
        vector<long long> y(n);
        
        x[0] = x0;
        y[0] = y0;
        
        for (int i = 1; i < n; ++i) {
            x[i] = (A * x[i-1] + B) % M;
            y[i] = (C * y[i-1] + D) % M;
        }

        long long sol = 0;
        
        for (int i = 0; i < n-2; ++i)
          for (int j = i+1; j < n-1; ++j)
            for (int k = j+1; k < n; ++k)
                if ((x[i] + x[j] + x[k]) % 3 == 0 && (y[i] + y[j] + y[k]) % 3 == 0)
                        ++sol;

        printf("Case #%d: %lld\n", icase+1, sol);
    }
    return 0;
}
