#include <iostream>
using namespace std;

const int MAXN = 51;
int board[MAXN][MAXN];
int T, N, K;

int checkforwin(int color) {
  int curcount;
  for(int i = 0; i < N; i++) {
    curcount = 0;
    for(int j = 0; j < N; j++) {
      if(board[i][j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }
  
  for(int j = 0; j < N; j++) {
    curcount = 0;
    for(int i = 0; i < N; i++) {
      if(board[i][j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }
  
  for(int i = 0; i < N; i++) {
    curcount = 0;
    for(int j = 0; i+j < N; j++) {
      if(board[i+j][j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }
  for(int j = 1; j < N; j++) {
    curcount = 0;
    for(int i = 0; i+j < N; i++) {
      if(board[i][i+j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }

  for(int i = 0; i < N; i++) {
    curcount = 0;
    for(int j = 0; i-j >= 0; j++) {
      if(board[i-j][j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }
  for(int i = 0; i < N; i++) {
    curcount = 0;
    for(int j = N-1; i+N-1-j < N; j--) {
      if(board[i+N-1-j][j] == color) {
        curcount++;
        if(curcount >= K) return true;
      } else {
        curcount = 0;
      }
    }    
  }

  return false;
}

int main(int argc, char *argv[]) {
  char ch;
  int startj;
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    cin >> N >> K >> ws;
    for(int i=0; i<N; i++) {
      for(int j=0; j<N; j++) {
        cin >> ch;
        switch(ch) {
          case '.': board[i][j] = 0; break;
          case 'R': board[i][j] = 1; break;
          case 'B': board[i][j] = 2; break;
        }
      }
      cin >> ws;
    }
    for(int i=0; i<N; i++) {
      startj = N-1;
      for(int count=0; count<N; count++) {
        if(board[i][startj] == 0) {
          for(int j = startj; j >= 1; j--) {
            board[i][j] = board[i][j-1];
          }
          board[i][0] = 0;
        } else {
          startj--;
        }
      }
    }
    cout << "Case #" << t << ": ";
    if(checkforwin(1) && checkforwin(2)) {
      cout << "Both" << endl;
    } else if(checkforwin(1) && !checkforwin(2)) {
      cout << "Red" << endl;
    } else if(!checkforwin(1) && checkforwin(2)) {
      cout << "Blue" << endl;
    } else {
      cout << "Neither" << endl;
    }
  }
  
  return 0;
}
