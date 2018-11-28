#define DBGLEVEL 1

//#include <mingw/_mingw.h>
#include <mingw/math.h>
#include "std.h"

char buf[1024*1024];

char* sol[31] = {
  "000", "005", "027", "143", "751", 
  "935", "607", "903", "991", "335",
  "047", "943", "471", "055", "447",
  "463", "991", "095", "607", "263",
  "151", "855", "527", "743", "351",
  "135", "407", "903", "791", "135",
  "647"
};

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int n; cin >> n;
    cin.getline(buf,sizeof buf);
    long double x = 5;
    x = sqrt(5) + 3;
    x = pow(x, n);
    DBG(1, n << ":" << setprecision(30)<<x);
    cout << sol[n];
    cout << endl;
  done:
    continue;
  }
  return 0;
}
