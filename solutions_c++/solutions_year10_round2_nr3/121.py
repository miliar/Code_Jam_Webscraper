#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

#define D(x) 

using namespace std;

int choose_table[501][501];
int choose(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0) return 1;
    return (choose_table[n-1][k-1] + choose_table[n-1][k]) % 100003;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int n = 0; n <= 500; n++) {
        for (int k = 0; k <= 500; k++) {
            choose_table[n][k] = choose(n, k);
        }
    }
    int N = 500;
    vector<vector<int> > table(N+1, vector<int>(N+1));
    table[1][0] = 1;
    for (int m = 2; m <= N; m++) {
        for (int k = 0; k < m; k++) {
            long long int total = 0;
            for (int k_ = 0; k_ < k; k_++) {
                D(cout << "\tadding [" << k << "," << k_ << "] = " <<
                        table[k][k_] << "*" << choose(m-k-1, k-k_-1)
                        << endl);
                total += ((long long int) table[k][k_]) * choose(m-k-1, k-k_-1);
                total %= 100003;
            }
            table[m][k] = total % 100003;

            D(cout << "table[" << m << "][" << k << "] = " << table[m][k] << endl);
        }
    }

    for (int testCase = 1; testCase <= numCases; testCase++) {
        int n;
        cin >> n;

        int result = 0;
        for (int i = 0; i <= n; i++) result += table[n][i];
        result %= 100003;
        cout << "Case #" << testCase << ": " << result << endl;
    }
}
