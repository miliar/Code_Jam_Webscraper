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
    int winner = 0;
    bool full = true;
    string row[4];
    for (int j = 0; j < 4; j++) {
      inp>>row[j];
      int countO = 0;
      int countX = 0;
      for (int k = 0; k < 4; k++) {
	if (row[j][k] == '.') {
	  full = false;
	}
	if (row[j][k] == 'O' || row[j][k] == 'T') {
	  countO++;
	}
	if (row[j][k] == 'X' || row[j][k] == 'T') {
	  countX++;
	}
      }
      if (countO == 4) {
	winner = 1;
      }
      if (countX == 4) {
	winner = 2;
      }
    }
    if (winner == 0) {
      for (int j = 0; j < 4; j++) {
	int countO = 0;
	int countX = 0;
	for (int k = 0; k < 4; k++) {
	  if (row[k][j] == 'O' || row[k][j] == 'T') {
	    countO++;
	  }
	  if (row[k][j] == 'X' || row[k][j] == 'T') {
	    countX++;
	  }
	}
	if (countO == 4) {
	  winner = 1;
	}
	if (countX == 4) {
	  winner = 2;
	}
      }
      if (winner == 0) {

	int countO = 0;
	int countX = 0;
	for (int k = 0; k < 4; k++) {
	  if (row[k][k] == 'O' || row[k][k] == 'T') {
	    countO++;
	  }
	  if (row[k][k] == 'X' || row[k][k] == 'T') {
	    countX++;
	  }
	}
	if (countO == 4) {
	  winner = 1;
	}
	if (countX == 4) {
	  winner = 2;
	}

	countO = 0;
	countX = 0;
	for (int k = 0; k < 4; k++) {
	  if (row[k][3 - k] == 'O' || row[k][3 - k] == 'T') {
	    countO++;
	  }
	  if (row[k][3 - k] == 'X' || row[k][3 - k] == 'T') {
	    countX++;
	  }
	}
	if (countO == 4) {
	  winner = 1;
	}
	if (countX == 4) {
	  winner = 2;
	}
      }
    }
    

    if (winner == 1) {
      outp<<"Case #"<<i+1<<": O won";
    }
    if (winner == 2) {
      outp<<"Case #"<<i+1<<": X won";
    }
    if (winner == 0) {
      if (full) {
	outp<<"Case #"<<i+1<<": Draw";
      } else {
	outp<<"Case #"<<i+1<<": Game has not completed";
      }
    }
    outp<<endl;
	
      

    /* End of code */

  }

  inp.close();
  outp.close();
}
