#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>

#include <cmath>

using namespace std;

typedef map<char, char> Substitution;
Substitution s;

const string S1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi "
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";

const string S2 = "our language is impossible to understand "
    "there are twenty six factorial possibilities "
    "so it is okay if you want to just give up";

int main(int argc, char* argv[]) {
    for (int i = 0; i < S1.length(); ++i) {
        if (S1[i] != ' ') {
            s[S1[i]] = S2[i];
        }
    }

    s['z'] = 'q';
    s['q'] = 'z';

    int T = 0;
    cin >> T;
    cin.ignore(1);

    for (int test = 1; test <= T; ++test) {
        string str;
        getline(cin, str);

        for (int i = 0; i < str.length(); ++i)
            if (str[i] != ' ')
                str[i] = s[str[i]];
        
        cout << "Case #" << test << ": " << str << endl;
    }

    return 0;
}
