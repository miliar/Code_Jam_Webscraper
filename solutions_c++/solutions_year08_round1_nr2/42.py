#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;

set<int> like[2001];
int malt[2001];

int main () {
    int i, j, cse=0;
    int C, N, M;
    cin >> C;
    while (C--) {
        cin >> N >> M;
        for (i=0; i<M; i++) {
            like[i].clear();
            malt[i] = -1;
        }
        for (i=0; i<M; i++) {
            int T;
            cin >> T;
            for (j=0; j<T; j++) {
                int x, y;
                cin >> x >> y;
                if (y == 1) malt[i] = x-1;
                like[i].insert(x-1);
            }
        }
        bool malted[2001];
        for (i=0; i<N; i++) malted[i] = 0;
        bool imposs = 0;
        while (true) {
            set<int> newmalt;
            for (i=0; i<M; i++) {
                if (like[i].size() == 0 && malt[i] < 0) {
                    imposs = 1;
                    break;
                }
                if (malt[i] >= 0 && like[i].size() == 1) {
                    int b = *like[i].begin();
                    newmalt.insert(b);
                    malted[b] = 1;
                }
            }
            set<int>::iterator it;
            for (it=newmalt.begin(); it!=newmalt.end(); it++) {
                for (i=0; i<M; i++) {
                    if (malt[i] == *it) {
                        like[i].clear();
                    }
                    else like[i].erase(*it);
                }
            }
            if (newmalt.empty()) break;
        }
        cout << "Case #" << ++cse << ":";
        if (imposs) cout << " IMPOSSIBLE" << endl;
        else {
            for (i=0; i<N; i++) {
                cout << " " << malted[i];
            }
            cout << endl;
        }
    }
    return 0;
}
