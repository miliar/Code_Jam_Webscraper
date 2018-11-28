#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
#include <set>

using namespace std;

int gcd(int a, int b){
  if(b == 0) return a;
  return gcd(b, a%b);
}

int main() {
  int T; cin >> T;
  for(int cs = 1; cs <= T; ++cs){
    long long N;
    int PD, PG; cin >> N >> PD >> PG;
    int g = gcd(PD, 100);
    long long div = 100/g;
    long long played = div; 
    if((PG == 100 && PD != 100) || (PG == 0 && PD != 0) || played > N){
      printf("Case #%d: Broken\n", cs);
    }
    else{
      printf("Case #%d: Possible\n", cs);
    }
  }
  return 0;
}
