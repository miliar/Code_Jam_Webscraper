#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();
    for (int c=0; c<n; ++c) {
        string line[4];
        for (int i=0; i<4; ++i) {
            getline(cin, line[i]);
        }
        cin.ignore();
        bool xwin = false;
        bool owin = false;
        int xcount;
        int ocount;
        for (int i=0; i<4; ++i) {
            xcount = 0;
            ocount = 0;
            for (int j=0; j<4; ++j) {
                switch (line[i][j]) {
                    case 'T':
                        ++xcount;
                        ++ocount;
                        break;
                    case 'O':
                        ++ocount;
                        break;
                    case 'X':
                        ++xcount;
                        break;
                    default:
                        break;
                }
            }
            if (xcount == 4) xwin = true;
            if (ocount == 4) owin = true;
        }


        for (int i=0; i<4; ++i) {
            xcount = 0;
            ocount = 0;
            for (int j=0; j<4; ++j) {
                switch (line[j][i]) {
                    case 'T':
                        ++xcount;
                        ++ocount;
                        break;
                    case 'O':
                        ++ocount;
                        break;
                    case 'X':
                        ++xcount;
                        break;
                    default:
                        break;
                }
            }
            if (xcount == 4) xwin = true;
            if (ocount == 4) owin = true;
        }
        
        xcount = 0;
        ocount = 0;
        for (int j=0; j<4; ++j) {
            switch (line[j][j]) {
                case 'T':
                    ++xcount;
                    ++ocount;
                    break;
                case 'O':
                    ++ocount;
                    break;
                case 'X':
                    ++xcount;
                    break;
                default:
                    break;
            }
        }
        if (xcount == 4) xwin = true;
        if (ocount == 4) owin = true;

        xcount = 0;
        ocount = 0;
        for (int j=0; j<4; ++j) {
            switch (line[j][3-j]) {
                case 'T':
                    ++xcount;
                    ++ocount;
                    break;
                case 'O':
                    ++ocount;
                    break;
                case 'X':
                    ++xcount;
                    break;
                default:
                    break;
            }
        }
        if (xcount == 4) xwin = true;
        if (ocount == 4) owin = true;

        cout << "Case #" << c + 1 << ": ";;
        if (xwin && owin) {
draww:
            cout << "Draw" << endl;
        } else if (xwin) {
            cout << "X won" << endl;
        } else if (owin) {
            cout << "O won" << endl;
        } else {
            for (int i=0; i<4; ++i) {
                for (int j=0; j<4; ++j) {
                    if (line[i][j] == '.') goto yet;
                }
            }
            goto draww;
yet:
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}
