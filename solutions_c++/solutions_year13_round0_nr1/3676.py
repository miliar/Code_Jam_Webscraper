#include <iostream>
#include <fstream>
#include <string>

class TicTacToeTomek {
public:
    TicTacToeTomek(char b[4][5]);
    ~TicTacToeTomek();
    void check();
    std::string getresult();

private:
    void checkRow();
    void checkColumn();
    void checkMainDiag();
    void checkMinorDiag();

    char board[4][5];
    std::string xxxt,
           xxtx,
           xtxx,
           txxx,
           xxxx;
    std::string ooot,
           ooto,
           otoo,
           tooo,
           oooo;
    bool notCompleted;
//    std::ofstream f;
    std::string result;
};

TicTacToeTomek::TicTacToeTomek(char b[4][5])
{
    notCompleted = false;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
            board[i][j] = b[i][j];
            if (board[i][j] == '.')
                notCompleted = true;
        }
    }

    xxxt = "XXXT";
    xxtx = "XXTX";
    xtxx = "XTXX";
    txxx = "TXXX";
    xxxx = "XXXX";

    ooot = "OOOT";
    ooto = "OOTO";
    otoo = "OTOO";
    tooo = "TOOO";
    oooo = "OOOO";
}

TicTacToeTomek::~TicTacToeTomek()
{
}

void TicTacToeTomek::check()
{
    checkRow();
}

void TicTacToeTomek::checkRow()
{
    for(int i = 0; i < 4; i++) {
        std::string s = board[i];
        if (s == xxxt || s == xxtx || s == xtxx || s == txxx || s == xxxx) {
            result += "X won\n";
            return;
        }
        else if (s == ooot || s == ooto || s == otoo || s == tooo || s == oooo) {
            result += "O won\n";
            return;
        }
    }
    checkColumn();
}

void TicTacToeTomek::checkColumn()
{
    for(int i = 0; i < 4; i++) {
        std::string s;
        s += board[0][i];
        for (int j = 1; j < 4; j++) 
            s += board[j][i];

        if (s == xxxt || s == xxtx || s == xtxx || s == txxx || s == xxxx) {
            result += "X won\n";
            return;
        }
        else if (s == ooot || s == ooto || s == otoo || s == tooo || s == oooo) {
            result += "O won\n";
            return;
        }
    }
    checkMainDiag();
}

void TicTacToeTomek::checkMainDiag()
{
    std::string s;
    s += board[0][0];
    for (int j = 1; j < 4; j++) 
        s += board[j][j];

    if (s == xxxt || s == xxtx || s == xtxx || s == txxx || s == xxxx) {
        result += "X won\n";
        return;
    }
    else if (s == ooot || s == ooto || s == otoo || s == tooo || s == oooo) {
        result += "O won\n";
        return;
    }
    else {
        checkMinorDiag();
    }
}

void TicTacToeTomek::checkMinorDiag()
{
    std::string s;
    s += board[0][3];
    for (int j = 1; j < 4; j++) 
        s += board[j][3 - j];

    if (s == xxxt || s == xxtx || s == xtxx || s == txxx || s == xxxx) {
        result += "X won\n";
        return;
    }
    else if (s == ooot || s == ooto || s == otoo || s == tooo || s == oooo) {
        result += "O won\n";
        return;
    }
    else{
        if (notCompleted == true)
            result += "Game has not completed\n";
        else
            result += "Draw\n";
    }
}

std::string TicTacToeTomek::getresult()
{
    return result;
}

int main()
{
    //Pretreatment
    std::ifstream inf("A-large.in");
    std::ofstream f("result.out");

    if (!inf.is_open())
        std::cout << "Error when openning file!" << std::endl;

    if (!f.is_open())
        std::cout << "Error when openning file!" << std::endl;

    int T;
    inf >> T;
    int S = T;
    char tmp;
    inf.get(tmp);
    //Pretreatment

    while ( T > 0) {
        char buffer[4][5];
        int i = 0;
        while(i < 4) {
            inf.getline(buffer[i], 5);
            i++;
        }

        f << "Case #" << S + 1 - T << ": ";
        TicTacToeTomek t(buffer);
        t.check();
        f << t.getresult();
        T--;
        inf.get(tmp);
    }

    inf.close();
    f.close();

    return 0;
}
