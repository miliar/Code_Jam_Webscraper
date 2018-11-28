#include <iostream>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <numeric>
#include <cassert>

using namespace std;
  
const int maxL = 15;

bool present[maxL][256];
vector<string> dic;

int L,D,N;
  
int main() {
  cin>>L>>D>>N;
  cin.ignore();
  for (int i = 0 ; i < D ; i++) {
    string s;  
    getline(cin, s);
    dic.push_back(s);
  }
  for (int i = 0 ; i < N ; ++i) {
    string s;
    getline(cin, s);
    fill(*present, *present + maxL * 256, false);
    int k = 0;
    for (int j = 0 ; j < s.size() ; j++, k++) {
      if (s[j] == '(') {
	while (s[++j] != ')') {
	  present[k][s[j]] = true;
	}
      } else {
	present[k][s[j]] = true;
      }
    }
    int K = 0;
    for (int j = 0 ; j < D ; ++j) {
      const string &s = dic[j];
      bool matches = true;
      for (int l = 0 ; l < s.size() && matches; l++) {
	if (!present[l][s[l]]) matches = false;
      }
      K += matches;
    }
    cout << "Case #" << i+1 << ": " << K << endl;
  }
}
