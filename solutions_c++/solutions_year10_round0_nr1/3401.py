#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;
int main(int argc, char** argv) {
  ifstream file(argv[1]);
  int nbTestCases;
  file >> nbTestCases;
//  cout << nbTestCases<< endl;
  for (int i = 0; i<nbTestCases; ++i ) {
      int n;
      long long k;
      file >> n >> k;
      long long mx = 2;
      for (int j=1;  j<n; ++j) {
        mx *= 2;  
      }
   //   cout << "n=#" << n << " mx=" << mx << endl;


//      cout << n << " " << k << endl;
      cout << "Case #" << i+1 << ": " <<
          (( (k % mx ) == (mx-1) ) ? "ON" : "OFF") << endl;
  }
}
