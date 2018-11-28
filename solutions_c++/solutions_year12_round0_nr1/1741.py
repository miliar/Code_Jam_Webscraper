#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int main()
{
    string from = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string to = "our language is impossible to understand"
                "there are twenty six factorial possibilities"
                "so it is okay if you want to just give up";

    map<char,char> m;
    for ( size_t i = 0; i < from.size(); i++ ) {
        m[from[i]] = to[i];
    }
    m['q'] = 'z';
    m['z'] = 'q';

    int n;
    cin >> n;
    string s;
    getline( cin, s );
    for ( int i = 0; i < n; i++ ) {
        getline( cin, s );
        cout << "Case #" << i+1 << ": ";
        for ( size_t j = 0; j < s.size(); j++ ) {
            cout << m[s[j]];
        }
        cout << endl;
    }

    return 0;
}