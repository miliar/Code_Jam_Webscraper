#include <iostream>
#include <fstream>
using namespace std;

void mapping(char in[], char out[]) {
    char iStr1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char iStr2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char iStr3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

    char oStr1[] = "our language is impossible to understand";
    char oStr2[] = "there are twenty six factorial possibilities";
    char oStr3[] = "so it is okay if you want to just give up";

    int i, j;
    for (i = 0; i < 26; ++i)
        in[i] = 'a' + i;
    in[26]  = '\0';
    out[26] = '\0';

    for (i = 0; i < 26; ++i) {
        bool found = false;
        for (j = 0; j < strlen(iStr1); ++j) {
            if (iStr1[j] == in[i]) {
                out[i] = oStr1[j];
                found = true;
                break;
            }
        }
        if (found)
            continue;

        for (j = 0; j < strlen(iStr2); ++j) {
            if (iStr2[j] == in[i]) {
                out[i] = oStr2[j];
                found = true;
                break;
            }
        }
        if (found)
            continue;

        for (j = 0; j < strlen(iStr3); ++j) {
            if (iStr3[j] == in[i]) {
                out[i] = oStr3[j];
                found = true;
                break;
            }
        }
        if (found)
            continue;

        cout << "error, couldn't find mapping for char " << in[i] << "!\n";
    }

    out['q'-'a'] = 'z';
    out['z'-'a'] = 'q';
}

int main() {
    char in[27], out[27];
    mapping(in, out);

    const int SIZE = 1000;
    char buff[SIZE];

    fstream fin, fout;

    fin.open ("../data/problemA/A-small-attempt2.in", fstream::in);
    fout.open("../data/problemA/result.out", fstream::out);

    fin.getline(buff, SIZE);
    int lines = atoi(buff);

    int i = 1, j;
    while (!fin.eof()) {
        fin.getline(buff, SIZE);
        if (strlen(buff) < 1)
            break;

        fout << "Case #" << i << ": ";
        for (j = 0; buff[j] != '\0'; ++j) {
            if (buff[j] == ' ')
                fout << " ";
            else if (buff[j] >= 'a' && buff[j] <= 'z') {
                fout << out[buff[j] - 'a'];
            }
        }
        fout << "\n";

        ++i;
    }

    fin.close();
    fout.close();

    return 0;
}
