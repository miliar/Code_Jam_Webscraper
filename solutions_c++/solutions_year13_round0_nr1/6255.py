#include <fstream>
using namespace std;

int main() {
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("A-large.out");
    int N, blankCount = 0;
    char board[4][4];
    string input;
    bool done = false;
    in >> N;
    for(int i = 0; i < N; i++) {
            done = false;
            blankCount = 0;
            for(int j = 0; j < 4; j++) {
                    in >> input;
                    for(int k = 0; k < 4; k++) {
                            board[k][j] = input[k];
                            if(input[k] == '.')
                                        blankCount++;
                    }
            }
            for(int k = 0; k < 4; k++) {
                    //columns for x
                    if((board[0][k] == 'X' || board[0][k] == 'T') && 
                       (board[1][k] == 'X' || board[1][k] == 'T') && 
                       (board[2][k] == 'X' || board[2][k] == 'T') && 
                       (board[3][k] == 'X' || board[3][k] == 'T') && !done) {
                                   out << "Case #" << i + 1 << ": X won" << endl;
                                   done = true;}
                    //rows for x
                    else if((board[k][0] == 'X' || board[k][0] == 'T') &&
                       (board[k][1] == 'X' || board[k][1] == 'T') &&
                       (board[k][2] == 'X' || board[k][2] == 'T') &&
                       (board[k][3] == 'X' || board[k][3] == 'T') && !done){
                                   out << "Case #" << i + 1 << ": X won" << endl;
                                   done = true;}
                    //columns for o
                    else if((board[0][k] == 'O' || board[0][k] == 'T') &&
                       (board[1][k] == 'O' || board[1][k] == 'T') &&
                       (board[2][k] == 'O' || board[2][k] == 'T') &&
                       (board[3][k] == 'O' || board[3][k] == 'T') && !done){
                                   out << "Case #" << i + 1 << ": O won" << endl;
                                   done = true;}
                    //rows for o
                    else if((board[k][0] == 'O' || board[k][0] == 'T') &&
                       (board[k][1] == 'O' || board[k][1] == 'T') &&
                       (board[k][2] == 'O' || board[k][2] == 'T') &&
                       (board[k][3] == 'O' || board[k][3] == 'T') && !done){
                                   out << "Case #" << i + 1 << ": O won" << endl;
                                   done = true;}
            }
            if((board[0][0] == 'X' | board[0][0] == 'T') &
               (board[1][1] == 'X' | board[1][1] == 'T') &
               (board[2][2] == 'X' | board[2][2] == 'T') &
               (board[3][3] == 'X' | board[3][3] == 'T') && !done)
                           out << "Case #" << i + 1 << ": X won" << endl;
            else if((board[0][0] == 'O' || board[0][0] == 'T') &&
               (board[1][1] == 'O' || board[1][1] == 'T') &&
               (board[2][2] == 'O' || board[2][2] == 'T') &&
               (board[3][3] == 'O' || board[3][3] == 'T') && !done)
                           out << "Case #" << i + 1 << ": O won" << endl;
            else if((board[3][0] == 'X' || board[3][0] == 'T') &&
               (board[2][1] == 'X' || board[2][1] == 'T') &&
               (board[1][2] == 'X' || board[1][2] == 'T') &&
               (board[0][3] == 'X' || board[0][3] == 'T') && !done)
                           out << "Case #" << i + 1 << ": X won" << endl;
            else if((board[3][0] == 'O' || board[3][0] == 'T') &&
               (board[2][1] == 'O' || board[2][1] == 'T') &&
               (board[1][2] == 'O' || board[1][2] == 'T') &&
               (board[0][3] == 'O' || board[0][3] == 'T') && !done)
                           out << "Case #" << i + 1 << ": O won" << endl;
            else if(blankCount > 0 && !done) 
                 out << "Case #" << i + 1 << ": Game has not completed" << endl;
            else if(!done)
                out << "Case #" << i + 1 << ": Draw" << endl;
    }
}
