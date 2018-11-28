#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

char pav[51][51];

int R,C;

void draw(ostream &out) {
  for (int r=0;r<R;++r) {
    for (int c=0;c<C;++c) 
      out<< pav[r][c];
    out<<endl;
  }
}

int iter() {
  int r,c;
  //  draw(cerr);
  for (r=0;r<R;++r) {
    for (c=0;c<C;++c) {
      if (pav[r][c]=='#') {
	if (r<R-1 && c<C-1 && 
	    pav[r+1][c]=='#' && pav[r][c+1]=='#' && pav[r+1][c+1]=='#') {
	  pav[r][c] = pav[r+1][c+1] = '/';
	  pav[r+1][c] = pav[r][c+1] = '\\';
	  return 0;
	}
	return -1;
      }
    }
  }
  return 1;
}

int run() {
  do {
    int r=iter();
    if (r==-1) {
      cout<<"Impossible"<<endl;
      return 0;
    }
    if (r==1) {
      draw(cout);
      return 0;
    }
  } while (1);
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin>>R>>C;
    for (int i=0;i<R;++i) {
      cin>>pav[i];
    }
    
    cout<<"Case #"<<Ti<<":"<<endl;
    run();
  }
}
