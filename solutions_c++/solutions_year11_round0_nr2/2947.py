#include <iostream>
#include <string>

using namespace std;

int main() {
  unsigned int T;

  //read in the number of test cases
  cin >> T;
  for (unsigned int i = 0; i < T; ++i) {
    char combine[26][26];
    bool oppose[26][26];

    for (unsigned int j = 0; j < 26; ++j) {
      for (unsigned int k = 0; k < 26; ++k) {
	combine[j][k] = '0';
	oppose[j][k] = false;
      }
    }

    //read in the number of combines
    unsigned int C;
    cin >> C;

    //read in the elements combination
    for (unsigned int j = 0; j < C; ++j) {
      char c1, c2, c3;
      cin >> c1 >> c2 >> c3;

      combine[c1-'A'][c2-'A'] = c3;
      combine[c2-'A'][c1-'A'] = c3;
    }

    
    //read in the number of oppositions
    unsigned int D;
    cin >> D;

    //read in the elements oppositions
    for (unsigned int j = 0; j < D; ++j) {
      char c1, c2;
      cin >> c1 >> c2;

      oppose[c1-'A'][c2-'A'] = true;
      oppose[c2-'A'][c1-'A'] = true;
    }

    
    //read in the number of characters in base elements
    unsigned int N;
    cin >> N;

    string ans;
    for (unsigned int j = 0; j < N; ++j) {
      char c;
      cin >> c;

      ans.push_back(c);

      if (ans.size() == 1)
	continue;

      //perform combinations
      if (combine[ans[ans.size()-1]-'A'][ans[ans.size()-2]-'A'] != '0') {
	ans[ans.size()-2] = combine[ans[ans.size()-1]-'A'][ans[ans.size()-2]-'A'];
	ans.erase(ans.end()-1);
	continue;
      }


      //then perform oppositions
      for (unsigned int k = 0; k < ans.size()-1; ++k) {
	if (oppose[ans[k]-'A'][ans[ans.size()-1]-'A']) {
	  ans.clear();
	  break;
	}
      }
    }


    cout <<"Case #"<<i+1<<": [";
    for (unsigned int j = 0; j < ans.size(); ++j) {
      cout <<ans[j];
      
      if (j != ans.size()-1)
	cout <<", ";
    }

    cout <<"]\n";
  }

  return 0;
}
