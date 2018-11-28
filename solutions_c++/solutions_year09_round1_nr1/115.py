#include <iostream>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

const int K = 2000000;

bool known[K][11];
bool dp[K][11];

bool isHappy(int x, int base) {
    if (x < K) {
        if (known[x][base]) {
            return dp[x][base];
        }
        known[x][base] = true;
    }

    bool res = false;
    if (x == 1)
        res = true;
    else {
        int sum = 0;
        int temp = x;
        while (temp) {
            int d = (temp % base);
            temp /= base;
            sum += d * d;
        }

        if (isHappy(sum, base)) res = true;
    }

    if (x < K) {
        dp[x][base] = res;
    }
    return res;
}

int main() {
    string s; getline(cin, s);
    int t = atoi(s.c_str());
    for (int tt = 1; tt <= t; tt++) {
        getline(cin, s);
        istringstream iss(s);
        int b;
        vector<int> bases;
        while (iss >> b) {
            bases.push_back(b);
        }

        for (int i = 2; true; i++) {
            bool valid = true;
            for (int j = 0; valid && j < bases.size(); j++) {
                bool h = isHappy(i, bases[j]);
                if (!h) valid = false;
            }

            if (valid) {
                cout << "Case #" << tt << ": " << i << endl;
                break;
            }
        }
    }
    return 0;
}
