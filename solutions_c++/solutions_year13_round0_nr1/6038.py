#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define rep2(i,m,n) for(int i=(int)m;i<(int)n;i++)

using namespace std;

string solution() {
    string result = "Unknown";
    bool hasEmptyCell = false;
    char c;
    int posMatrix[4][4];
    rep(i,4) {
        rep(j,4) {
            scanf("%c", &c);
            if(c == '.') { hasEmptyCell = true; posMatrix[i][j] = 0; }
            if(c == 'X') posMatrix[i][j] = 1;
            if(c == 'O') posMatrix[i][j] = 2;
            if(c == 'T') posMatrix[i][j] = 3;
        }
        scanf("\n");
    }
    scanf("\n");
    
    int player, winner;
    winner = 0;
    rep(k,2) {
        rep(i,4) {
            if(winner != 0) continue;
            player = k+1;
            rep(j,4) {
                player &= posMatrix[i][j];
            }
            if(player == k+1) winner = player;
        }
        rep(j,4) {
            if(winner != 0) continue;
            player = k+1;
            rep(i,4) {
                player &= posMatrix[i][j];
            }
            if(player == k+1) winner = player;
        }
        rep(i,2) {
            if(winner != 0) continue;
            player = k+1;
            rep(j,4) {
                int l;
                if(i==0) l = 3-j; else l = j;
                player &= posMatrix[j][l];
            }
            if(player == k+1) winner = player;
        }
    }
    if(winner == 1) result = "X won";
    else if(winner == 2) result = "O won";
    else if(hasEmptyCell) result = "Game has not completed";
    else result = "Draw";
    
    return result;
}

int main() {
	int tc;
    scanf("%d\n", &tc);
    rep(i,tc) {
        printf("Case #%d: %s\n", i+1, solution().c_str());
    }
	return 0;
}