#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector <string> D;
int N;

int get_score(string L, int w) {
    int s = 0;
    int valid[110];
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (D[w].size() == D[i].size()) {
            valid[i] = 1;
            cnt++;
        }
        else valid[i] = 0;
    }
    for (int j = 0; j < L.size(); j++) {
        if (cnt == 1) return s;
        int old_cnt = cnt;
        for (int i = 0; i < N; i++) if (valid[i]) {
            int v = 1;
            for (int p = 0; p < D[i].size(); p++) {
                if (D[i][p] == L[j] && D[i][p] != D[w][p]) {
                    v = 0;
                }
                if (D[w][p] == L[j] && D[i][p] != D[w][p]) {
                    v = 0;
                }
            }
            if (!v) {
                valid[i] = 0;
                cnt--;
            }
        }
        int f = 0;
        if (old_cnt == cnt) continue;
        for (int p = 0; p < D[w].size(); p++) {
            if (D[w][p] == L[j]) {
                f = 1;
            }
        }
        if (!f) s++;
    }
    return s;
}

int process(string L) {
    int best_score = 0;
    int best_word = 0;
    for (int i = 0; i < N; i++) {
        int score = get_score(L, i);
        if (score > best_score) {
            best_score = score;
            best_word = i;
        }
    }
    return best_word;
}

string doit() {
    int M;
    cin >> N;
    cin >> M;
    D.clear();
    string t;
    for (int i = 0; i < N; i++) {
        cin >> t;
        D.push_back(t);
    }
    string res = "";
    for (int i = 0; i < M; i++) {
        string L;
        cin >> L;
        if (i > 0) res += " ";
        int r = process(L);
        res += D[r];
    }
    return res;
}

int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        string res = doit();
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
