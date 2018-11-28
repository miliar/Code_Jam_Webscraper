#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;


int gcd(int pd){
  int res = 1;
  if(!(pd % 4)) res *= 4;
  else if (!(pd % 2)) res *= 2;

  if(!(pd % 25)) res *= 25;
  else if (!(pd % 5)) res *= 5;

  return res;
}

bool possible(long long n, int pd, int pg) {
  if(!pg)
    if(pd) return false;
    else return true;
  if(pg == 100)
    if(pd == 100) return true;
    else return false;

  if(!pd) return true;

  long long n1 = 100 / gcd(pd);

  if(n1 <= n) return true;
  else return false;
}

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int pd, pg;
    long long n;
    cin >> n >> pd >> pg;
    cout << "Case #" << tcase << ": ";
    if(possible(n, pd, pg))
      cout << "Possible\n";
    else
      cout << "Broken\n";
  }
}
