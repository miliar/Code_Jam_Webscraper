#include <iostream>
#include <string>
#include <map>
#include <set>

#define For(i,n) for(int i=0;i<(n);++i)


using namespace std;

int main() {
  int n;
  cin >> n;
  For(c,n) {
    cout << "Case #" << (c+1) << ": ";

    int s, q;
    cin >> s;
    set<string> se;
    string kk;
    getline(cin, kk);
    For(i, s) {
      getline(cin, kk);
      se.insert(kk);
    }
    
    int numsw = 0;
    map<string, bool> seen;
    cin >> q;
    getline(cin, kk);
    For(i, q) {
      string qu;
      getline(cin, qu);
      if (se.find(qu)!=se.end()) {
	seen[qu] = true;
      }
      if (seen.size()==s) {
	seen.clear();
	seen[qu] = true;
	++numsw;
      }
    }
    cout << numsw << endl;
  }
}
