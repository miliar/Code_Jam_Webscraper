#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;


#define SMALL_NON_ZERO 0.00000001 /* or something else small */
double ABS(double a)
{
   return ((a)<0?-(a):a);
}

int players[10002];

int main() {
  int cases;

  cin >> cases;

  for(int cas = 1; cas <= cases; cas++) {
    int n, l, h;
    
    cin >> n >> l >> h;
    
    for(int j = 0; j < n; j++) {
	cin >> players[j];
    }
    bool possible = false;
    int i;
    for(i = l; i <= h && !possible; i++){
      bool next = false;
      possible = true;
      for(int j = 0; j < n; j++) {
	if(!(players[j] % i == 0 || i % players[j] == 0)) {
	  next = true;
	  possible = false;
	  break;
	}
      }
      if(next) continue;
    }
    
    if(!possible)
      cout << "Case #" << cas << ": NO" << endl;
    else
      cout << "Case #" << cas << ": " << i-1 << endl;
    
  }
  
  return 0;
}