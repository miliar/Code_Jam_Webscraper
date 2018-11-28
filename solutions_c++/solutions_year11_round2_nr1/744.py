#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm> 

#define sz(x) ((int)x.size()) 
#define all(x) (x).begin(), (x).end() 
#define pb(x) push_back(x) 
#define mp(x, y) make_pair(x, y) 

typedef long long int64; 

using namespace std;

void put_it(int test) {
     cout << "Case #" << test + 1 << ":";
}

long double get_ans(long double x, long double y, long double z) {
    return 0.25 * x + 0.5 * y + 0.25 * z;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n;
        vector<string> a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        put_it(test);
        cout << endl;
        vector<long double> b(n, 0);
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = 0; j < n; ++j)
                if (a[i][j] != '.') {
                    ++cnt;
                    int wins = 0;
                    int total = 0;
                    for (int k = 0; k < n; ++k)
                        if (k != i && a[j][k] != '.') {
                            if (a[j][k] == '1')
                                ++wins;
                            ++total;
                        }
                    b[i] += (long double)wins / total;
                }
            b[i] /= cnt;
        }
        for (int i = 0; i < n; ++i) {
            int wins = 0;
            int total = 0;        
            for (int j = 0; j < n; ++j)
                if (a[i][j] != '.') {
                    if (a[i][j] == '1')
                        ++wins;
                    ++total;
                }
            long double x = (long double)wins / total;
            long double y = b[i];
            long double z = 0;
            int cnt = 0;
            for (int j = 0; j < n; ++j)
                if (a[i][j] != '.') {
                   ++cnt;
                   z += b[j];
                }
            z /= cnt;
            printf("%.10lf\n", (double)get_ans(x, y, z));
        }
    }
    return 0;
}
