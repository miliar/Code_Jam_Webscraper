#include <iostream>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main(/*unsigned long long argc, char **argv*/) {
  unsigned long long nb_test = 0;
  //freopen("input.txt", "r", stdin);
  cin >> nb_test;
  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    // For each test case
    int result = 0;
    int R;
    int C;
    cin >> R;
    cin >> C;
    ////cerr << "R: " <<R;
    ////cerr << " C: " <<C << endl;
    // Init tabs
    char **tab = (char**)calloc(sizeof(char*),R);
    for (int i=0; i<R; i++) tab[i] = (char*)calloc(sizeof(char),C);
    char **tab_res = (char**)calloc(sizeof(char*),R);
    for (int i=0; i<R; i++) tab_res[i] = (char*)calloc(sizeof(char),C);
    // Fill tab
    for (int ri=0; ri<R; ri++) {
      string rString;
      cin >> rString;
      //////cerr << rString << endl;
      for (int ci=0; ci<C; ci++) {
        ////cerr << "_ri, ci: " << ri << " " << ci << endl;
        tab[ri][ci] = rString.c_str()[ci];
        //////cerr << tab[ri][ci];
      }
      //////cerr << endl;
    }
    // Try to find solution
    bool possible = true;
    for (int ri=0; ri<R; ri++) {
      for (int ci=0; ci<C; ci++) {
        ////cerr << "ri, ci: " << ri << " " << ci << endl;
        ////cerr << tab[ri][ci];
        //tab_res[ci][ri] = tab[ci][ri];
        if (tab[ri][ci] == '#') {
          // Try to put red everywhere.
          //cerr << "DEBUG " << endl;
          tab[ri][ci] = '/';
          if (ci+1>=C || tab[ri][ci+1] == '.') {
            possible = false;
            //cerr << "DEBUG 0" << endl;
            break;
          }
          tab[ri][ci+1] = '\\';
          if (ri+1>=R || tab[ri+1][ci] == '.') {
            possible = false;
            //cerr << "DEBUG 1" << endl;
            break;
          }
          tab[ri+1][ci] = '\\';
          if (tab[ri+1][ci+1] == '.') {
            possible = false;
            //cerr << "DEBUG 2" << endl;
            break;
          }
          ////cerr << "DEBUG 3" << endl;
          tab[ri+1][ci+1] = '/';
          ////cerr << "DEBUG 4" << endl;
        }
      }
    }
    cout << "Case #" << test_i << ": " << endl;
    if (!possible) {
      cout << "Impossible";
      cout << endl;
    } else {
      for (int ri=0; ri<R; ri++) {
        for (int ci=0; ci<C; ci++) {
          cout << tab[ri][ci];
        }
        cout << endl;
      }
    }
  }
  return 0;
}

