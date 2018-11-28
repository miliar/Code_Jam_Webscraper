#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<long>::iterator longIt;
typedef vector<double>::iterator doubleIt;
typedef vector<string>::iterator stringIt;
typedef vector<vector<long> >::iterator vecIntIt;
typedef vector<vector<double> >::iterator vecDoubleIt;
typedef vector<vector<string> >::iterator vecStringIt;

template <class T>
inline const T max_arg(const T& a, const T& b) {
  return (b < a) ? 1 : 2;
}

template <class T>
inline bool from_string(T& t, const string& s,
                        std::ios_base& (*f)(std::ios_base&)) {
  istringstream iss(s);
  return !(iss>>f>>t).fail();
}

template <class T>
inline string to_string(const T& t) {
  stringstream ss;
  ss<<t;
  return ss.str();
}

int main(int argc, char **argv) {
  ifstream inp(argv[1]); //input file
  ofstream outp((string(argv[1])+".out").c_str()); //output file

  int t;
  inp>>t;
  inp.get();

  char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
                  'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
                  'j', 'p', 'f', 'm', 'a', 'q'};

  for(int i = 0; i < t; i++) {

    /* Code goes here */
    char text_in[102];
    inp.getline(text_in, 102);
    for (int n = 0; n < 102; n++) {
      if (text_in[n] == 0) break;
      for (int m = 0; m < 26; m++) {
        if ((text_in[n] - 97) == m) {
          text_in[n] = map[m];
          break;
        }
      }
    }

    outp<<"Case #"<<i+1<<": "<<text_in<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
