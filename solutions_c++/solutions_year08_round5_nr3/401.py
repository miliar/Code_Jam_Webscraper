#include <iostream>
#include <fstream>
#include <vector>
#include <sys/time.h>
#include <cstdlib>
using namespace std;

ifstream in("cheat.in");
ofstream out("cheat.out");

int M,N,bestnum;
vector<string> v;

timeval tim;
int t0;


int nextr(int r, int c) {
  if (c == N-1) {
    return r-1;
  }
  return r;
}
int nextc(int r, int c) {
  if (c == N-1) {
    if (r == 0) {
      return -1;
    }
    return 0;
  }
  return c+1;
}

void foo(int r, int c, int curnum) {
  if (curnum > bestnum) {
    bestnum = curnum;
  } else if (bestnum - curnum > r*((N+1)/2) + (c+1)/2) {
    return;
  }
  //gettimeofday(&tim, NULL);
  //int t1 = tim.tv_sec;
  //if (t1 - t0 > 30) {
  //  return;
  //}
  if (r == -1 && c == -1) {
    return;
  }
  if (v[r][c] != 'x') {
    if ( (r == M-1 || c == N-1 || v[r+1][c+1] != 's') 
	 && (r == M-1 || c == 0 || v[r+1][c-1] != 's') 
	 && (c == 0 || v[r][c-1] != 's') ) {
      v[r][c] = 's';
      foo(nextr(r,c),nextc(r,c),curnum+1);
      v[r][c] = '.';
    }
  }
  foo(nextr(r,c),nextc(r,c),curnum);
}

int main() {
  int C;
  in >> C;

  for (int casenum = 1; casenum <= C; casenum++) {
    //gettimeofday(&tim, NULL);
    //t0 = tim.tv_sec;
    in >> M >> N;
    bestnum = 0;
    v.clear();
    v.resize(M);
    for (int i = M - 1; i >= 0; i--) {
      in >> v[i];
    }
    foo(M-1,0,0);
    out << "Case #" << casenum << ": " << bestnum << endl;

  }
  return 0;
}
