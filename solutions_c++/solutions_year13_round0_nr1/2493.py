#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;

int t;
string a[4];

char getWinner(string b) {
    bool tRaide = false;
    char now = 'T';
    int times = 0;

    for(int i = 0; i< 4; ++i) {
        if(b[i] == 'T')
            tRaide = true;
        else if(b[i] != '.') {
            if(now == 'T' || now == b[i]) {
                now = b[i];
                ++times;
            } else
                return 'T';

        } else
            return 'T';

    }

    if(times == 4 || (times == 3 && tRaide))
        return now;

    return 'T';
}

bool checkFOrEmpties() {
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(a[i][j] == '.')
                return true;

    return false;
}

char checkForWinner() {
    //HOrizontaliai

    for(int i = 0; i < 4; ++i) {
        char w = getWinner(a[i]);

        if(w != 'T')
            return w;

    }

    //Vertikaliai
    for(int i = 0; i < 4; ++i) {
        string toCheck = "";

        for(int j = 0; j < 4; ++j)
            toCheck += a[j][i];

        char w = getWinner(toCheck);

        if(w != 'T')
            return w;
    }

    //Istrizai 1
    string toCheck = "";
    for(int i = 0; i < 4; ++i) {
        toCheck += a[i][i];

        char w = getWinner(toCheck);

        if(w != 'T')
            return w;
    }

    //Istrizai 2

    toCheck = "";

    for(int i = 0; i < 4; ++i) {
        toCheck += a[i][3-i];

        char w = getWinner(toCheck);

        if(w != 'T')
            return w;
    }

    return 'T';
}

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("labas.txt", "w", stdout);

    cin >> t;

    for(int i = 0; i < t; ++i) {
        for(int j = 0; j < 4; ++j)
            cin >> a[j];

        char winner = checkForWinner();

        if(winner == 'O' || winner == 'X')
            printf("Case #%d: %c won\n", i+1, winner);
        else {
            if(!checkFOrEmpties())
                printf("Case #%d: Draw\n", i+1);
            else
                printf("Case #%d: Game has not completed\n", i+1);
        }
    }

    //fclose(stdin);
    //fclose(stdout);

}
