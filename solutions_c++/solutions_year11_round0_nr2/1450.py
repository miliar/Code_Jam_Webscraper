#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() {
    char combine[26][26], oppose[26][26];
    int n;
    cin>>n;
    cin.get();
    for (int i = 1; i <= n; ++i) {
        memset(combine, 0, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));
        int c;
        string s;
        cin>>c;
        while (c--) {
            cin>>s;
            combine[s[0]-'A'][s[1]-'A'] = s[2];
            combine[s[1]-'A'][s[0]-'A'] = s[2];
        }
        cin>>c;
        while (c--) {
            cin>>s;
            oppose[s[0]-'A'][s[1]-'A'] = 'Y';
            oppose[s[1]-'A'][s[0]-'A'] = 'Y';
        }
        cin>>c>>s;

        string t;
        for (size_t j = 0; j < s.length(); ++j) {
            if (!t.length())
                t += s[j];
            else {
                char ch = s[j];
                bool bCombine = false;
                do {
                    bCombine = t.length() && combine[*t.rbegin()-'A'][ch-'A'];
                    if (bCombine) {
                        ch = combine[*t.rbegin()-'A'][ch-'A'];
                        t.resize(t.length() - 1);
                    }
                } while (bCombine);

                bool bOppose = false;
                for (size_t k = 0; k < t.length() && !bOppose; ++k)
                    if (oppose[t[k] - 'A'][ch - 'A'])
                        bOppose = true;
                if (bOppose)
                    t.clear();
                else
                    t += ch;
            }
        }

        cout<<"Case #"<<i<<": [";
        for (size_t j = 0; j < t.length(); ++j) {
            if (j) cout<<", ";
            cout<<t[j];
        }
        cout<<"]\n";
    }

    return 0;
}
