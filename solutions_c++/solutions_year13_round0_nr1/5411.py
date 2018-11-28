#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

char b[4][4];

int process_line(char *b) {
    char cur = b[0];
    int draw = 0;
    for (int y = 1; y < 4; y++) {
        char c = b[y];
        if (c == '.')
            return -1;
        if (c == 'T') {
            if (y == 3)
                return cur;
            continue;
        }
        if (c != cur) {
            if (cur == 'T') {
                cur = c;
            }
            break;
        }
        if (y == 3)
            return cur;
    }
    return 0;
}

int process_board() {
    int result;
    int draw;
    for (int x = 0; x < 4; x++) {
        char line[4] = {b[x][0], b[x][1], b[x][2], b[x][3]};
        result = process_line(line);
        if (result == -1)
           draw = -1;
        if (result > 0)
           return result;
    }
    
    for (int x = 0; x < 4; x++) {
        char line[4] = {b[0][x], b[1][x], b[2][x], b[3][x]};
        result = process_line(line);
        if (result == -1)
           draw = -1;
        if (result > 0)
           return result;
    }
    
    char line1[4] = {b[0][0], b[1][1], b[2][2], b[3][3]};
    result = process_line(line1);
    if (result == -1)
        draw = -1;
    if (result > 0)
        return result;
    
    char line2[4] = {b[0][3], b[1][2], b[2][1], b[3][0]};
    result = process_line(line2);
    if (result == -1)
        draw = -1;
    if (result > 0)
        return result;
    
    if (draw < 0)
        return -1;
    return 0;
} 

int main(int argc, char *argv[])
{
    int count;
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output");
    fin >> count;
    for (int c = 0; c < count; c++) {
        for (int i = 0; i < 4; i++) {
            fin >> b[i][0] >> b[i][1] >> b[i][2] >> b[i][3];
            fin.get();
        }
        int result = process_board();
        switch (result) {
            case -1:
                 fout << "Case #"<<c+1<<": Game has not completed" << "\n";
                 break;
            case 0:
                 fout << "Case #"<<c+1<<": Draw" << "\n";
                 break;
            default:
                 fout << "Case #"<<c+1<<": "<<(char)result<<" won" << "\n";
        }
    }
    

    system("PAUSE");
    return EXIT_SUCCESS;
}
