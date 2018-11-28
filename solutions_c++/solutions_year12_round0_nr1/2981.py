#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <cmath>
#include <set>
using namespace std;

string in[3] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string out[3] = {
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};

char tr[255];

int main()
{
    tr['q'] = 'z', tr['z'] = 'q';

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < in[i].size(); j++) tr[in[i][j]] = out[i][j];
    }

    int tests;
    char s[110], out[110];

    cin >> tests;

    cin.getline(s, 200);

    for (int test = 1; test <= tests; test++) {
        cin.getline(s, 200);
        int i;
        for (i = 0; s[i]; i++)
            if (s[i] == ' ') out[i] = ' ';
            else out[i] = tr[s[i]];

        out[i] = 0;

        cout << "Case #" << test << ": " << out << endl;
    }
}
