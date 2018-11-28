#include <string>
#include <iostream>
#include <iomanip>
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

    /* Code goes here */

    int a, b;
    inp>>a>>b;
    double* p = new double[a];
    double* expe = new double[a + 2];
    double correct = 1;
    for (int j = 0; j < a; j++) {
      inp>>p[j];
      expe[j] = (((a - j) + (b - j) + 1)) +
          ((b + 1) * (1 - correct));
      correct *= p[j];
    }
    expe[a] = ((b - a + 1)) +
        ((b + 1) * (1 - correct));
    expe[a + 1] = (b + 2);
    
    outp<<"Case #"<<i+1<<": "<<setprecision(10)<<*min_element(expe, expe + a + 2)<<endl;

    /* End of code */
    delete[] p;
  }

  inp.close();
  outp.close();
}
