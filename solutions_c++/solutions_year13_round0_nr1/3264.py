#include <iostream>
#include <fstream>

using namespace std;


char check(char table[4], bool &tablefull) //Check one line or row
{
    char winner = table[0]; //Peek the first char
    if (winner == 'T') {
        //Peek even next char, then just go on.
        winner = table[1];
    }

    if (winner == '.') {
        tablefull = false;
        return '.'; //No winner in this line.
    }

    for ( int y = 1 ; y < 4 ; y++ ) {
        if (table[y] == '.') tablefull = false;
        if (winner != table[y] && table[y] != 'T') { //Next char was different from prev.
            return '.';
        }
    }

    return winner; 
}

char checkTable(char table[4][4])
{
    bool tablefull = true;
    //Checking lines first.
    for ( int x = 0 ; x < 4; x++ ) { //Lines
        char res = check(table[x], tablefull);
        if (res == '.') continue;
        cout << "winner: " << res << " in line: " << x+1 << endl;
        return res; //Here we got a winner.
    }

    //Checking rows now.
    
    for (int y = 0 ; y < 4; y++ ) { //rows, cols whatever
        //Generate a row in an array... :)
        char row[4];
        for ( int z = 0; z < 4 ; z++ ) {
            row[z] = table[z][y];
        }

        char res = check(row, tablefull); //tablefull is not necessary here, but we don't care now.
        if (res == '.') continue;
        cout << "winner: " << res << " in row: " << y+1 << endl;
        return res;
    }

    //Check diagonals.
    //Generate it into the usual array :P
    char diag[4];
    for ( int x = 0; x < 4; x++ ) {
        diag[x] = table[x][x];
    }   
    
    char res = check(diag, tablefull);
    if (res != '.') {
        cout << "winner in diag, \\ " << res << endl;
        return res;
    }

    for ( int x = 0; x < 4; x++ ) {
        diag[x] = table[3-x][x];
    }

    res = check(diag, tablefull);
    cout << "Diag: "<< diag[0] << diag[1] << diag[2] << diag[3] << endl;
    if (res != '.') {
        cout << "winner in diag, / " << res << endl;
        return res;
    }


    if (tablefull) { 
        cout << "Draw." << endl;
        return 'D';
    }
    
    cout << "No winner, game goes on." << endl;
    return '.';
}

int main(void)
{
    char table[4][4] = {'.'}; //Just to start with an empty table

    ifstream inp("A-large.in", ifstream::in); //No errorhandling no one cares, sorry I'm in hurry. :)
    ofstream out("test.out", ofstream::out);

    int tcs;

    inp >> tcs;


    for ( int cs = 0; cs < tcs; cs++ ) {
        cout << endl << endl << "===========================" << endl;
        cout << "CASE #" << cs+1 <<endl;
        //Read for lines, each consists 4 chars...
        for ( int x = 0 ; x < 4 ; x++ ) {
            for ( int y = 0; y < 4; y++ ) {
                inp >> table[x][y];
            }
        }

        //Print table, just for debugging.
        for ( int x = 0; x < 4 ; x++) {
            for (int y = 0 ; y < 4; y++ ) {
                cout << table[x][y];
            }
            cout << endl;
        }
    

        //Table readed up. Eval.

        out << "Case #" << cs+1 << ": ";
        switch (checkTable(table)) {
            case 'X':
                out << "X won" << endl;
                break;
            case 'O':
                out << "O won" << endl;
                break;
            case '.':
                out << "Game has not completed" << endl;
                break;
            case 'D':
                out << "Draw" << endl;
                break;
        }
    }
    return 0;

}
