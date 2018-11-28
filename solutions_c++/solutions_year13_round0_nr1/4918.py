#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cstring>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>

#define MOD 1000000007
using namespace std;
typedef vector<int> ivec;
int n;

void initialize() {

}

char input() {

  int  r=-1, c=-2;
  unsigned p;
  string str[4];
  for (int i = 0; i<4; i++) {
    cin>>str[i];
    p = str[i].find('T');
    if (p != string::npos) {
      r = i;
      c = p;
    }
  }

  //cout<<"r,c = "<<r<<" "<<c<<endl;

  ivec c1,d1,a1,b1;
  int dots = 0;
  char flag;

  c1.assign(255, 0);
  d1.assign(255, 0);
  for (int i =0; i<4; i++) {
    a1.assign(255, 0);
    b1.assign(255, 0);
    c1[str[i][i]]++;
    d1[str[i][3-i]]++;
    for (int j =0; j<4; j++) {
      a1[str[i][j]]++;
      b1[str[j][i]]++;
    }
    dots += a1['.'];

    if (a1['X'] + (r == i?1:0) == 4) {
      flag = 'X';
      return flag;
    } else if (a1['O'] + (r==i?1:0) == 4) {
      flag = 'O';
      return flag;
    } 
    else if (b1['X'] + (c == i?1:0) == 4) {
      flag = 'X';
      return flag;
    } else if (b1['O'] + (c==i?1:0) == 4) {
      flag = 'O';
      return flag;
    } 
  }


  if (c1['X'] + (r == c?1:0) == 4) {
      flag = 'X';
      return flag;
  } else if (c1['O'] + (r==c?1:0) == 4) {
      flag = 'O';
      return flag;
  } 
  if (d1['X'] + (r+ c == 3?1:0) == 4) {
      flag = 'X';
      return flag;
  } else if (d1['O'] + (r+c==3?1:0) == 4) {
      flag = 'O';
      return flag;
  } 

  if (dots > 0) {
    //cout<<"dots = "<<dots<<endl;
    return '.';
  } else {
    return 0;
  }

}

void process() {

}

void output() {

}

int main() {
    int i, t=1;
    string msg;
    cin >>t;
    initialize();
    for (i = 0; i <t; i++) {
        char v = input();
        switch(v) { 
          case 'X':
            msg = "X won";
          break;
          case 'O':
            msg = "O won";
          break;
          case '.':
            msg = "Game has not completed";
          break;
          case 0:
            msg = "Draw";
          break;
        }
        process();
        output();
        cout<<"Case #"<<i+1<<": "<<msg<<endl;
    }
    return 0;
}
