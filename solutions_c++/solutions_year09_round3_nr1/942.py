#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <climits>
#include <cstring>

#define print(x) cout << #x" = " << x << endl

using namespace std;

string N;
int m[260];
int s;

int solve() {
    int seconds = 0;
    int p = 1;

    if (s == 1) {
        s++;
    }

    for (int i = 0; i < N.size(); i++) {
        seconds += p * m[N[N.size() - 1 - i]];
        p *= s;
    }

    return seconds;
}

int main(void) {
    int t = 1, n;

    cin >> n;

    while(n--) {
        cin >> N;
        memset(m, -1, sizeof(m));
        s = 0;

        for (int i = 0; i < N.size(); i++) {
            if (m[N[i]] == -1) {

                if (s == 0) {
                    m[N[i]] = 1;
                } else if (s == 1) {
                    m[N[i]] = 0;
                } else {
                    m[N[i]] = s;
                }
                
                s++;
            }
        }


        cout << "Case #" << t++ << ": " << solve() << endl;
    }

    return 0;
}
