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
      int teams=0;
      input >> teams;
      vector<vector<char> > results;
      for(int i(0); i != teams; ++i){
          results.push_back(vector<char>());
          for(int j(0); j != teams; ++j) {
              char temp;
              input >> temp;
              results[i].push_back(temp);
          }
      }
      vector<double> wps;
      for(int i(0); i != teams; ++i) {
          double won(0);
          double lost(0);
          for(int j(0); j != teams; ++j) {
              if(results[i][j] == '1')
                  ++won;
              if(results[i][j] == '0')
                  ++lost;
          }
          wps.push_back(won/(won+lost));
      }
  
      vector<double> owps;
      for(int i(0); i != teams; ++i){
          double sum(0);
          int opponents(0);
          for(int j(0); j != teams; ++j) {
              if(j == i || results[i][j] == '.')
                  continue;
              ++opponents;
              double won(0);
              double lost(0);
              for(int k(0); k != teams; ++k) {
                  if( k == i )
                      continue;
                  if(results[j][k] == '1')
                      ++won;
                  if(results[j][k] == '0')
                      ++lost;
              }
              sum += (won/(won+lost));
          }
          owps.push_back(sum/(double(opponents)));
      }
  
      vector<double> oowps;
      for(int i(0); i != teams; ++i) {
          double sum(0);
          int opponents(0);
          for(int j(0); j != teams; ++j) {
              if(results[i][j] == '.')
                  continue;
              ++opponents;
              sum += owps[j];
          }
          oowps.push_back(sum/opponents);
      }
      cout.precision(10);
      cout << "Case #" << test+1 << ":" << endl;
      for(int i(0); i != teams; ++i) {
          cout << 0.25*wps[i]+0.5*owps[i]+0.25*oowps[i] << endl;
      }
  }
  input.close();
  return 0;
}
