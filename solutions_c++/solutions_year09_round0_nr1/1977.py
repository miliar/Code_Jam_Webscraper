#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isa_word(const vector<string> &words, string str);

int main() {
  int L, D, N;

  cin >> L >> D >> N;
  //  cout << "You just typed:" << L << D << N << endl;
  vector<string> words;
  for (int i = 0; i < D; i++) {
    string s;
    cin >> s;
    words.push_back(s);
  }
  //sort(words.begin(), words.end());

//   vector<string>::const_iterator iter = words.begin();
//   while (iter != words.end()) {
//     cout << *iter << endl;
//     iter++;
//   }


  int test_case = 1;
  while (N-- > 0) {
    cout << "Case #" << test_case++ << ": ";
    string s;
    cin >> s;

    string str[L]; // To store tokens
    int str_i = 0;
    char c[L+1]; // To store current token
    int c_i = 0;
    bool wait = false;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == ')') {
	c[c_i] = '\0';
	c_i = 0;
	wait = false;
	str[str_i++] = string(c);
      } else if (wait) {
	c[c_i++] = s[i];
      } else if (s[i] == '(') {
	wait = true;
	c_i = 0;
      } else {
	c[c_i++] = s[i];
	c[c_i] = '\0';
	c_i = 0;
	str[str_i++] = string(c);
      }
    }

//     for (int i = 0; i < L; i++) 
//       cout << str[i] << ",";
//     cout << endl;

    int num = 0;
    vector<string>::const_iterator iter = words.begin();
    while (iter != words.end()) {
      int i;
      for (i = 0; i < L; i++) {
        if (str[i].find((*iter)[i]) == -1)
	  break;
      }
      if (i == L)
	num++;

      iter++;
    }
    cout << num << endl;
  }
}


