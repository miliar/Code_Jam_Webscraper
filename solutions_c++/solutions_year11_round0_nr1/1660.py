#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <utility>

using namespace std;

int abs(int n) {
    if (n > 0) return n;
    else return -n;
}

int main() {
    int t;
    cin >> t;

    for (int cn = 1; cn <= t; cn++) {
        int o = 0, b = 0, ol = 1, bl = 1, l, n;
        cin >> l;
        string ts;
        queue<pair<int, int> > bv, ov;
        for (int i = 0; i < l; i++) {
            cin >> ts >> n;
            if (ts.compare("O") == 0) {
                pair<int, int> p(i, n);
                ov.push(p);
            } else {
                pair<int, int> p(i, n);
                bv.push(p);
            }
        }
        
        int nextButton = 0;
        int time = 0;
        while (!bv.empty() || !ov.empty()) {
            time++;
            bool increment = false;
            if (!bv.empty()) {
                if (bv.front().second == bl) {
                    if (nextButton == bv.front().first) {
                        increment = true;
                        bv.pop();
                    }
                } else {
                    int dist = bv.front().second - bl;
                    bl += dist / abs(dist);
                }
            }
            
            if (!ov.empty()) {
                if (ov.front().second == ol) {
                    if (nextButton == ov.front().first) {
                        increment = true; 
                        ov.pop();
                    }
                } else {
                    int dist = ov.front().second - ol;
                    ol += dist / abs(dist);
                }
            }
            if (increment)
                nextButton++;
        }

        cout << "Case #" << cn << ": " << time << endl;
    }
}