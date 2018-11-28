#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

using namespace std;

bool is_win(vector<string> &board, int player)
{
    for(int y=0;y<4;y++){
        int x = -1;
        for(x=0;x<4;x++){
            if(!(board[y][x]==player || board[y][x]=='T')){
                break;
            }
        }
        if(x==4){
            return true;
        }
    }
    for(int x=0;x<4;x++){
        int y = -1;
        for(y=0;y<4;y++){
            if(!(board[y][x]==player || board[y][x]=='T')){
                break;
            }
        }
        if(y==4){
            return true;
        }
    }
    
    {
        int i = -1;
        for(i=0;i<4;i++){
            if(!(board[i][i]==player || board[i][i]=='T')){
                break;
            }
        }
        if(i==4){
            return true;
        }
    }
    {
        int i = -1;
        for(i=0;i<4;i++){
            if(!(board[3-i][i]==player || board[3-i][i]=='T')){
                break;
            }
        }
        if(i==4){
            return true;
        }
    }

    
    return false;
}
bool is_game_not_end(vector<string> &board)
{
    for(int y=0;y<4;y++){
        for(int x=0;x<4;x++){
            if(board[y][x]=='.'){
                return true;
            }
        }
    }
    return false;
}
void print_board(vector<string> &board)
{
    cout << "===board===" << endl;
    for(int y=0;y<4;y++){
        cout << board[y] <<endl;
    }
}
void testcase(int t)
{
	string result_str = "OK";
    vector<string> board;
    for(int y=0;y<4;y++){
        string line;
        cin >> line;
        cin.ignore();
        board.push_back(line);
    }
    cin.ignore(1000,'\n');

    // print_board(board);
    if(is_win(board, 'X')){
        result_str = "X won";
    }else if(is_win(board, 'O')){
        result_str = "O won";
    }else if(is_game_not_end(board)){
        result_str = "Game has not completed";
    }else{
        result_str = "Draw";
    }
    
	cout << "Case #" << (t+1) << ": " << result_str << endl;
}

int main(int argc, char *argv[]) {
	int T;
    if(argc >= 2){
        int fd = open(argv[1], O_RDONLY);
        if(fd == -1){
            fprintf(stderr, "failed to open [%s]\n", argv[1]);
            exit(1);
        }
        int ret = dup2(fd, 0);
        if(ret == -1){
            fprintf(stderr, "failed to dup2[%s]\n", argv[1]);
            exit(1);
        }
    }
	cin >> T;
	for(int t=0;t<T;t++){
		testcase(t);
	}
	return 0;
}

