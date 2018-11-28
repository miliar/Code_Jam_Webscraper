#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>


//#define DEBUG

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main(){
	#ifndef DEBUG
		freopen("A-small-attempt6.in", "r", stdin);
		freopen("A-small.out", "w", stdout);
	#endif

    string board[4];
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        string answer = "Draw";
        int N;
        for (int i = 0; i < 4; i++) {
            cin >> board[i];
        }
        int dots = 0; 
        bool win = false;
        for (int i = 0; i < 4; i++){
            char start = board[i][0];
            if(start == 'T')
                start = board[i][1];

            char startv = board[0][i];
            if(startv == 'T')
                startv =  board[1][i];
            if(startv == '.' && start == '.'){
                dots++;
                continue;
            }
            win = true;
            for (int j = 0; j < 4 ; j++){
                if(board[i][j] == start || board[i][j] == 'T')
                    continue;
                else {
                    if(board[i][j] == '.')
                        dots ++;
                    win = false;
                    break;
                }
            }
            if (win && start != '.'){ 
                string winner = "  won";
                winner[0] = start;
                answer = winner;
                break;
            }

            win = true;
            for (int j = 0; j < 4 ; j++){
                if(board[j][i] == startv || board[j][i] == 'T')
                    continue;
                else{
                    win = false;
                    break;
                }
            }
            if (win && startv != '.'){ 
                string winner = "  won";
                winner[0] = startv;
                answer = winner;
                break;
            }
        }
        
        char d1 = board[0][0] == 'T' ? board[1][1] : board[0][0];
        char d2 = board[3][0] == 'T' ? board[2][1] : board[3][0];

        for(int i = 0; i < 4; i++){
            if (d1 != '.'){
                if (board[i][i] != 'T' && board[i][i] != d1)
                    d1 = '.';
            }
            if (d2 != '.'){
                if (board[3-i][i] != 'T' && board[3-i][i] != d2)
                    d2 = '.';
            }
        }
        if(d1 != '.'){
            string winner = "  won";
            winner[0] = d1;
            answer = winner;
            win = true;
        }
        else if(d2 != '.'){
            string winner = "  won";
            winner[0] = d2;
            answer = winner;
            win = true;
        }


        if(dots > 0 && !win)
            answer = "Game has not completed";

        cout << "Case #" << test+1 << ": ";//Output Answer:
        cout << answer << endl;
    }

	return 0;
}
