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
  return (b<a)?1:2;
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

  for(int i=0; i<t; i++) {

    int N, S, p;
    /* Code goes here */

    inp>>N>>S>>p;
    int* ti = new int[N];

    for (int n = 0; n < N; n++) {
      inp>>ti[n];
    }

    int total = 0;
    for (int n = 0; n < N; n++) {
      if (ti[n] % 3 == 0) {
        if (ti[n] / 3 >= p) {
          total++;
          continue;
        }
        if (ti[n] >= 2 && ti[n] / 3 == (p - 1) && S > 0) {
          S--;
          total++;
          continue;
        }
      }
      if (ti[n] % 3 == 1) {
        if ((ti[n] / 3) + 1 >= p) {
          total++;
          continue;
        }
      }
      if (ti[n] % 3 == 2) {        
        if ((ti[n] / 3) + 1 >= p) {
          total++;
          continue;
        }
        if (ti[n] / 3 == (p - 2) && S > 0) {
          S--;
          total++;
          continue;
        }
      }
    }
    
    outp<<"Case #"<<i+1<<": "<<total<<endl;

    /* End of code */
    delete[] ti;
  }

  inp.close();
  outp.close();
}
