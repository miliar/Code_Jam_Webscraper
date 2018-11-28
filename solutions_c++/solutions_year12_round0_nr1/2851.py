#include <iostream>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int n;
    cin >> n;
    getchar();
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);
        for (int j = 0; j < s.length(); j++) {
            if (s[j] != ' ') {
                s[j] = map[s[j] - 'a'];
            }
        }
        cout << "Case #" << i + 1 << ": " << s << endl;
    }
    return 0;
}
