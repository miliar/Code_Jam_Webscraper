#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;
char check(int count[]) {
//    printf("x:%d O: %d\n", count['X'], count['O']);
    
    if (count['X'] == 4 || (count['X'] == 3 && count['T'] == 1)) {
        return 'X';
    }

    if (count['O'] == 4 || (count['O'] == 3 && count['T'] == 1)) {
        return 'O';
    }
    
    return ' ';
}

void reset(int count[]){
            count['O'] = 0;
        count['X'] = 0;
        count['T'] = 0;
        count['.'] = 0;
}
int main(int argc, char** argv) {
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++) {
        char board[10][10];
        for(int r=1;r<=4; r++){
            scanf("%s", board[r]+ 1);
        }
        char empty[200];
//        scanf("%s", empty);
//        for(int r=1;r<=4; r++){
//            printf("%s\n", board[r] + 1);
//        }
        
        int free=0, x, o, t;
        int count[200];
        cout << "Case #" << i << ": ";
        reset(count);
        
        char win;
        for(int r=1; r<=4; r++){
            for(int c=1; c<=4; c++){
//                printf("adding count : %c\n", board[r][c]);
                count[board[r][c]] ++;
            }
            win = check(count);
            free +=count['.'];
            
            if(win != ' '){
                cout << win << " won" << endl;
                break;
            }
            reset(count);
        }
        
        for(int c=1; c<=4 && win == ' '; c++){
            for(int r=1; r<=4; r++){
                count[board[r][c]] ++;
            }
            win = check(count);
            
            if(win != ' '){
                cout << win << " won" << endl;
                break;
            }
            reset(count);
        }
        
        if(win == ' ') {
            for (int r = 1; r <= 4; r++) {
                count[board[r][r]]++;
            }
            win = check(count);

            if (win != ' ') {
                cout << win << " won" << endl;
            }
            reset(count);
            
        }

        if (win == ' ') {
            for(int r=1; r<=4 && win == ' '; r++) {
                count[board[r][5-r]] ++;

            }
            win = check(count);

            if (win != ' ') {
                cout << win << " won" << endl;
            }
            reset(count);
        }
        if(win == ' '){
            if(free >0){
//                cout << "free " << free<<endl;
                cout << "Game has not completed"<<endl;
            }else{
                cout << "Draw"<<endl;
            }
        }
    }
    return 0;
}

