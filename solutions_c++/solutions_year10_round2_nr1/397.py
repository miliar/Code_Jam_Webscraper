#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t) {
        int m, n;
        cin >> m >> n;
        set<string> X, Y;
        for(int i = 0; i < m; ++i) {
            string s;
            cin >> s;
            X.insert(s);
            for(int j = 1; j < s.size(); ++j) {
                if(s[j] == '/') {
                    X.insert(s.substr(0, j));
                }
            }
        }
        for(int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            Y.insert(s);
            for(int j = 1; j < s.size(); ++j) {
                if(s[j] == '/') {
                    Y.insert(s.substr(0, j));
                }
            }
        }
        int ans = 0;
        for(set<string>::iterator iter = Y.begin(); iter != Y.end(); ++iter) {
            if(X.find(*iter) == X.end()) {
                ++ans;
            }
        }
        printf("Case #%d: %d\n", t + 1, ans);
    }
}
