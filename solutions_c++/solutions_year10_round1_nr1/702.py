#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(int argc, const char* argv[]) {
  FILE* f=fopen(argv[1], "r");
  FILE* f2=fopen(argv[2], "w");

  int C;
  fscanf(f, "%d", &C);

  for(int c=0; c < C; c++) {
    int N, K;
    fscanf(f, "%d %d", &N, &K);
    // printf("N:%d K:%d\n", N, K);


    vector<vector<char> > board;
    board.resize(N);
    for(int j=0; j < N; j++) {
      board[j].resize(N);
      for(int k=0; k < N; k++) {
        char ch = ' ';
        while (ch != '.' && ch != 'R' && ch != 'B') {
          ch = fgetc(f);
        }
        // printf("%c\n", ch);
        board[j][k] = ch;
      }
    }

    // shift pieces down
    for(int i=0; i < N; i++) {
      for(int j=N-1; j >=0; j--) {
        if (board[i][j] == '.') {
          int j1=j-1;
          while (j1 >= 0 && board[i][j1] == '.')
            j1--;
          if (j1 >= 0) {
            board[i][j] = board[i][j1];
            board[i][j1] = '.';
          }
        }
      }
    }

    /*
    for(int i=0; i < N; i++) {
      for(int j=0; j < N; j++) {
        printf("%c", board[i][j]);
      }
      printf("\n");
    }
    */


    bool rwins = false;
    bool bwins = false;

    for(int i=0; i < N; i++) {
      for(int j=0; j < N; j++) {
        if (board[i][j] != '.') {
          int i1=0;
          for(i1=0; i1 < K && i1+i < N && board[i+i1][j]==board[i][j]; i1++);
          if (i1 == K && board[i][j] == 'R') {
            rwins = true;
          }
          if (i1 == K && board[i][j] == 'B') {
            bwins = true;
          }

          i1=0;
          for(i1=0; i1 < K && i1+j < N && board[i][j+i1]==board[i][j]; i1++);
          if (i1 == K && board[i][j] == 'R') {
            rwins = true;
          }
          if (i1 == K && board[i][j] == 'B') {
            bwins = true;
          }

          i1=0;
          for(i1=0; i1 < K && i1+j < N && i1+i < N && board[i+i1][j+i1]==board[i][j]; i1++);
          if (i1 == K && board[i][j] == 'R') {
            rwins = true;
          }
          if (i1 == K && board[i][j] == 'B') {
            bwins = true;
          }

          i1=0;
          for(i1=0; i1 < K && j-i1 >= 0 && i1+i < N && board[i+i1][j-i1]==board[i][j]; i1++);
          if (i1 == K && board[i][j] == 'R') {
            rwins = true;
          }
          if (i1 == K && board[i][j] == 'B') {
            bwins = true;
          }


        }

      }
    }

    char* result;
    if (rwins && bwins) {
      result = "Both";
    } else if (rwins) {
      result = "Red";
    } else if (bwins) {
      result = "Blue";
    } else
      result = "Neither";

    fprintf(f2, "Case #%d: %s\n", c+1, result);
  }
  fclose(f);
  fclose(f2);
}


