#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<VC> VVC;

const string base = "QWERASDF";

void escriu(VC& v) {
    cout << "[";
    for (int i = 0; i < v.size(); ++i) {
        if (i != 0) cout << ", ";
        cout << v[i];
    }
    cout << "]" << endl;
}

bool esBase(char c) {
    for (int i = 0; i < base.size(); ++i) if (c == base[i]) return true;
    return false;
}

void omple(string& s, VVC& combine) {
    if (esBase(s[0]) and esBase(s[1])) combine[s[0] - 'A'][s[1] - 'A'] = combine[s[1] - 'A'][s[0] - 'A'] = s[2];
    else if (esBase(s[0]) and esBase(s[2])) combine[s[0] - 'A'][s[2] - 'A'] = combine[s[2] - 'A'][s[0] - 'A'] = s[1];
    else combine[s[2] - 'A'][s[1] - 'A'] = combine[s[1] - 'A'][s[2] - 'A'] = s[0];
}

int main() {
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        VC v;
        VVC combine(30, VC(30, -1)), oppose(30);
        int c, d;
        cin >> c;
        for (int i = 0; i < c; ++i) {
            string s;
            cin >> s;
            omple(s, combine);
        }
        cin >> d;
        for (int i = 0; i < d; ++i) {
            string s;
            cin >> s;
            oppose[s[0] - 'A'].push_back(s[1] - 'A');
            oppose[s[1] - 'A'].push_back(s[0] - 'A');
        }
        int n;
        cin >> n;
        string s;
        cin >> s;
        VI count(30, 0);
        for (int i = 0; i < n; ++i) {
            if (v.size() == 0) {
                v.push_back(s[i]);
                ++count[s[i] - 'A'];
            }
            else if (combine[v[v.size() - 1] - 'A'][s[i] - 'A'] != -1) {
                --count[v[v.size() - 1] - 'A'];
                v[v.size() - 1] = combine[v[v.size() - 1] - 'A'][s[i] - 'A'];
                ++count[v[v.size() - 1] - 'A'];
            }
            else {
                bool cleared = false;
                for (int j = 0; j < oppose[s[i] - 'A'].size() and not cleared; ++j) {
                    if (count[oppose[s[i] - 'A'][j]] > 0) {
                        cleared = true;
                        v.clear();
                        count = VI(30, 0);
                    }
                }
                if (not cleared) {
                    v.push_back(s[i]);
                    ++count[s[i] - 'A'];
                }
            }
        }
        cout << "Case #" << cas << ": ";
        escriu(v);
    }
}