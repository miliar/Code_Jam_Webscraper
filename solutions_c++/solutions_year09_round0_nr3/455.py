#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>

using namespace std;

const string target = "$welcome to code jam";
const int t_size = 20, len_max = 500 + 10, mod = 10000; 

int cnt[t_size];

void solve();
int get_cnt(const string&);

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    cin.get();
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}

void solve() {
    string str;
    getline(cin, str);
    cout << setfill('0') << setw(4) << get_cnt(str) << endl;
}

int get_cnt(const string& str) {
    memset(cnt, 0, sizeof(cnt));
    cnt[0] = 1;
    for (string::const_iterator i = str.begin(); i != str.end(); ++i)
        for (string::const_iterator j = target.begin(); j != target.end(); ++j)
            if (*i == *j)
                cnt[j - target.begin()]  = (cnt[j - target.begin()] + cnt[j - target.begin() - 1]) % mod;
    return cnt[target.size() - 1];
}
