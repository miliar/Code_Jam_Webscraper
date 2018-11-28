#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cmath>
using namespace std;

int width, threshold;
char input[50][50], output[50][50];

void judge(int x, int y, bool &red_win, bool &blue_win, bool init=false) {
  static int cnt;
  static char mode;

  if(init) {
    cnt = 0;
    mode = ' ';
    //    cout << "init!" << endl;
    return;
  }

  //  cout << "(x,y) = " << x << " " << y << endl;
  if(output[x][y] != mode) {
    mode = output[x][y];
    cnt = 0;
    return;
  }
  
  cnt++;
  if(cnt+1 >= threshold) {
    switch(mode) {
    case 'R':
      red_win = true;
      //      cout << "red_win" << endl;
      break;
    case 'B':
      blue_win = true;
      //      cout << "blue_win" << endl;
      break;
    }
  }
  
}

int main() {
  int testcase;
  cin >> testcase;

  for(int iii=1; iii<=testcase; iii++) {
    cin >> width >> threshold;

    for(int y=0; y<width; y++) {
      for(int x=0; x<width; x++) {
        cin >> input[x][y];
        output[x][y] = ' ';
      }
    }

    int index[width];
    fill_n(index, width, 0);

    for(int y=width-1; y>=0; y--) {
      for(int x=0; x<width; x++) {
        if(input[y][x] == '.') continue;

        output[x][index[x]++] = input[y][x];
        input[y][x] = '.';
      }
    }
    /*
    for(int y=0; y<width; y++) {
      for(int x=0; x<width; x++) {
        cout << output[x][y] << " ";
      }
      cout << endl;
    }
    //*/

    bool red_win = false, blue_win = false;
    for(int y=0; y<width; y++) {
      judge(0, 0, red_win, blue_win, true);
      for(int x=0; x<width; x++) {
        judge(x, y, red_win, blue_win);
      }
    }

    for(int x=0; x<width; x++) {
      judge(0, 0, red_win, blue_win, true);
      for(int y=0; y<width; y++) {
        judge(x, y, red_win, blue_win);
      }
    }

    for(int xxx=-width+1; xxx<width; xxx++) {
      judge(0, 0, red_win, blue_win, true);
      int x = xxx;
      int y = 0;
      if(x < 0) {
        y = -x;
        x = 0;
      }
      for(int i=0; x+i < width && y+i < width; i++) {
        judge(x+i, y+i, red_win, blue_win);
      }
    }

    //    cout << "---" << endl;
    for(int xxx=0; xxx<width*2; xxx++) {
      judge(0, 0, red_win, blue_win, true);
      int x = xxx;
      int y = 0;
      if(x >= width) {
        y = x-(width-1);
        x = width-1;
      }
      for(int i=0; x-i>=0 && y+i<width; i++) {
        judge(x-i, y+i, red_win, blue_win);
      }
    }

    cout << "Case #" << iii << ": ";
    if(red_win) {
      if(blue_win) cout << "Both" << endl;
      else cout << "Red" << endl;
    } else {
      if(blue_win) cout << "Blue" << endl;
      else cout << "Neither" << endl;
    }
    
  }


  return 0;
}
