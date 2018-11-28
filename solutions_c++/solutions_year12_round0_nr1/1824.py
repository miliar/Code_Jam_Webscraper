/*
ID: dhxav
PROG: speaking_in_tongues
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define CONST 10000

int main() {
    ifstream fin ("A-small-attempt0.in");
    ofstream fout ("A-small-attempt0.out");

    int T;
    string buf;
    fin >> T;

    string googlerese = "yhesocvxduiglbkrztnwjpfmaq";
    getline(fin, buf);

    forn (i,T)
    {
        string G;
        getline(fin, G);

        fout << "Case #" << i+1 << ": ";
        forn (j, G.length())
        {
            if (G[j]==' ')
                fout << ' ';
            else
                fout << googlerese[G[j]-'a'];
        }
        fout << endl;
    }

}


