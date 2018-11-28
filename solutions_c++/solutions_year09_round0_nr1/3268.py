#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
vector<string> p;
int l, d, n;
map<string, int> m;

long long solve(int idx, int level, string pred) {
    if(level > l) return 0;
    if(!m[pred]) return 0;
    if(level == l) {
        if(m[pred]) {return 1;}
        else {return 0;}
    }
    if(idx >= int(p[level].size())) return 0;
    return solve(0, level + 1, pred + p[level][idx]) + solve(idx + 1, level, pred);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cin >> l >> d >> n;

    forn(i, d) {
        string s;
        cin >> s;
        forn(j, s.size()) {
            ++m[s.substr(0, j)];
        }
        ++m[s];
    }
    forn(i, n) {
        string s, tmp = "";
        cin >> s;
        p.clear();
        bool open = false;
        forn(j, s.size()) {
            if(s[j] == '(') open = true;
            else if(s[j] == ')') {
                p.push_back(tmp);
                tmp = "";
                open = false;
            } else if(open) {
                tmp += s[j];
            } else {
                p.push_back(tmp + s[j]);
                tmp = "";
            }
        }

        cout << "Case #" << i + 1 << ": " << solve(0, 0, "") ;
        if(i < n - 1) cout << endl;
    }

    return 0;
}
