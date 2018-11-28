#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
  int N;
  cin >> N;

  string t;
  for (int a = 1; a <= N; a++) {
    cout << "Case #" << a << ": ";

    int s;
    cin >> s;
    getline(cin, t);

    string se[s];
    for (int i = 0; i < s; i++) {
      getline(cin, se[i]);
    }

    int q;
    cin >> q;
    getline(cin, t);

    int sw[s][q+1];
    fill(&sw[0][0], &sw[s-1][q]+1, 0);

    for (int i = q-1; i >= 0; i--) {
      getline(cin, t);

      for (int j = 0; j < s; j++) {
	if (se[j] == t) {
	  sw[j][i] = INT_MAX;
	  for (int k = 0; k < s; k++) {
	    if (j != k) {
	      sw[j][i] = min(sw[j][i], sw[k][i+1] + 1);
	    }
	  }
	}
	else {
	  sw[j][i] = sw[j][i+1];
	}
      }
    }
    
    int ans = INT_MAX;
    for (int i = 0; i < s; i++) {
      ans = min(sw[i][0], ans);
    }
    cout << ans << endl;
  }
    
  return 0;
}
