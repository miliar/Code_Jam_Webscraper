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


int main(int argc, char **argv) {
  if (!argc) {
    return 1;
  }  
  
  int len = strlen(argv[1]);
  char fname[len+5];
  strcpy(fname, argv[1]);

  strcpy(fname+len, ".in");
  fstream fin(fname, fstream::in);

  strcpy(fname+len, ".out");
  fstream fout(fname, fstream::out);

  //Get number of cases
  int numTests;
  fin >> numTests;
  fin.ignore_line();

  // Loop over each case
  for (int test = 1; test <= numTests; test += 1) {
    // Do stuff here...
    int num, Pd, Pg;
    fin >> num >> Pd >> Pg;
    
    bool gotit = false;
    int tops;
    if (num < 100) {
      tops = num;
    } else {
      tops = 0;
      gotit = true;
    }
    int i;
    for (i=1; i<=tops; i+=1) {
      if ((Pd*i)%100 == 0) {
        gotit = true;
        break;
      }
    }
   
    if (gotit && (Pg != 100 || Pd == 100) && (Pg != 0 || Pd == 0))  {
      fout << "Case #" << test << ": Possible" << endl;
    } else {
      fout << "Case #" << test << ": Broken" << endl;
    }

    // Print output here
  }
    
  return 0;
}
