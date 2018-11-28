#include <iostream>

using namespace std;


int main() {
  int tc=0, i = 0, j=0;
  cin >> tc;
  for (i = 0; i < tc; i++) {
    int N=0, S=0, p=0, w=0, d=0, have=0, m=0;
    cin >> N;
    cin >> S;
    cin >> p;
    
    for (j = 0; j < N; j++) {
      cin >> w;
      d = w/3;
      m = w%3;

      if (d >= p) have++;
      else if (d + 1 >= p && m >= 1) have++;
      else if (d + 1 >= p && m == 0 && S > 0 && d >= 1) {
	have++;
	S--;
      }
      else if (d + 2 >= p && m >= 2 && S > 0) {
	have++;
	S--;
      }
    }
    cout << "Case #" << i+1 << ": " << have << endl;
  }

  return 0;
}
