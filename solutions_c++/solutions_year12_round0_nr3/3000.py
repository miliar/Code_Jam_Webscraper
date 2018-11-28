#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

//#define LARGE

int d[7];

set<pair<int, int>> s;

int main() {

#ifdef LARGE
    FILE *file = fopen("C-large.txt", "w");
#else
    FILE *file = fopen("C-small.txt", "w");
#endif
    int T; cin >> T;
    for (int t = 0; t < T; t++) {

        int A; cin >> A;
        int B; cin >> B;

        int len = 0;
        {
            int tmp = A;
            for (;;){
                len++;
                tmp /= 10;
                if (!tmp) break;
            }
        }

        s.clear();

        for (int n = A; n <= B; n++){
            int tmp = n;
            for (int j = len - 1; j >= 0; j--){
                int k = (int)pow((double)10, j);
                d[len - j - 1] = tmp / k;
                tmp %= k;
            }

            for (int k = 0; k <= len - 2; k++){
                if (d[len - 1 - k] == 0){
                    continue;
                }
                int m = 0;
                for (int j = len - 1 - k; j < len; j++){
                    m = 10 * m + d[j];
                }
                for (int j = 0; j < len - 1 - k; j++){
                    m = 10 * m + d[j];
                }
                
                if (n < m && m <= B) s.insert(make_pair(n, m));
            }
        }

        fprintf(file, "Case #%d: ", t + 1);
        fprintf(file, "%d\n", s.size());
    }

    return 0;
}
