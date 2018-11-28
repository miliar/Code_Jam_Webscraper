#include <iostream>
#include <string>
using namespace std;

string xWins[]={"XXXX", "TXXX", "XTXX", "XXTX", "XXXT"};
string oWins[]={"OOOO", "TOOO", "OTOO", "OOTO", "OOOT"};
bool isWon(string row, char p){
    bool res = false;
    if (p == 'X'){
        for (int i=0;i<5;i++){
            if (row.find(xWins[i])!=string::npos){
                res = true;
                break;
            }
        }
    }
    else {
        for (int i=0;i<5;i++){
            if (row.find(oWins[i])!=string::npos){
                res = true;
                break;
            }
        }
    }

    return res;
}

std::string solve(){
    const int sz = 4;
    string rows[sz];
    string columns[sz];
    for (int i=0;i<sz;i++){
        cin >> rows[i];
        for (int j=0;j<sz;j++)
            columns[j].append(rows[i].begin()+j, rows[i].begin()+j+1);
    }
    string result = "Uknown";
    bool xWon = false, oWon = false, completed=true;
    //Check rows

    for (int i=0;i<sz;i++){
        if (!xWon)
            xWon = isWon(rows[i], 'X');
        if (!oWon)
            oWon = isWon(rows[i], 'O');
        if (rows[i].find(".") != string::npos){
            completed = false;
        }
    }
    //Check columns
    for (int i=0;i<sz;i++){
        if (!xWon)
            xWon = isWon(columns[i], 'X');
        if (!oWon)
            oWon = isWon(columns[i], 'O');
    }
    //Check diagonals
    string diagonals[2];
    for (int i=0;i<sz;i++){
            diagonals[0].append(rows[i].begin()+i, rows[i].begin()+i+1);
            diagonals[1].append(rows[i].begin()+sz-i-1, rows[i].begin()+sz-i);
    }
    if (!xWon)
        xWon = isWon(diagonals[0], 'X');
    if (!oWon)
        oWon = isWon(diagonals[0], 'O');
    if (!xWon)
        xWon = isWon(diagonals[1], 'X');
    if (!oWon)
        oWon = isWon(diagonals[1], 'O');
    if (xWon && oWon)
        result = "Draw";
    else
        if (!xWon && !oWon && completed)
            result = "Draw";
        else
            if (!xWon && !oWon && !completed)
                result = "Game has not completed";
            else
                if (xWon)
                    result = "X won";
                else
                    if (oWon)
                        result = "O won";
                    else
                        result = "Uknown";
    return result;
}

int main(int argc, char *argv[])
{
    int n;
    cin >> n;
    for (int i=1; i<=n;i++){
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
