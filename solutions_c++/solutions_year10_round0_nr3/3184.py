/*
  GCJ 2010: Theme Park
*/
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <queue>

#define print(x) cout << #x" = " << x << endl

using namespace std;

long long R, K, N;
queue<long long> q1, q2;
long long ret, k, g;


int main(void) {
    int t = 1, n;

    cin >> n;

    while(n--) {
        cin >> R >> K >> N;
        ret = 0;
        q1 = queue<long long>();
        q2 = queue<long long>();

        for (int i = 0; i < N; i++) {
            cin >> g;
            q1.push(g);
        }

        while (R > 0) {
            k = K;
            while (!q1.empty() && (k - q1.front()) >= 0) {
                g = q1.front();
                q1.pop();
                k -= g;
                q2.push(g);
            }

            ret += K - k;
            R--;
            while (!q2.empty()) {
                q1.push(q2.front());
                q2.pop();
            }
        }

        cout << "Case #" << t++ << ": " << ret << endl;
    }

    return 0;
}
