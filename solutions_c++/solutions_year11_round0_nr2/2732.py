#include <fstream>
#include <vector>
#include <map>
#include <iostream>
#include <set>
#include <utility>
#include <string>
#define MP make_pair
#define PB push_back
#define all(v) v.begin(), v.end()
using namespace std;

map<pair<char, char>, char> combine;
set<pair<char, char> > oppose;
vector<char> simulator;
string the_list = "";
int main() {
    fstream tre;
    tre.open("Bsmall.txt");
    int n, c, d, t;
    tre >> t;
    for (int i = 0; i < t; ++i) {
          simulator.clear(); 
          combine.clear();
          oppose.clear();            
          tre >> c;
          for (int j = 0; j < c; ++j) {
                  string temp;
                  tre >> temp;
                  combine[MP(temp[0], temp[1])] = combine[MP(temp[1],temp[0])] = temp[2];
          }  
          tre >> d;
          for (int j = 0; j < d; ++j) {
                   string temp;
                   tre >> temp;
                   oppose.insert(MP(temp[0], temp[1]));
                   oppose.insert(MP(temp[1], temp[0]));
          }
          tre >> n;
          tre >> the_list;
          for (int j = 0; j < n; ++j) {
                  simulator.PB(the_list[j]);
                  if (simulator.size() > 1) {
                    
                     if (combine.count(MP(simulator[simulator.size() - 1], simulator[simulator.size() - 2]))) {
                           char temp = combine[MP(simulator[simulator.size() - 1], simulator[simulator.size() - 2])];
                           simulator.erase(simulator.end() - 2, simulator.end());
                           simulator.PB(temp);
                     }
                      for (int k = 0; k + 1 < simulator.size(); ++k) {
                         if (oppose.count(MP(simulator[k], simulator[simulator.size() - 1]))) {
                            simulator.clear();                              
                         }
                     }
                  }
          }
          cout <<"Case #" << i + 1 << ": [";
          for (int j = 0; j + 1 < simulator.size(); ++j) {
              cout << simulator[j] << ", ";    
          }
          if (!simulator.empty()) {
                cout << simulator.back();
          }
          cout << "]";
      //    if ( i + 1 < t) {
             cout<<endl;     
      //    }
    }
    return 0;   
}
