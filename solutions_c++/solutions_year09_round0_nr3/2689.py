#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define INF 1000000000
#define P 10000

string t = "welcome to code jam";

int cnt(int i, string s) {
    if(int(t.size()) == i) return 1;
    int res = 0;
    forn(j, s.size())
        if(t[i] == s[j])
            res += cnt(i + 1, s.substr(j + 1, s.size() - j)), res %= P;
    return res;
}

int main() {
    freopen("input.txt", "rt",stdin);
    int n;
    cin >> n;
    string s;
    vector<int> v;
    freopen("output.txt", "wt", stdout);
    forn(i, n + 1) {
        getline(cin, s);
        v.push_back(cnt(0, s));
    }
    for(int i = 1; i <int(v.size()); ++i) {
        cout << "Case #" << i  << ": ";
        if(v[i] < 10) cout << "000";
        else if(v[i] < 100) cout << "00";
        else if(v[i] < 1000) cout << "0";
        cout << v[i] << endl;
    }

    return 0;
}
