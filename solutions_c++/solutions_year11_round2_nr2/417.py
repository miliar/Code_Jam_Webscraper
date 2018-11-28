#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int num_test_cases=0;
  input >> num_test_cases;
  for(int test(0); test != num_test_cases; ++test) {
      int c(0);
      input >> c;
      int d(0);
      input >> d;
      vector<int> vendors;
      vector<int> points;
      for(int i(0); i != c; ++i) {
          int temp(0);
          input >> temp;
          points.push_back(temp);
          input >> temp;
          vendors.push_back(temp);
      }
      double maxtime(0);
      for(int i(0); i != c; ++i) {
          for(int j(i+1); j != c+1; ++j) {
              double between(0);
              double dist = points[j-1]-points[i];
              for(int k(i); k != j; ++k) {
                  between += vendors[k];
              }
              double time = (d*(between - 1)-dist)/2.0;
              if(time > maxtime)
                  maxtime = time;
          }
      }
      cout << fixed << "Case #" << test+1 << ": " << maxtime << endl;
  }
          
  input.close();
  return 0;
}
