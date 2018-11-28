#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T;
    cin>>T;
    int t = 0;
    while (T--) {
        t++;
        int N;
        cin>>N;
        vector<int> P[2];
        vector<pair<int, bool> > O;
        for (int i=0;i<N;i++) {
            char c;
            int d;
            cin>>c>>d;
            if (c == 'O') {
                P[0].push_back(d);
                O.push_back(make_pair(d, 0));
            } else {
                P[1].push_back(d);
                O.push_back(make_pair(d, 1));
            }
        }
        int p[2] = {1,1};
        int c[2] = {0,0};
        int o = 0;
        for (int ans=0;;ans++) {
            if (o == O.size()) {
                cout << "Case #" << t << ": " <<  ans << endl;
                break;
            }
            bool moved[2] = {0};
            if (p[O[o].second] == O[o].first) {
                c[O[o].second]++;
                moved[O[o].second] = true;
                o++; 
            } 
            for (int i=0;i<2;i++) {
                if (moved[i]) continue;
                if (c[i] < P[i].size()) {
                    if (p[i] < P[i][c[i]]) {
                        p[i]++;
                    } else if (p[i] > P[i][c[i]]) {
                        p[i]--;
                    }
                }
            }
        }
    }
}
