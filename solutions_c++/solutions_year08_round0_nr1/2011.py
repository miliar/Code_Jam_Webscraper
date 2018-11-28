#include <iostream>
#include <map>
#include <queue>

#define maxq 1001
#define maxs 101

using namespace std;

map<string, int> ms;
int t[maxs], nt, ns, nq;

int main () {

  cin >> nt;
  for (int nc = 1; nc <= nt; nc++) {
  
    ms.clear();    
  
    cin >> ns;
    string s;
    getline(cin, s);
    for (int i = 0; i < ns; i++) {
      getline(cin, s);
      ms[s] = i;
      t[i] = 0;
    }
    
    cin >> nq;
    getline(cin, s);
    for (int i = 0; i < nq; i++) {
      getline(cin, s);
      //cout << s << endl;
      if (ms.count(s) == 1) {
        int a = ms[s];
        int mi = 100000;
        for (int j = 0; j < ns; j++)
          if (j != a && mi > t[j]) {
            mi = t[j]; 
          }
        t[a] = mi+1;
      }
    }
    int mi = 100000;
        for (int j = 0; j < ns; j++)
          if (mi > t[j])
            mi = t[j]; 
    
    cout << "Case #" << nc << ": " << mi << endl;
  }

  return 0;
}
