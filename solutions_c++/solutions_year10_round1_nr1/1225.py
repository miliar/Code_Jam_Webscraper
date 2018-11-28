#include <iostream>

using namespace std;

char board[100][100];
char new_board[100][100];

bool B, R;

void rotate(int N) {
    for (int row = 0; row < N; row++) {
    char found_chars[100];
    int count = 0;
     for (int col = 0; col < N; col++) {
       if (board[row][col] != '.') {
         found_chars[count] = board[row][col];
         count++;
       }
     }
     int start = N-1;
     for (;count > 0; count--) {
       board[row][start] = found_chars[count-1];
       start--;
      }
     for (; start >=0; start--) {
       board[row][start] = '.';
     }
    }
    /*
    for (int row = 0; row < N; row++) {
      for (int col = 0; col < N; col++) {
        cout << board[row][col];
      }
      cout << "\n";
    }
      cout << "\n";
      */
      

    for (int row = 0; row < N; row++) {
      for (int col = 0; col < N; col++) {
        new_board[row][col] = board[N-col-1][row];
      }
    }
    for (int row = 0; row < N; row++) {
      for (int col = 0; col < N; col++) {
        board[row][col] = new_board[row][col];
      }
    }
    /*
    for (int row = 0; row < N; row++) {
      for (int col = 0; col < N; col++) {
        cout << board[row][col];
      }
      cout << "\n";
    }
    */
}

void check_horiz(int N, int K){
    for (int row = 0; row < N; row++) {
    char last = '.';
    int count = 1;
     for (int col = 0; col < N; col++) {
       if (board[row][col] == last) {
         count++;
       } else {
         count = 1;
       }
       if(count == K) {
         if (last == 'B')
           B = true;
         if (last == 'R') 
           R = true;
       }
       last = board[row][col];
     }
    }
}

void check_vert(int N, int K){
    for (int col = 0; col < N; col++) {
    char last = '.';
    int count = 1;
     for (int row = 0; row < N; row++) {
       if (board[row][col] == last) {
         count++;
       } else {
         count = 1;
       }
       if(count == K) {
         if (last == 'B')
           B = true;
         if (last == 'R') 
           R = true;
       }
       last = board[row][col];
     }
    }
}

void check_diag_right(int N, int K) {
  for (int col = 0; col < N-1; col++) {
    char last = '.';
    int count = 1;
    int curr_col = col;
    for (int row = N-1; row >= 0; row--) {
       if (board[row][curr_col] == last) {
         count++;
       } else {
         count = 1;
       }
       if(count == K) {
         if (last == 'B')
           B = true;
         if (last == 'R') 
           R = true;
       }
       last = board[row][curr_col];
       curr_col++;
       if (curr_col >= N) {
         break;
       }
     }
    }
}


void check_diag_left(int N, int K) {
  for (int col = N-1; col >= 0; col--) {
    char last = '.';
    int count = 1;
    int curr_col = col;
    for (int row = N-1; row >= 0; row--) {
       if (board[row][curr_col] == last) {
         count++;
       } else {
         count = 1;
       }
       if(count == K) {
         if (last == 'B')
           B = true;
         if (last == 'R') 
           R = true;
       }
       last = board[row][curr_col];
       curr_col--;
       if (curr_col < 0) {
         break;
       }
     }
    }
}

int main() {
  int T, N, K;
  cin >> T;  
  for (int t = 0; t < T; t++) {
    cin >> N >> K;
    B = false; R = false;
    for (int row = 0; row < N; row++) {
     for (int col = 0; col < N; col++) {
       cin >> board[row][col];
     }
    }
    //rotate board
    rotate(N);

    //check winners
    check_horiz(N,K);
    check_vert(N,K);
    check_diag_right(N,K);
    check_diag_left(N,K);
    if (B && R) {
      cout << "Case #" << t+1 << ": Both\n";
    } else if (B) {
      cout << "Case #" << t+1 << ": Blue\n";
    } else if (R) {
      cout << "Case #" << t+1 << ": Red\n";
    } else {
      cout << "Case #" << t+1 << ": Neither\n";
    }
  }

  return 0;
}

