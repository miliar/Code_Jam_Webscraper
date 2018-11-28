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

    /* Code goes here */
    int n;
    inp>>n;
    int* dist = new int[n];
    int* leng = new int[n];
    int* max_swing = new int[n];
    inp>>dist[0]>>leng[0];
    max_swing[0] = dist[0] * 2;
    for (int j = 1; j < n; j++) {
      inp>>dist[j]>>leng[j];
      int pot_max_swing = 0;
      for (int k = 0; k < j; k++) {
        if (dist[j] <= max_swing[k]) {
          if (leng[j] >= dist[j] - dist[k]) {
            if ((dist[j] - dist[k]) + dist[j] > pot_max_swing) {
              pot_max_swing = (dist[j] - dist[k]) + dist[j];
            }
          } else {
            if (dist[j] + leng[j] > pot_max_swing) {
              pot_max_swing = dist[j] + leng[j];
            }
          }
        }
       
      }
      max_swing[j] = pot_max_swing;
    }
    

    int d;
    inp>>d;
    bool can = false;
    for (int j = 0; j < n; j++) {
      if (max_swing[j] >= d) {
        can = true;
        break;
      }
    }
    if ( can) {
      outp<<"Case #"<<i+1<<": YES"<<endl;
    } else {
      outp<<"Case #"<<i+1<<": NO"<<endl;
    }
    delete[] max_swing;
    delete[] dist;
    delete[] leng;

    /* End of code */

  }

  inp.close();
  outp.close();
}
