#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>

using namespace std;

bool NeedClear(const string &s, const vector<string> &ers) {
    set<char> letters;
    for (size_t i = 0, sz = s.size(); i < sz; ++i)
        letters.insert(s[i]);
    for (vector<string>::const_iterator it = ers.begin(), end = ers.end(); it != end; ++it) {
        if (letters.find((*it)[0]) != letters.end() && letters.find((*it)[1]) != letters.end())
            return true;
    }
    return false;
}

string Work() {
    map<string, char> cmb;
    string s;
    size_t n;
    cin >> n;
    for (; n > 0; --n) {
        cin >> s;
        cmb[s.substr(0, 2)] = s[2];
        swap(s[0], s[1]);
        cmb[s.substr(0, 2)] = s[2];
    }
    cin >> n;
    vector<string> ers(n);
    for (size_t i = 0; i < n; ++i)
        cin >> ers[i];
    cin >> n;
    cin >> s;
    string res;
    for (size_t i = 0, sz = s.size(); i < sz; ++i) {
        res += s[i];
        if (res.size() > 1) {
            string c = res.substr(res.size() - 2);
            map<string, char>::const_iterator it = cmb.find(c);
            if (it != cmb.end()) {
                res = res.substr(0, res.size() - 2);
                res += it->second;
            } else if (NeedClear(res, ers)) {
                res.clear();
            }
        }
    }
    return res;
}

void Output(size_t k, const string &res) {
    cout << "Case #" << k << ": [";
    for (size_t i = 0, sz = res.size(); i < sz; ++i) {
        if (i != 0)
            cout << ", ";
        cout << res[i];
    }
    cout << "]" << endl;
}

int main() {
    size_t t;
    cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        Output(i, Work());
    }
    return 0;
}

