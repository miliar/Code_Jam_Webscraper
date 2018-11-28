#include <iostream>
#include <string>
#include <sstream>

using namespace std;

char sub[] = {
/*  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'  */
    'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
    };

int toInt(string s) {
    istringstream in(s);
    int n;
    in >> n;
    return n;
}

int main() {
    int T;
    string buf;
    getline(cin, buf);
    T = toInt(buf);
    for(int te = 1; te <= T; te++) {
        getline(cin, buf);
        cout << "Case #" << te << ": ";
        for(int i = 0; i < buf.size(); i++) {
            if(buf[i] != ' ') buf[i] = sub[buf[i]-'a'];
            cout << buf[i];
        }
        cout << endl;
    }
    return 0;
}
