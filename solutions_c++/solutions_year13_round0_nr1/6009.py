#include <iostream>
#include <stdint.h>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{

    ifstream sourceFile("./files/A-large.in");
    ofstream output("./files/output.txt");

    if (sourceFile.is_open()) {

        int T;
        sourceFile >> T;
        for(int i = 0; i < T; i++) {
            char** ch = new char*[4];
            for(int j = 0; j < 4; j++) {
                ch[j] = new char[4];
                for(int k = 0; k < 4; k++) {
                    sourceFile >> ch[j][k];
                }
            }

            int O_won_hor = 0, O_won_vert = 0, X_won_hor = 0, X_won_vert = 0;

            bool got_result = false;
            bool finished = true;

            for(int j = 0; j < 4 && !got_result; j++) {
                for(int k = 0; k < 4; k++) {
                    if(ch[j][k] == 'O') {
                        O_won_hor++;
                    }
                    else if(ch[j][k] == 'X') {
                        X_won_hor++;
                    }
                    else if(ch[j][k] == 'T') {
                        O_won_hor++;
                        X_won_hor++;
                    }
                    else if(ch[j][k] == '.') {
                        finished = false;
                    }

                    if(ch[k][j] == 'O') {
                        O_won_vert++;
                    }
                    else if(ch[k][j] == 'X') {
                        X_won_vert++;
                    }
                    else if(ch[k][j] == 'T') {
                        O_won_vert++;
                        X_won_vert++;
                    }
                    else if(ch[k][j] == '.') {
                        finished = false;
                    }

                }

                if(O_won_hor == 4 || O_won_vert == 4) {
                    got_result = true;
                    output << "Case #" << i + 1 << ": O won" << endl;
                }
                else if (X_won_hor == 4 || X_won_vert == 4) {
                    got_result = true;
                    output << "Case #" << i + 1 << ": X won" << endl;
                }
                else {
                X_won_hor = 0;
                X_won_vert = 0;
                O_won_hor = 0;
                O_won_vert = 0;
                }
            }

            if(!got_result) {
                if(((ch[0][0] == 'O' || ch[0][0] == 'T') && (ch[1][1] == 'O' || ch[1][1] == 'T') && (ch[2][2] == 'O' || ch[2][2] == 'T') && (ch[3][3] == 'O'|| ch[3][3] == 'T'))
                   || ((ch[0][3] == 'O'|| ch[0][3] == 'T') && (ch[1][2] == 'O' || ch[1][2] == 'T') && (ch[2][1] == 'O' || ch[2][1] == 'T') && (ch[3][0] == 'O'|| ch[3][0] == 'T'))) {
                    got_result = true;
                    output << "Case #" << i + 1 << ": O won" << endl;
                }
                else if(((ch[0][0] == 'X'|| ch[0][0] == 'T') && (ch[1][1] == 'X'|| ch[1][1] == 'T') && (ch[2][2] == 'X'|| ch[2][2] == 'T') && (ch[3][3] == 'X'|| ch[3][3] == 'T'))
                   || ((ch[0][3] == 'X'|| ch[0][3] == 'T') && (ch[1][2] == 'X'|| ch[1][2] == 'T') && (ch[2][1] == 'X'|| ch[2][1] == 'T') && (ch[3][0] == 'X'|| ch[3][0] == 'T'))) {
                    got_result = true;
                    output << "Case #" << i + 1 << ": X won" << endl;
                }
            }

            if(!got_result) {
                if(finished) {
                    output << "Case #" << i + 1 << ": Draw" << endl;
                }
                else {
                    output << "Case #" << i + 1 << ": Game has not completed" << endl;
                }
            }

            delete ch;

        }
        sourceFile.close();
        output.close();
    }

    return 0;
}
