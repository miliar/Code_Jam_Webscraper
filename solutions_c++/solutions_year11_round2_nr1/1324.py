#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>

using namespace std;
using namespace boost;

#define foreach BOOST_FOREACH
#define reverse_foreach BOOST_REVERSE_FOREACH
#define tokeniz(str, sep)  tokenizer< char_separator<char> >(str, char_separator<char>(sep))
#define ignore_line() ignore(1024,'\n')

typedef unsigned int uint;
typedef unsigned long ulong;

int main(int argc, char **argv) {
  if (argc <= 1) {
    cerr << "No file given!" << endl;
    return 1;
  }  
  
  int len = strlen(argv[1]);
  char fname[len+5];
  strcpy(fname, argv[1]);

  strcpy(fname+len, ".in");
  fstream fin(fname, fstream::in);

  if (!fin) {
    cerr << '"' << fname << "\" not found" << endl;
    return 1;
  }

  strcpy(fname+len, ".out");
  fstream fout(fname, fstream::out);

  if (!fout) {
    cerr << '"' << fname << "\" could not be opened" << endl;
    return 1;
  }

  //Get number of cases
  int numTests;
  fin >> numTests;

  // Loop over each case
  for (int test = 1; test <= numTests; test += 1) {
    // Do stuff here...
    int N;
    fin >> N;
    fin.ignore_line();

    double p[N], wp[N], owp[N], oowp[N], awp[N];
    vector<int> opp[N];
    string games[N];
    for (int i=0; i<N; i+=1) {
      wp[i] = owp[i] = oowp[i] = 0;
    }

    for (int i=0; i<N; i+=1) {
      string line;
      getline(fin, line);
      games[i] = line;

      int j = 0;
      foreach(char oc, line) {
        if (oc != '.') {
          opp[i].push_back(j);
          if (oc == '1') {
            wp[i] += 1;
          }
        }
        j+=1;
      }
    }



    for (int i=0; i<N; i+=1) {
      foreach(int o, opp[i]) {
        char oc = games[i][o];
        double temp = wp[o];
        if (oc != '1') {
          temp -= 1;
        }
        owp[i] += temp / (double)(opp[o].size() - 1);
      }
    }
    for (int i=0; i<N; i+=1) {
      owp[i] /= (double) (opp[i].size());
      if (!opp[i].size()) {
        owp[i] = 0;
      }
    }

   for (int i=0; i<N; i+=1) {
      wp[i] /= (double) (opp[i].size());
      if (!opp[i].size()) {
        wp[i] = 0;
      }
    }

    for (int i=0; i<N; i+=1) {
      foreach(int o, opp[i]) {
        oowp[i] += owp[o];
      }
    }
    for (int i=0; i<N; i+=1) {
      oowp[i] /= (double) (opp[i].size());
      if (!opp[i].size()) {
        oowp[i] = 0;
      }
    }



    // Print output here
    fout << "Case #" << test << ":" << endl;

    for (int i=0; i<N; i+=1) {
      double ans = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
      //cout << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
      fout << ans << endl;
    }
  
  }
    
  return 0;
}
