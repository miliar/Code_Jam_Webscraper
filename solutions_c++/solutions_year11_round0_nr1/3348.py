#include <iostream>
#include <vector>
#include <string>
using namespace std;
 
struct node {
    int location; string robot;
};
 
int T, N;
 
inline int abs(int x) { return x < 0 ? -x : x; }
 
int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        vector<node> tot;
        for (int n = 0; n < N; n++) {
            node n;
            cin >> n.robot >> n.location;
            tot.push_back(n);
        }
 
        int lastb = 0, lasto = 0, bspot = 1, ospot = 1, time = 0;
        for (int n = 0; n < N; n++) {
            if (tot[n].robot == "B") {
                //int asdf = max(0, abs(tot[n].location - bspot) - (time - lastb));
                //cout << asdf << "\n";
                time += 1 + max(0, abs(tot[n].location - bspot) - (time - lastb));
                lastb = time; bspot = tot[n].location;
            }
            else {
                //int asdf = max(0, abs(tot[n].location - ospot) - (time - lasto));
                //cout << asdf << "\n";
                time += 1 + max(0, abs(tot[n].location - ospot) - (time - lasto));
                lasto = time; ospot = tot[n].location;
            }
        }
        cout << "Case #" << t << ": " << time << "\n";
    }
}