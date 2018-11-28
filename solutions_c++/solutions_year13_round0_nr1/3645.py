#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

bool xline(char *gbd)
{
    int xl = gbd[0] + gbd[1] + gbd[2] + gbd[3];
    return (xl == 4 * 'X' || xl == 3 * 'X' + 'T');
}

bool xcol(char *gbd)
{
    int xc = gbd[0] + gbd[4] + gbd[8] + gbd[12];
    return (xc == 4 * 'X' || xc == 3 * 'X' + 'T');
}

bool xx(char *gbd)
{
    int xxx = gbd[0] + gbd[5] + gbd[10] + gbd[15];
    if (xxx == 4 * 'X' || xxx == 3 * 'X' + 'T') return true;
    xxx = gbd[3] + gbd[6] + gbd[9] + gbd[12];
    return (xxx == 4 * 'X' || xxx == 3 * 'X' + 'T');
}

bool oline(char *gbd)
{
    int ol = gbd[0] + gbd[1] + gbd[2] + gbd[3];
    return (ol == 4 * 'O' || ol == 3 * 'O' + 'T');
}

bool ocol(char *gbd)
{
    int oc = gbd[0] + gbd[4] + gbd[8] + gbd[12];
    return (oc == 4 * 'O' || oc == 3 * 'O' + 'T');
}

bool ox(char *gbd)
{
    int oxx = gbd[0] + gbd[5] + gbd[10] + gbd[15];
    if (oxx == 4 * 'O' || oxx == 3 * 'O' + 'T') return true;
    oxx = gbd[3] + gbd[6] + gbd[9] + gbd[12];
    return (oxx == 4 * 'O' || oxx == 3 * 'O' + 'T');
}

bool notcomplete(char *gbd)
{
    for (int i = 0; i < 16; ++i) {
        if (gbd[i] == '.') return true;
    }
    return false;
}

int main()
{
    ifstream si;
    si.open("A-large.in", fstream::in);

    char ct[5] = { 0 };
    si >> ct;

    int t = 0;
    t = atoi(ct);
//    cout << t << endl;
    for (int i = 0; i < t; ++i) {
        char gbd[17] = { 0 };
        int c = 0;
        for (int j = 0; j < 5; ++j) {
            char line[5] = { 0 };
            si.getline(line, 5);
            strncat(gbd, line, 4);
//            cout << line << endl;
        }
        gbd[16] = '\0';
//        cout << gbd << endl;
        cout << "Case #" << i+1 << ": ";
        bool hasWinner = false;
        for (int k = 0; k < 4; ++k) {
            if (xline(gbd+4*k) || xcol(gbd+k) || xx(gbd)) {
                cout << "X won" << endl;
                hasWinner = true;
                break;
            }
            else if (oline(gbd+4*k) || ocol(gbd+k) || ox(gbd)) {
                cout << "O won" << endl;
                hasWinner = true;
                break;
            }
        }
        if (!hasWinner) {
            if (notcomplete(gbd)) {
                cout << "Game has not completed" << endl;
            }
            else {
                cout << "Draw" << endl;
            }
        }
    }
    si.close();

    return 0;
}

