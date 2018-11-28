#include <iostream>
#include <cstdio>
#include <string>
#include <vector>


using namespace std;

int T;
int n;
vector<string> next;
vector<int> nexto;
vector<int> nextb;
int nowo, nowb;
int ttime;

int main() {
    freopen("E:\\A-large.in", "r", stdin);
    freopen("E:\\A-large.out", "w", stdout);
    cin >> T;
    int tc;
    int i;
    int tmpn;
    string tmps;
    int step;
    for (tc = 1; tc <= T; tc++) {
        cin >> n;
        ttime = 0;
        next.clear();
        nexto.clear();
        nextb.clear();
        for (i = 0; i < n; i++) {
            cin >> tmps >> tmpn;
            next.push_back(tmps);
            if (tmps == "O") nexto.push_back(tmpn);
            else nextb.push_back(tmpn);
        }
        nowo = nowb = 1;
        ttime = 0;
        step = 0;
        int i, j;
        i = j = 0;
        bool stepped;
        while (step < n) {
            stepped = false;
            if (nowo != nexto[i]) {
                if (nowo < nexto[i]) nowo++;
                else nowo--;
            } else {
                if (next[step] == "O") {
                    i++;
                    step++;
                    stepped = true;
                }
            }
            if (nowb != nextb[j]) {
                if (nowb < nextb[j]) nowb++;
                else nowb--;
            } else {
                if (!stepped && next[step] == "B") {
                    j++;
                    step++;
                }
            }
            ttime++;
        }
        cout << "Case #" << tc << ": ";
        cout << ttime << endl;
        
    }

    return 0;
}
