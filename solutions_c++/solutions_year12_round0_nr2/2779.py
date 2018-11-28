#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <set>

using namespace std;

int get_max(int sum) {
    if (sum <= 2) return 0;
    else return (sum + 4) / 3;
}
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, N, P, S, bad[128];
    cin >> T;
    int testcases = 0;
    while (T --) {
        cin >> N >> S >> P;
        int cnt = 0, sum = 0, num = 0;
        for (int i = 0; i < N; ++ i) {
            cin >> sum;
            if ((sum + 2) / 3 >= P) ++ cnt;
            else if (S > 0 && get_max(sum) >= P) {
                -- S;
                ++ cnt;
            }
        }
        cout << "Case #" << ++ testcases << ": " << cnt << endl;
    }
    return 0;
}
