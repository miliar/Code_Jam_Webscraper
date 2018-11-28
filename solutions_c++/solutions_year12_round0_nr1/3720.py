#include <iostream>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

string s;
map<char, char> z;

int main() {
    freopen("pre","r",stdin);
    freopen("out.txt","w",stdout);

    for (int i = 0; i < 3; ++i) {
        string a, b;
        getline(cin, a);
        getline(cin, b);
        for (int i = 0; i < a.size(); ++i)
            if (a[i] != ' ')
                z[a[i]] = b[i];
    }

    z['q'] = 'z';
    z['z'] = 'q';
    z[' '] = ' ';

    for (char i = 'a'; i <= 'z'; ++i)
        cerr << i << "->" << z[i] << endl;
    
    freopen("in.txt","r",stdin);

    int tests;
    cin >> tests;
    getline(cin, s);
    for (int testnum = 1; testnum <= tests; ++testnum) {
        getline(cin, s);
        string ans;
        ans = s;
        for (int i = 0; i < s.size(); ++i)
            ans[i] = z[s[i]];
        cout << "Case #" << testnum << ": " << ans << endl;
    }

    return 0;
}
