#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int main() {
  int N; 
  cin >> N;
  string s;
  getline(cin, s);

  string t = "@welcome to code jam";

  for (int ii = 0; ii < N; ii++) {
    getline(cin, s);
    s = '@' + s;
    
    VVI M(s.length(), VI(t.length()));
    

    cout << "Case #" << ii+1 << ": ";
    
    for (int i = 0; i < s.length(); i++) {
      for (int j = 0; j < t.length(); j++) {
	if (i == 0 && j == 0) {
	  M[i][j] = 1;
	} else if (i == 0) {
	  M[i][j] = 0;
	} else if (j == 0) {
	  M[i][j] = 1;
	} else {
	  M[i][j] = M[i-1][j];
	  if (s[i] == t[j]) M[i][j] += M[i-1][j-1];
	  M[i][j] = M[i][j] % 10000;
	}	  
      }
    }

    printf("%04d\n", M[s.length()-1][t.length()-1]);
  }
}
