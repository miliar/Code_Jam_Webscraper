#include <iostream>
#include <map>

using namespace std;

int main() {
    int n;
    cin >> n;
    string str;
    for (int c = 1; c <= n; c ++) {
        int s, q;
        cin >> s;
        getline(cin, str);
        map<string, int> used;
        for (int i = 0; i < s; i ++) {
            getline(cin, str);
            used[str] = 0;
        }
        int num = s, res = 0;
        cin >> q;
        getline(cin, str);
        for (int i = 0; i < q; i ++) {
            getline(cin, str);
            if (used[str] == res) {
                if (num == 1) {
                    res += 1;
                    used[str] += 1;
                    num = s;
                }
                used[str] += 1;
                num -= 1;
            }
        }
        cout << "Case #" << c << ": " << res << endl;
    }
    return 0;
}
