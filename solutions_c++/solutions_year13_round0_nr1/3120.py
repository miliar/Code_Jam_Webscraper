#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

class FileReader : public ifstream {
public:
    FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
    int readInt() { int x = 0; *this >> x; return x; }
    vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
    string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
    string readString() { string x; *this >> x; return x; }
    vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
    __int64 readInt64() { __int64 x; *this >> x; return x; }
};

class FileWriter : public ofstream {
public:
    FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

__int64 gcd( __int64 a, __int64 b ) { return a ? gcd( b%a, a ) : b; }

int main() {
    FileReader fin( "A-large.in" );
    FileWriter fout( "out.txt" );

    int caseCount;
    fin >> caseCount;
    fin.readLine();
    for (int cc = 0; cc < caseCount; cc ++ ) {
        int winX = 0;
        int winO = 0;
        int emptySpace = 0;
        int mp [4][4];

        for (int i = 0; i < 4; i ++) {
            string tmp (fin.readLine());
            for (int j = 0; j < 4; j ++)
                if (tmp [j] == 'X') mp [i][j] = 1;
                else if (tmp [j] == 'O') mp [i][j] = 0;
                else if (tmp [j] == 'T') mp [i][j] = -10;
                else {
                    mp [i][j] = -100;
                    emptySpace ++;
                }
        }
        fin.readLine();

        int tmp = mp [0][0] * mp [1][1] * mp [2][2] * mp [3][3];
        if (tmp == 1 || tmp == -10) winX = 1;
        tmp = mp [0][0] + mp [1][1] + mp [2][2] + mp [3][3];
        if (tmp == 0 || tmp == -10) winO = 1;
        tmp = mp [3][0] * mp [2][1] * mp [1][2] * mp [0][3];
        if (tmp == 1 || tmp == -10) winX = 1;
        tmp = mp [3][0] + mp [2][1] + mp [1][2] + mp [0][3];
        if (tmp == 0 || tmp == -10) winO = 1;

        if (winX + winO == 0) for (int i = 0; i < 4; i ++) {
            tmp = mp [i][0] * mp [i][1] * mp [i][2] * mp [i][3];
            if (tmp == 1 || tmp == -10) {
                winX = 1;
                break;
            }
            tmp = mp [i][0] + mp [i][1] + mp [i][2] + mp [i][3];
            if (tmp == 0 || tmp == -10) {
                winO = 1;
                break;
            }
            tmp = mp [0][i] * mp [1][i] * mp [2][i] * mp [3][i];
            if (tmp == 1 || tmp == -10) {
                winX = 1;
                break;
            }
            tmp = mp [0][i] + mp [1][i] + mp [2][i] + mp [3][i];
            if (tmp == 0 || tmp == -10) {
                winO = 1;
                break;
            }
        }

        string status ("");
        if (winX == 1) status = "X won";
        else if (winO == 1) status = "O won";
        else if (emptySpace > 0) status = "Game has not completed";
        else status = "Draw";

        stringstream ss;
        ss << "Case #" << cc + 1 << ": " << status << endl;
        fout << ss.str().c_str();
        cout << ss.str().c_str();
    }
    return 0;
}
