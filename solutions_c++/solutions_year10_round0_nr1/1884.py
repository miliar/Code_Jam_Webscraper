#include <iostream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <string>
#include <sstream>


using namespace std;

template <typename T>
void convertStoT(T &value, const string &str) {
  stringstream istr(str);
  istr >> value;
}

int main (int argc, char **argv) {
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);
  vector<string> svec;
  
  copy(istream_iterator<string>(ifile),
       istream_iterator<string>(),
       back_inserter(svec));

  const int T = atoi(svec[0].c_str());
  int counter = 0;
  for (int i = 0; i < T; ++i) {
    const int N = atoi(svec[++counter].c_str());
    long long unsigned int K = 0;
    convertStoT(K, svec[++counter]);
    
    if ( 0 == K)
      ofile << "Case #" << i+1 << ": OFF" << endl;
    else {
      long long unsigned int powval = 1 << N;
      if (K%powval == (powval-1))
	ofile << "Case #" << i+1 << ": ON" << endl;
      else
	ofile << "Case #" << i+1 << ": OFF" << endl;
    }
  }
}
