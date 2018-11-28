#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct T {
    string name;
    vector<T> next;
};

T dummy;

int insert(T &root, const vector<string> &p, int idx) {
    if (idx == (int) p.size()) {
        return 0;
    }
    for (int i = 0; i < (int) root.next.size(); i++) {
        if (root.next[i].name == p[idx]) {
            return insert(root.next[i], p, idx + 1);
        }
    }
    T x;
    x.name = p[idx];
    x.next.clear();
    root.next.push_back(x);
    return insert(root.next.back(), p, idx + 1) + 1;
}

int t;
int n, m;

vector<string> split(string str) {
    for (int i = 0; i < (int) str.length(); i++) {
        if (str[i] == '/') {
            str[i] = ' ';
        }
    }
    istringstream is(str);
    string c;
    vector<string> ret;
    while (is >> c) {
        ret.push_back(c);
    }
    return ret;
}

int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        dummy.next.clear();
        cin >> n >> m;
        for (int j = 0; j < n; j++) {
            string str;
            cin >> str;
            insert(dummy, split(str), 0);
        }
        int result = 0;
        for (int j = 0; j < m; j++) {
            string str;
            cin >> str;
            result += insert(dummy, split(str), 0);
        }
        cout << "Case #" << (i + 1) << ": " << result << endl;
    }
    return 0;
}

