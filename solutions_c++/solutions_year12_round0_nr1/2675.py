#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <functional>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iterator>
#include <memory>
#include <utility>

using namespace std;

char enc2dec[256];
char dec2enc[256];
int main() {
    const char* enc[] = {
        "a zoo q",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };
    const char* dec[] = {
        "y qee z",
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    };
    memset((void*)dec2enc, 0, sizeof(char)*256);
    memset((void*)enc2dec, 0, sizeof(char)*256);
    enc2dec[' '] = ' ';
    dec2enc[' '] = ' ';
    for (int i=0; i<4; ++i) {
        const int len = strlen(enc[i]);
        for (int j=0; j< len; ++j) {
            if (enc2dec[enc[i][j]] != dec[i][j]) {
                //cout << enc[i][j] << " => " << dec[i][j] << endl;
                enc2dec[enc[i][j]] = dec[i][j];
                //dec2enc[dec[i][j]] = enc[i][j];
            }
        }
    }

#if 0
    for (char c = 'a'; c<='z'; ++c) {
        cout << c << "=>" << enc2dec[c] << endl;
        cout << dec2enc[c] << "<=" << c << endl;
    }
#endif
    string line;
    getline(cin, line);
    const int T = atoi(line.c_str());
    for (int c=0; c<T; ++c) {
        getline(cin, line);
        cout << "Case #" << c+1 << ": ";
        for (string::iterator it = line.begin(); it != line.end(); ++it) {
            cout << enc2dec[*it];
        }
        cout << endl;
    }

}

