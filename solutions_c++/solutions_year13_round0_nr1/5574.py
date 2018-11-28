#include <iostream>
#include <vector>
#include <string>
#include "string.h"
using namespace std;

int main(int argc, char const *argv[])
{
  int count;
  int horz[2][4]={0}; // o for 0 x for 1
  int vect[2][4]={0};
  int cross[2][2]={0}; // 0 for j-k = 0 1 for j + k = 4
  int end = 1;
  cin >> count;
  string buf;
  for(int i = 0;i < count;i++) {
    memset(horz, 0, sizeof(horz));
    memset(vect, 0, sizeof(vect));
    memset(cross, 0, sizeof(cross));
    end = 1;
    for(int j = 0;j < 4;j++) {
      cin >> buf;
      // cout <<buf;
      for(int k = 0;k < 4;k++) {
        if(buf[k] == '.') {
          end = 0;
          // cout <<"catched" <<endl;
          continue;
        }
        if(buf[k] == 'X') {
          vect[1][k]++;
          horz[1][j]++;
          vect[0][k] = 0;
          horz[0][j] = 0;
          if(j == k) {
            cross[1][0]++;
            cross[0][0] = 0;
          }
          if(j + k == 4) {
            cross[1][1]++;
            cross[0][1] = 0;
          }
          continue;
        }
        if(buf[k] == 'O') {
          vect[0][k]++;
          horz[0][j]++;
          vect[1][k] = 0;
          horz[1][j] = 0;
          if(j == k) {
            cross[0][0]++;
            cross[1][0] = 0;
          }
          if(j + k == 4) {
            cross[0][1]++;
            cross[1][1] = 0;
          }
          continue;
        }
        if(buf[k] == 'T') {
          vect[0][k]++;
          horz[0][j]++;
          vect[1][k]++;
          horz[1][j]++;
          if(j == k) {
            cross[0][0]++;
            cross[1][0]++;
          }
          if(j + k == 4) {
            cross[0][1]++;
            cross[1][1]++;
          }
          continue;
        }
      }
    }
    // cin.getline(buf,);
    int printed = 0;
    for(int j = 0;j < 4 && !printed;j++) {
      if(horz[0][j] == 4 || vect[0][j] == 4) {
        cout <<"Case #" << i+1 << ": O won";
        printed = 1;
        break;
      }
      if(horz[1][j] == 4 || vect[1][j] == 4) {
        cout <<"Case #" << i+1 << ": X won";
        printed = 1;
        break;
      }
    }

    if((cross[0][1] == 4 || cross[0][0] == 4) && !printed) {
      cout <<"Case #" << i+1 << ": O won";
        printed = 1;
    }
    if((cross[1][1] == 4 || cross[1][0] == 4) && !printed) {
      cout <<"Case #" << i+1 << ": X won";
        printed = 1;
    }
    if(!printed) {
      if(end == 1) {
        cout <<"Case #" << i+1 <<": Draw";
      }
      else {
        cout <<"Case #" << i+1 <<": Game has not completed";
      }
    }
    if(i +1 != count) {
      cout <<endl;
    }
  }
  return 0;
}