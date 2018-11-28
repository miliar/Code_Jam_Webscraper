#include <iostream>
#include <map>
using namespace std;

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        map<string, char> combo;
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            char a, b, c;
            cin >> a >> b >> c;
            combo[string("") + a + b] = c;
            combo[string("") + b + a] = c;
        }
        map<string, bool> erase;
        cin >> n;
        for (int i = 0; i < n; i++) {
            char a, b;
            cin >> a >> b;
            erase[string("") + a + b] = true;
            erase[string("") + b + a] = true;
        }
        string s;
        cin >> n >> s;
        string t;
        for (int i = 0; i < s.size(); i++) {
            t += s[i];
            //cout << i << " " << t << "\n";
            if (t.size() <= 1) continue;
            char a = t[t.size() - 1], b = t[t.size() - 2];
            if (combo[string("") + a + b] != 0)
                t = t.substr(0, t.size() - 2) + combo[string("") + a + b];
            else {
                //cout << "t = " << t << "\n";
                for (int j = 0; j < (int)t.size() - 1; j++) {
                    //cout << j << " " << t << " " << t.size() - 1 << "\n";
                    if (erase[string("") + a + t[j]])
                        t = "";
                }
            }
        }
        cout << "Case #" << cc << ": [";
        for (int i = 0; i < t.size(); i++)
            cout << t[i] << (i < t.size() - 1 ? ", " : "");
        cout << "]\n"; 
    }
}
