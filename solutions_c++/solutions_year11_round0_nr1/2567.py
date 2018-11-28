#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <ctime> 
 
using namespace std; 
 
int main () {
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int n, N;
    cin >> N;
    string s, prev = "";
    int p;
    int O = 0, B = 0, o = 1, b = 1;
    int time = 0;
    for (n = 0; n < N; n++) {
      cin >> s;
      cin >> p;
      if (s == "O") {
	O += abs (o - p) + 1;
	o = p;
	if (prev == "B") {
	  if (O > B) O -= B;
	  else O = 1;
	  time += B;
	  B = 0;
	}
	prev = "O";
      }
      if (s == "B") {
	B += abs (b - p) + 1;
	b = p;
	if (prev == "O") {
	  if (B > O) B -= O;
	  else B = 1;
	  time += O;
	  O = 0;
	}
	prev = "B";
      }
    }
    time += O + B;
    cout << "Case #" << t << ": " << time << endl;
  }
  return 0; 
}
