
#include <cstdlib>
#include <iostream>
#include <ctime>
#include <queue>
#include <cstdio>
#include <cstdarg>
#include <fstream>

using namespace std;

int go(bool b, queue<int> &q, int *p, int *r){
  int nMotion = abs(q.front()-p[b])-r[b];
  if(nMotion < 0) nMotion = 0;

  r[b] = 0;
  nMotion++;
 
  p[b] = q.front();
  q.pop();

  r[!b] += nMotion;

  return nMotion;
}


int main(int argc, char** argv){
  ifstream cin("in.txt");
  ofstream cout("out.txt");

  int nCase, nMove;

  cin >> nCase;
  for(int i = 0; i < nCase; i++){
    cin >> nMove;

    queue<int> q[2];
    queue<bool> iR;

    for(int j = 0; j < nMove; j++){
      char r, ch;
      int n;
      cin >> r >> n;
      bool b = (r == 'O') ? 0 : 1;
      iR.push(b);
      q[b].push(n);
    }

    int p[2] = {1,1},
        r[2] = {0,0};

    int n = 0, move = 0;
    while(n++ != nMove){
      bool b = iR.front();
      move += go(b,q[b],p,r);
      iR.pop();
    }

    cout << "Case #" << i+1 << ": " << move << "\n";
  }

  return 0;
}

