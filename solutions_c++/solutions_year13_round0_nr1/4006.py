#include <iostream>

using namespace std;

char mygrid[4][4];

char diagright(void){
    int xcount = 0, ocount = 0;
    for (int i = 0; i < 4; ++i){
        if (mygrid[3 - i][i] == 'X'){
            xcount += 1;
        }
        else if (mygrid[3 - i][i] == 'O'){
            ocount += 1;
        }
        else if (mygrid[3 - i][i] == 'T'){
            ocount += 1;
            xcount += 1;
        };
    };
    if (xcount == 4){
        return 'X';
    }
    else if (ocount == 4){
        return 'O';
    }
    else {
        return 'N';
    };
}

char diagleft(void){
    int xcount = 0, ocount = 0;
    for (int i = 0; i < 4; ++i){
        if (mygrid[i][i] == 'X'){
            xcount += 1;
        }
        else if (mygrid[i][i] == 'O'){
            ocount += 1;
        }
        else if (mygrid[i][i] == 'T'){
            ocount += 1;
            xcount += 1;
        };
    };
    if (xcount == 4){
        return 'X';
    }
    else if (ocount == 4){
        return 'O';
    }
    else {
        return 'N';
    };
}

char rowcheck(int row){
    int xcount = 0, ocount = 0;
    for (int i = 0; i < 4; ++i){
        if (mygrid[row][i] == 'X'){
            xcount += 1;
        }
        else if (mygrid[row][i] == 'O'){
            ocount += 1;
        }
        else if (mygrid[row][i] == 'T'){
            ocount += 1;
            xcount += 1;
        };
    };

    if (ocount == 4){
        return 'O';
    }
    else if (xcount == 4){
        return 'X';
    }
    else {
        return 'N';
    };
}

char colcheck(int col){
    int xcount = 0, ocount = 0;
    for (int i = 0; i < 4; ++i){
        if (mygrid[i][col] == 'X'){
            xcount += 1;
        }
        else if (mygrid[i][col] == 'O'){
            ocount += 1;
        }
        else if (mygrid[i][col] == 'T'){
            ocount += 1;
            xcount += 1;
        };
    };

    if (ocount == 4){
        return 'O';
    }
    else if (xcount == 4){
        return 'X';
    }
    else {
        return 'N';
    };
}

int main()
{
    int n;
    cin >> n;

    string tmp;


/*
    for (int i = 0; i < 4; ++i){
        for (int j = 0; j < 4; ++j){
            cout << i << " " << j << " " << mygrid[i][j] << endl;
        };
    };
*/

    char myans[n];


    for (int i = 0; i < n; ++i){
        for (int j = 0; j < 4; ++j){
            cin >> tmp;
            for (int k = 0; k < 4; ++k){
                mygrid[j][k] = tmp[k];
            };
        };
        if (diagleft() != 'N'){
            myans[i] = diagleft();
            continue;
        };
        if (diagright() != 'N'){
            myans[i] = diagright();
            continue;
        };
        for (int j = 0; j < 4; ++j){
            if (rowcheck(j) != 'N'){
                myans[i] = rowcheck(j);
                goto here;
            };
            if (colcheck(j) != 'N'){
                myans[i] = colcheck(j);
                goto here;
            };
        };
        for (int j = 0; j < 4; ++j){
            for (int k = 0; k < 4; ++k){
                if (mygrid[j][k] == '.'){
                    myans[i] = 'N';
                    goto here;
                };
            };
        };
        myans[i] = 'D';
        here:;
    }

    for (int i = 0; i < n; ++i){
        cout << "Case #" << i + 1 << ": ";
        if (myans[i] == 'X'){
            cout << "X won";
        }
        else if (myans[i] == 'O'){
            cout << "O won";
        }
        else if (myans[i] == 'D'){
            cout << "Draw";
        }
        else {
            cout << "Game has not completed";
        };
        cout << endl;
    };


    return 0;
}
