#include<iostream>
#include<fstream>
using namespace std;
const int MAX_T = 1000;

int status[1001];

typedef string strM[4];

bool compue_if_won(const strM &str, char sym) {
    int stat = 0;
// X horizontal laimejo
    for(int a = 0; a <= 3; a++) {
        stat = 1;
        for(int b = 0; b <= 3; b++)
            if ((str[a][b] != sym)&&(str[a][b] != 'T')) {
                stat = 0;
                break;
            }
        if (stat != 0)
            return true;
    }

    // X vertical laimejo
    for(int a = 0; a <= 3; a++) {
        stat = 1;
        for(int b = 0; b <= 3; b++)
            if ((str[b][a] != sym)&&(str[b][a] != 'T')) {
                stat = 0;
                break;
            }
        if (stat != 0)
            return true;
    }

    // X diagonal1 laimejo
    stat = 1;
    for(int a = 0, b = 0; a <= 3; a++) {
        if ((str[b][a] != sym)&&(str[b][a] != 'T')) {
            stat = 0;
            break;
        }
        b++;
    }
    if (stat != 0)
        return true;

    // X diagonal2 laimejo
    stat = 1;
    for(int a = 3, b = 0; b <= 3; b++) {
        if ((str[a][b] != sym)&&(str[a][b] != 'T')) {
            stat = 0;
            break;
        }
        a--;
    }
    return (stat == 1);
}

int compute_test_case(const strM &str) {
    bool filled = false;
    // ar filled
    for(int a = 0; a <= 3; a++) {
        for(int b = 0; b <= 3; b++)
            if (str[a][b] == '.') {
                filled = true;
                break;
            }
        if (filled)
            break;
    }
    if (compue_if_won(str, 'X'))
        return 1;
    if (compue_if_won(str, 'O'))
        return -1;
    if (filled)
        return 2;
    else
        return 0;
}

int compute(char *txt, char *txt2) {
	ifstream fin(txt);
	ofstream fout(txt2);
	int status;

    int count;
    int stat = 0;
    bool filled = false;

    fin >> count;
    strM str;
    for(int i = 1; i <= count; i++) {
        fin >>str[0] >> str[1] >> str[2] >> str[3];
        int stat = compute_test_case(str);
        fout << "Case #" << i << ": ";
        if (stat == 0)
           fout << "Draw" << endl;
        else if (stat == 1)
           fout << "X won" << endl;
        else if (stat == -1)
           fout << "O won" << endl;
        else // (stat == 2)
           fout << "Game has not completed" << endl;
    }


    fout.close();
	fin.close();
}

int main(int argc, char* argv[]) {
	compute((char*)("input.txt"), (char*)("output.txt"));
	return 0;
}
