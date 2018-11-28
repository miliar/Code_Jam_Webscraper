#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <string>
using namespace std;

int main(void) {
    int t, ch, cnt = 1;
    string str1 = "abcdefghijklmnopqrstuvwxyz";
    string str2 = "yhesocvxduiglbkrztnwjpfmaq";
    //string str2 = "yhesocvxduiglbkrqtnwjpfmaz";
    string inp;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    ch = getc(stdin);
    while (t--) {
        inp = "";
        while (1) {
            ch = getc(stdin);
            if (ch == '\n') break;
            inp.push_back(ch);
        }

        cout << "Case #" << cnt << ": ";
        for (int j = 0; j < inp.size(); j++) {
            if (inp[j] == ' ')
                cout << " ";
            else
                cout << str2[inp[j] - 97];
        }
        cout << "\n";
        cnt++;
    }

    return 0;
}

