#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int abs(int n) {
    if (n > 0) return n;
    else return -n;
}

int main() {
    int tests;
    cin >> tests;

    for (int cn = 1; cn <= tests; cn++) {
        char c;
        int cc, d, n;
        string t;
        map<string, char> compound;
        map<string, bool> destroy;
        map<char, int> inListCount;
        string list = "";
        cin >> cc;
        for (int i = 0; i < cc; i++) {
            cin >> t;
            compound[t.substr(0, 2)] = t[2];
            string tr = "";
            tr += t[1];
            tr += t[0];
            compound[tr] = t[2];
        }
        cin >> d;
        for (int i = 0; i < d; i++) {
            cin >> t;
            destroy[t] = true;
            string tr = "";
            tr += t[1];
            tr += t[0];
            destroy[tr] = true;
        }        
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> c;
            list += c;
            inListCount[c] = inListCount[c] + 1;
            if (list.length() == 1) continue;
            if (compound[list.substr(list.length() - 2, 2)] != 0) {
                char newComp = compound[list.substr(list.length() - 2, 2)];
                inListCount[list[list.length() - 2]] = inListCount[list[list.length() - 2]] - 1;
                inListCount[list[list.length() - 1]] = inListCount[list[list.length() - 1]] - 1;
                inListCount[newComp] = inListCount[newComp] + 1;
                list = list.substr(0, list.length() - 2) + newComp;
            } else {
                for (char j = 'A'; j <= 'Z'; j++) {
                    if (inListCount[j] == 0 || (inListCount[j] == 1 && j == c))
                        continue;
                    string d = "";
                    d += j;
                    d += c;
                    if (destroy[d]) {
                        list = "";
                        inListCount.clear();
                    }
                }
            }
//            cout << list << endl;
        }

        cout << "Case #" << cn << ": [";
        if (list.length() > 0) 
            cout << list[0];
        for (int i = 1; i < list.length(); i++) 
            cout << ", " << list[i];
        cout << "]" << endl;
    }
}