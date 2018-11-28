#include<iostream>
#include<fstream>

using namespace std;

#define INPUTFILE "A-large.in"
#define OUTPUTFILE "text.out"


int main() {
  int nTest;
  ifstream fi(INPUTFILE);
  ofstream fo(OUTPUTFILE);
  fi >> nTest;
  for (int test = 1; test <= nTest; test ++) {
    int r, c;
    int a[100][100];
    string s;
    fi >> r >> c;
    getline(fi, s);
    for (int i = 0; i < 100; i ++)
      for (int j = 0; j < 100; j ++)
	a[i][j] = -1;
    for (int i = 0; i < r; i ++) {
      getline(fi, s);
      for (int j = 0; j < s.length(); j ++) {
	if (s[j] == '.') a[i][j] = 0;
	else if (s[j] == '#') a[i][j] = 1;
      }
    }
    for (int i = 0; i < r; i ++) {
      for (int j = 0; j < c; j ++)
	if (a[i][j] == 1) {
	  if (a[i][j+1] == 1 && a[i+1][j] == 1 && a[i+1][j+1] == 1) {
	    a[i][j] = 2;
	    a[i][j+1] = 3;
	    a[i+1][j] = 4;
	    a[i+1][j+1] = 5;
	  }
	}
    }
    bool ok = true;
    for (int i = 0; i < r; i ++) {
      for (int j = 0; j < c; j ++)
	if (a[i][j] == 1) {
	  ok = false;
	  break;
	}
      if (!ok) break;
    }
    fo << "Case #" << test << ":" << endl;
    if (!ok) fo << "Impossible" << endl;
    else {
      for (int i = 0; i < r; i ++) {
	for (int j = 0; j < c; j ++)
	  if (a[i][j] == 0) fo << '.';
	  else if (a[i][j] == 2) fo << '/';
	  else if (a[i][j] == 3) fo << char(92);
          else if (a[i][j] == 4) fo << char(92);
          else if (a[i][j] == 5) fo << '/';
	fo << endl;
      }
    }
  }
  fi.close();
  fo.close();
  return 0;
}
