#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[]) {
  if(argc < 3)
    return 0;

  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  int T;
  ifs >> T;
  for(int t=1;t<=T;t++){
    ofs << "Case #" << t << ": ";

    long long R, C, D;
    ifs >> R;
    ifs >> C;
    ifs >> D;
    int **w = new int*[R];
    for(int r=0;r<R;r++) {
      w[r] = new int[C];
      char ch[2];
      for(int c=0;c<C;c++) {
	ifs >> ch[0];
	ch[1] = '\0';
	w[r][c] = atoi(ch);

	cout << w[r][c];
      }
      cout << endl;
    }
    cout << endl;

    long long max_blade_size = max(R, C);
    int size = max_blade_size;
    bool flag = false;
    long long mr, mc, mt;
    while(size >= 3) {
      if(flag)
	break;
      int re, ce;
      re = R - size;
      ce = C - size;
      for(int r=0;r<=re;r++) {
	if(flag)
	  break;
	for(int c=0;c<=ce;c++){
	  if(flag)
	    break;
	  mr = 0;
	  mc = 0;
	  mt = 0;
	  for(int br=0;br<size;br++) {
	    for(int bc=0;bc<size;bc++) {
	      if((br == 0 || br == size - 1) && (bc == 0 || bc == size - 1))
		continue;
	      mr += br * w[r + br][c + bc];
	      mc += bc * w[r + br][c + bc];
	      mt += w[r + br][c + bc];
	    }
	  }
	  if(mr * 2 == (size - 1) * mt && mc * 2 == (size - 1) * mt) {
	    ofs << size;
	    flag = true;
	  }

	  if(size == 5) {
	    cout << "mr = " << ((double)mr) << " mc = " << ((double)mc) << endl;
	    cout << "mr = " << mt << endl;
	  }
	}
      }
      size--;
    }
    if(!flag)
      ofs << "IMPOSSIBLE";

    for(int r=0;r<R;r++)
      delete []w[r];
    delete []w;



    ofs << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}
