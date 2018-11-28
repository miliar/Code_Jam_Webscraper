#include <iostream>
#include <cassert>
using namespace std;
inline int abs(int x) {
    return (x<0)?(-x):x;
}
int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        int N;
        cin >> N;
        int lef[2] = {0,0};
        int pos[2] = {1,1};
        int sol = 0;
        while(N--) {
	  char c;
	  int my_pos;
	  cin >> c >> my_pos;
	  int numer;
	  if(c == 'O')
	      numer = 0;
	  else if(c == 'B')
	      numer = 1;
	  else
	      assert(false);
	  
	  int other = (numer+1)%2;
	  int lmoves = abs(pos[numer] - my_pos);
	  pos[numer] = my_pos;
	  if(lef[numer] < lmoves) {
	      int add_time = lmoves - lef[numer];
	      sol += add_time;
	      lef[other] += add_time;
	  }
	  lef[numer] = 0;
	  lef[other]++;
	  sol++;
        }
        cout << "Case #" << z << ": " << sol << "\n";
    }
    return 0;
}