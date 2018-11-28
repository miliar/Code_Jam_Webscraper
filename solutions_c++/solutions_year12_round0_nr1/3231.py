#include <iostream>
#include <fstream>
using namespace std;

//                  "abcdefghijklmnopqrstuvwxyz"
//const char* map = "ynficwlbkuomxsevzpdrjgthaq";
  const char* map = "yhesocvxduiglbkrztnwjpfmaq";

int main () {

    //ifstream ifs ( "pA.txt" , ifstream::in );

    int lc = 1;
    int ntc = 0;
    cin >> ntc;
    cin.get();
    if (ntc > 0) cout << "Case #1: ";
    while (!cin.eof()) {
        char c = (char) cin.get();
        if ('a' <= c && c <= 'z') cout << map[c - 'a'];
        else if (c == ' ' || c == '\n') cout << c;
        if (c == '\n') {
            ++lc;
            if (lc <= ntc)
                cout << "Case #" << lc << ": ";
            else
                break;
        }
    }

    //ifs.close();

    return 0;
}
