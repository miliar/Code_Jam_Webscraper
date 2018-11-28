#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;

int T;

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char map[255];

int main() {
    memset(map, 'A', sizeof(map));
    for (int i = 0; i < a.size(); ++i) {
        map[ a[i] ] = b[i];
    }
    map['z'] = 'q';
    map['q'] = 'z';
    map[' '] = ' ';

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    cin >> T; cin.ignore();
    char txt[111];
    for (int nT = 1; nT <= T; ++nT) {
        gets(txt);
        
        printf("Case #%d: ", nT);
        
        for (int i = 0; txt[i]; ++i)
            cout << map[ txt[i] ];
        cout << endl;
    }
    
    return 0;
}
