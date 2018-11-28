#include <iostream>
#include <vector>
using namespace std;

int gcd(int p, int q) {
  if(p > q)
    return gcd(q, p);

  // p  q
  int r = q % p;
  if(r == 0)
    return p;
  return gcd(r, p);
}

bool is_possible(int N, int Pd, int Pg) {
  if(Pg == 0 && Pd > 0)
    return false;

  if(Pg == 100 && Pd < 100)
    return false;

  if(Pd == 0 && Pg == 0)
    return true;

  int d = gcd(Pd, 100);
  int r = 100 / d;
  if(r <= N)
    return true;
  return false;
}

int main()
{
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
    int N, Pd, Pg;
    cin >> N >> Pd >> Pg;
    bool possible = is_possible(N, Pd, Pg);
    cout << "Case #" << c << ": " << (possible ? "Possible" : "Broken") << "\n";
  }
  
  return 0;
}
