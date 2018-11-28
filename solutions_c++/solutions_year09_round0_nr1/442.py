#include <iostream>
#include <string>

using namespace std;

const int l_max = 15 + 5, d_max = 5000 + 10;

int l, d, n;
string word[d_max];

void solve();
int get_cnt(const string&);

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    solve();
    return 0;
}

void solve() {
    cin >> l >> d >> n;
    for (int i = 0; i < d; ++i)
        cin >> word[i];
    for (int i = 0; i < n; ++i) {
        string str;
        cin >> str;
        cout << "Case #" << i + 1 << ": " << get_cnt(str) << endl;
    }
}

int get_cnt(const string& str) {
    int len = 0;
    bool occur[l_max][26] = {};
    for (string::const_iterator i = str.begin(); i != str.end(); ++i) {
        if (*i == '(') {
            for (++i; *i != ')'; ++i)
                occur[len][*i - 'a'] = true;
        } else
            occur[len][*i - 'a'] = true;
        ++len;
    }
    int res = 0;
    for (int i = 0; i < d; ++i) {
        bool valid = true;
        for (string::iterator j = word[i].begin(); j != word[i].end() && valid; ++j)
            if (!occur[j - word[i].begin()][*j - 'a'])
                valid = false;
        if (valid)
            ++res;
    }
    return res;
}
