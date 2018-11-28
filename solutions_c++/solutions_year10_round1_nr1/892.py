#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dx[4] = {1, 0, -1, 1};
int dy[4] = {0, 1, 1, 1};
vector<string> board;
vector<string> rB;
int N;
int check(int x, int y, int k){
    if( x >= N || x < 0 || y < 0 || y >= N) return 0;
    else if(x+dx[k] >= N || x + dx[k] < 0 || y+dy[k] >= N || y + dy[k] < 0) return 1;
    else if(rB[x+dx[k]][y+dy[k]] != rB[x][y]) return 1;
    else return 1 + check(x+dx[k], y+dy[k], k);
}

int main()
{
    int T;
    cin >> T;
    for(int c = 1; c <= T; ++c){
        int K;
        cin >> N >> K;
        board = vector<string>(N);
        rB = vector<string>(N);
        for(int i = 0; i < N; ++i) {
            cin >> board[i];
            rB[i] = board[i];
        }
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < N; ++j){
                board[j][N-i-1] = rB[i][j];
            }
        }
        for(int i = 0; i < N; ++i) {
            rB[i] = board[i];
        }
        for(int i = 0; i < N; ++i){
            int totalC = 0;
            for(int j = N-1; j >= 0; --j){
                if(board[j][i] == '.'){
                    int c = 1;

                    while(j-c >= 0 && board[j-c][i] == '.')c++;
                    for(int k = j+totalC; k > 0; --k){
                        if(k < N && k-c-totalC >= 0){
                            rB[k][i] = board[k-c-totalC][i];
                        }
                        else rB[k][i] = '.';
                    }
                    totalC += c;
                    rB[0][i] = '.';
                    j -= (c-1);
                }
            }
        }
        int red = 0, blue = 0;
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < N; ++j){
                switch(rB[i][j]){
                    case '.': break;
                    case 'B': {
                        for(int k = 0; k < 4; ++k){
                            blue  = max(blue, check(i, j, k));
                        }
                        break;
                    }
                    case 'R': {
                        for(int k = 0; k < 4; ++k){
                            red  = max(red, check(i, j, k));
                        }
                        break;
                    }
                }
            }
        }
        if(red >= K && blue >= K){
            cout << "Case #" << c << ": Both" << endl;
        }
        else if( red >= K) cout << "Case #" << c << ": Red" << endl;
        else if( blue >= K) cout << "Case #" << c << ": Blue" << endl;
        else cout << "Case #" << c << ": Neither" << endl;



    }
	return 0;
}
