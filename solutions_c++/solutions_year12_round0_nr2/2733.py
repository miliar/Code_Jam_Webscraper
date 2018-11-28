#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  
  int T;
  cin >> T;
  
  string line;
  getline(cin, line);
  for(int t = 1; t <= T; t++) {
    getline(cin, line);
    stringstream ss(line);
    
    int num, p, N, S;
    ss >> N >> S >> p; // # googlers
    
    vector<int> nums;
    while(ss >> num) {
      nums.push_back(num);
    }

    int norm = 0, surp = 0;
    for(int i = 0; i < nums.size(); i++) {
      //cout << "num: " << nums[i];
      if(nums[i] % 3 == 0) {
        if(nums[i]/3 >= p) {
          norm++;
          //cout << " n ";
        } 
        else if(nums[i]/3+1 >= p && nums[i]/3-2 >= 0) {
          surp++;
          //cout << " s ";
        }
      } else if(nums[i] % 3 == 1) {
        if((nums[i]+2)/3 >= p) {
          norm++;
          //cout << " n ";
        }
      } else {
        if((nums[i]+1)/3 >= p) {
          norm++;
          //cout << " n ";
        }
        else if((nums[i]+4)/3 >= p && (nums[i]+4)/3-2 >= 0) {
          surp++;
          //cout << " s ";
        }
      }
      //cout << endl;
    }
    
    //cout << "norm: " << norm << " surp: " << surp << " S: "<< S <<  endl;
    cout << "Case #" << t << ": " << norm+min(S, surp) << endl;
  }
  
  return 0;
}
