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
    int* a = new int[n];
    int* b = new int[n];
    int* done_1 = new int[n];
    int* done_2 = new int[n];

    for (int j = 0; j < n; j++) {
      inp>>a[j]>>b[j];
      done_1[j] = 0;
      done_2[j] = 0;
    }

    int total_games = 0;
    int levels_complete = 0;
    int stars = 0;
    while (levels_complete != n) {
      bool contin = false;
      for (int j = 0; j < n; j++) {
        if (done_2[j] == 0 &&
            done_1[j] == 0 &&
            b[j] <= stars) {
          done_1[j] = 1;
          done_2[j] = 1;
          stars += 2;
          levels_complete++;
          total_games++;
          contin = true;
          break;
        }
      }
      if (contin)
        continue;
      for (int j = 0; j < n; j++) {
        if (done_2[j] == 0 &&
            b[j] <= stars) {
          done_1[j] = 1;
          done_2[j] = 1;
          stars += 1;
          levels_complete++;
          total_games++;
          contin = true;
          break;
        }
      }
      if (contin)
        continue;
      int max_b = -1;
      for (int j = 0; j < n; j++) {
        if (done_1[j] == 0 &&
            a[j] <= stars) {
          if (max_b == -1) {
            max_b = j;
          } else {
            if (b[j] > b[max_b]) {
              max_b = j;
            }
          }
          contin = true;
        }
      }
      if (!contin) {
        break;
      } else {
        done_1[max_b] = 1;
        stars += 1;
        total_games++;
        contin = true;
      }
    }
    if (levels_complete == n) {
      outp<<"Case #"<<i+1<<": "<<total_games<<endl;
    } else {
      outp<<"Case #"<<i+1<<": "<<"Too Bad"<<endl;
    }
    delete[] a;
    delete[] b;
    delete[] done_1;
    delete[] done_2;
    /* End of code */

  }

  inp.close();
  outp.close();
}
