#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "wt", stdout);

  int no_case;
  char board[100][100];
  char buffer[1024];
  int games[100];
  int win[100];
  double wp[100];
  double owp[100];
  double oowp[100];
  scanf("%d", &no_case);

  for(int no=1; no<=no_case; no++) {
    int N;
    scanf("%d", &N);

    for(int i=0; i<N; i++) {
      win[i] = 0;
      games[i] = 0;

      scanf("%s", buffer);
      for(int j=0; j<N; j++) {
        board[i][j] = buffer[j];
        if(board[i][j] == '1') {
          win[i]++;
          games[i]++;
        }
        else if(board[i][j] == '0')
          games[i]++;
      }
      wp[i] = (double) win[i] / games[i];
    }

    printf("Case #%d:\n", no);

    for(int i=0; i<N; i++) {
      int count = 0;
      double sum = 0;

      for(int j=0; j<N; j++) {
        if(board[j][i] != '.') {
          count++;
          if(board[j][i] == '1') {
            sum += (double) (win[j]-1) / (games[j]-1);
          } else {
            sum += (double) (win[j]) / (games[j]-1);
          }
        }
      }
      owp[i] = sum / count;
    }

    for(int i=0; i<N; i++) {
      int count = 0;
      double sum = 0;

      for(int j=0; j<N; j++) {
        if(board[i][j] != '.') {
          sum += owp[j];
          count++;
        }
      }
      oowp[i] = sum / count;
      printf("%.7lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
    }

  }
  
  return 0;
}