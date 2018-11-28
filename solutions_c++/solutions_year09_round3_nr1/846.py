//
// build via command line:
// g++ task.cpp -o task -lgmpxx -lgmp
//
// to run program:
// ./task A-task-data
//
// compiler version: g++ (Ubuntu 4.3.3-5ubuntu4) 4.3.3
//
// Coded by bearded
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>

#include <gmpxx.h> // uses for long numbers

using namespace std;

int main(int argc, char* argv[]) {
  string filename(argv[1]);
  string outfile = filename + ".out";
  string infile = filename + ".in";
  ifstream in(infile.c_str());
  ofstream out(outfile.c_str());

  int n;
  in >> n;

  string m;
  getline(in, m);
  for(int i=1; i<=n; i++) {
      getline(in, m);

      map<char, char> tt;
      for (int k=0; k<m.length(); k++) {
          tt[m[k]] = '0' - 1;
      }

      int bbase = tt.size();

      if (bbase == 1) {
          bbase++;
      }

 //     cout << m << endl;

      char ch = '0'; ch--;
      for (int k=0; k<m.length(); k++) {
          if (tt[m[k]] == '0'-1) {

              if (ch == '0'-1)
                  ch = '1';
              else if (ch == '1')
                  ch = '0';
              else if (ch == '0')
                  ch = '2';
              else if (ch == '9')
                  ch = 'a';
              else
                  ch++;
              tt[m[k]] = ch;
              m[k] = ch;
          } else {
              m[k] = tt[m[k]];
          }
      }

  //    cout << m << endl;

      try {
      mpz_class a(m, bbase);
      cout << "Case #" << i << ": " << a << endl;
      out << "Case #" << i << ": " << a << endl;
      }
      catch (...)
      {
          cout << "err" << endl;
      }


  }

  return 0;
}

