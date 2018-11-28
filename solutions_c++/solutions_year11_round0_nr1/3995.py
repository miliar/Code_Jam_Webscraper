#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n;
    cin >> n;
    for (int test = 1; test <= n; ++test) {
        int curpos[2] = {1, 1};
        int freesteps[2] = {0, 0};
        int answ(0);

        int k;
        cin >> k;
        for (int i = 0; i < k; ++i) {
            int pos;
            char chr;
            cin >> chr >> pos;
            
            int who = (chr == 'B') ? 0 : 1;
            int dist = abs(curpos[who] - pos) + 1;
            
            if (freesteps[who] > 0) {
                dist -= freesteps[who];
                if (dist < 1) dist = 1;
                freesteps[who] = 0;
            }
            
            freesteps[who xor 1] += dist;
            curpos[who] = pos;
            answ += dist;
        }
        cout << "Case #" << test << ": " << answ << endl;
    }
    return 0;
}
