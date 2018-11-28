#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int n;
    cin >> n;
    vector<int> v;
    for (int k = 0; k < n; k++) {
      string s;
      cin >> s;
      int maxplace = -1;
      for (int j = 0; j < s.length(); j++) {
	if (s[j] == '1') maxplace = j;
      }
      v.push_back(maxplace);
    }

    int ct = 0;
    for (int i = 0; i < n; i++) {
      
      int use = -1;
      for (int j = i; j < n; j++) {
	if (v[j] <= i) {
	  use = j;
	  break;
	}
      }

      for (int j = use; j >= i+1; j--) {
	swap(v[j], v[j-1]);
	ct++;
      }
    }

    cout << "Case #" << t+1 << ": " << ct << endl;

  }
  
}
