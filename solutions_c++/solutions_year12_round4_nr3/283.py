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

bool sety(int* d, int* height, int j, int n) {
  bool ret = true;
  double alpha = (height[d[j]] - height[j]) / (d[j] - j);
  for (int k = j + 1; k < d[j]; k++) {
    while(double(height[k]-height[j]) / (k - j) >= alpha) {
      ret = false;
      height[d[j]] += 1;
      alpha = double(height[d[j]] - height[j]) / (d[j] - j);
    }
  }
  for (int k = d[j] + 1; k < n; k++) {
    while(double(height[k]- height[j]) / (k - j) > alpha) {
      ret = false;
      height[d[j]] += 1;
      alpha = double(height[d[j]] - height[j]) / (d[j] - j);
    }
  }
  return ret;
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
    int* d = new int[n - 1];
    int* order = new int[n];
    int* height = new int[n];
    double* line = new double[n - 1];
    for (int j = 0; j < n - 1; j++) {
      inp>>d[j];
      d[j] -= 1;
      height[j] = 1;
    }
    height[n - 1] = 1;
      
    bool pos = true;
    for (int j = 0; j < n - 1; j++) {
      for (int k = j; k < d[j]; k++) {
        if (d[k] > d[j])
          pos = false;
      }
    }
      
    if (pos) {

      bool conv = false;
      while (!conv) {
        conv = true;
        for (int j = 0; j < n - 1; j++)
          if (!sety(d, height, j, n)) {
            conv = false;
          }
      }
      
      outp<<"Case #"<<i+1<<":";
      for (int j = 0; j < n; j++) {
        outp<<" "<<height[j];
      }
      outp<<endl;
    } else {
      outp<<"Case #"<<i+1<<": Impossible"<<endl;
    }

    /* End of code */
    delete[] d;
    delete[] order;
    delete[] height;
  }

  inp.close();
  outp.close();
}
