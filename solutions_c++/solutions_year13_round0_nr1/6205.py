#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <limits>
#include <iomanip>

#define all(c) (c).begin(),(c).end()

using namespace std;

typedef long long llong;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int caseNum=1;
ifstream fin("A.in");
ofstream fout("A.out");

#define gout fout << "Case #" << caseNum++ << ": ", fout

int main (int argc, char* argv[]) {
    int T;
    fin >> T;

    while (T--) {
        bool xC=false,oC=false;
        bool allFilled=true;
        string s;
        getline(fin, s);
        char map[4][4];
        for (int i=0; i<4; i++) {
            getline(fin, s);
            for (int j=0; j<4; j++) {
                map[i][j] = s[j];
                if (map[i][j] == '.')
                    allFilled = false;
            }
        }
        for (int y=0; y<4; y++) {
            bool X=true,O=true;
            for (int x=0; x<4; x++) {
                char c = map[x][y];
                if (!(c == 'O' || c == 'T'))
                    O = false;
                if (!(c == 'X' || c == 'T'))
                    X = false;
            }
            if (X)
                xC = true;
            if (O)
                oC = true;
            X=true; O=true;
            for (int x=0; x<4; x++) {
                char c = map[y][x];
                if (!(c == 'O' || c == 'T'))
                    O = false;
                if (!(c == 'X' || c == 'T'))
                    X = false;
            }
            if (X)
                xC = true;
            if (O)
                oC = true;
        }
        bool X=true,O=true;
        for (int i=0; i<4; i++) {
            char c = map[i][i];
            if (!(c == 'O' || c == 'T'))
                O = false;
            if (!(c == 'X' || c == 'T'))
                X = false;
        }
        if (O)
            oC = true;
        if (X)
            xC = true;
        X=true;O=true;
        for (int i=0; i<4; i++) {
            char c = map[3-i][i];
            if (!(c == 'O' || c == 'T'))
                O = false;
            if (!(c == 'X' || c == 'T'))
                X = false;
        }
        if (O)
            oC = true;
        if (X)
            xC = true;

        if (oC)
            gout << "O won\n";
        else if (xC)
            gout << "X won\n";
        else if (allFilled)
            gout << "Draw\n";
        else
            gout << "Game has not completed\n";
    }

    fin.close();
    fout.close();
    return 0;
}
