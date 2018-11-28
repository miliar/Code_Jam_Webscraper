#include <iostream>
#include <set>
#include <string>

using namespace std;

set<string> E;

int Work() {
    E.clear();
    E.insert("/");
    int n, m;
    cin >> n >> m;
    int res = 0;
    for (int i = 0; i < n; ++i) {
        string d;
        cin >> d;
        for (size_t p = 0; ;) {
            size_t t = d.find('/', p + 1);
            string s = d.substr(0, t);
            if (E.find(s) == E.end())
                E.insert(s);
            if (t == string::npos)
                break;
            p = t;
        }
    }
    for (int i = 0; i < m; ++i) {
        string d;
        cin >> d;
        for (size_t p = 0; ;) {
            size_t t = d.find('/', p + 1);
            string s = d.substr(0, t);
            if (E.find(s) == E.end()) {
                E.insert(s);
                ++res;
            }
            if (t == string::npos)
                break;
            p = t;
        }
    }
    return res;
}

void Output(int t, int res) {
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        Output(i, Work());
    }
    return 0;
}

