#include <iostream>
#include <cstdio>
#include <string>
#include <list>

using namespace std;

struct combine {
    char a, b, c;
};

int T, C, D, N, tc;
list<char> elist(1000);
combine comb[1000], oppo[1000];

int main() {
    freopen("E:\\B-large.in", "r", stdin);
    freopen("E:\\B-large.out", "w", stdout);
    int i, j;
    cin >> T;
    string tmps;

    for (tc = 1; tc <= T; tc++) {
        elist.clear();
        cin >> C;
        for (i = 0; i < C; i++) {
            cin >> tmps;
            comb[i].a = tmps[0];
            comb[i].b = tmps[1];
            comb[i].c = tmps[2];
        }
        cin >> D;
        for (i = 0; i < D; i++) {
            cin >> tmps;
            oppo[i].a = tmps[0];
            oppo[i].b = tmps[1];
        }
        cin >> N;
        cin >> tmps;
        bool topush;
        int tmpn;
        for (i = 0; i < N; i++) {
            topush = true;
            for (j = 0; elist.size() > 0 && j < C; j++) {
                if ((tmps[i] == comb[j].a && elist.back() == comb[j].b)
                 || (tmps[i] == comb[j].b && elist.back() == comb[j].a)) {
                    elist.pop_back();
                    elist.push_back(comb[j].c);
                    topush = false;
                    break;
                }
            }
            tmpn = elist.size();
            if (topush) for (j = 0; j < D; j++) {
                if (tmps[i] == oppo[j].a) elist.remove(oppo[j].b);
                if (tmps[i] == oppo[j].b) elist.remove(oppo[j].a);
            }
            if (tmpn != elist.size()) {
                topush = false;
                elist.clear();
            }
            if (topush) elist.push_back(tmps[i]);
        }

        cout << "Case #" << tc << ": ";

        list<char>::iterator it;
        if (elist.size() == 0) cout << "[]";
        else if (elist.size() == 1) cout << "[" << elist.front() << "]";
        else {
            cout << "[" << elist.front();
            it = elist.begin();
            it++;
            for (;it != elist.end(); it++) {
                cout << ", " << (*it);
            }
            cout << "]";
        }

        cout << endl;
    }
    return 0;
}
