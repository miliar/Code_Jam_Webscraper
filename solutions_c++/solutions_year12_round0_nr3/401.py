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

    int a, b;
    inp>>a>>b;

    int order_10 = 1;
    int order = 0;
    int temp = a;
    while (temp / 10 > 0) {
      order++;
      temp /= 10;
    }
    for (int n = 0; n < order; n++) {
      order_10 *= 10;
    }
    int pairs = 0;
    for (int n = a; n < b; n++) {
      temp = n;
      int* temp_list = new int[order];
      for (int k = 0; k < order; k++) {
        temp = (temp / 10) + ((temp % 10) * order_10);
        temp_list[k] = temp;
        bool unique = true;
        for (int m = 0; m < k; m++) {
          if (temp == temp_list[m]) {
            unique = false;
            break;
          }
        }
        if (temp > n && temp <= b && unique) {
          pairs++;
        }
      }
      delete[] temp_list;
    }
    /* Code goes here */

    outp<<"Case #"<<i+1<<": "<<pairs<<endl;

    /* End of code */

  }

  inp.close();
  outp.close();
}
