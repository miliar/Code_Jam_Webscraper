#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

int g[1000];

int turn[1000];
int riders[1000];

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int n, m; cin >> n >> m;
    cin.getline(buf,sizeof buf);
    set<string> dir;
    FOR(i, n) {
	string s;
	cin >> s;
	dir.insert(s);
	cin.getline(buf,sizeof buf);
    }
    dir.insert("");
    n = dir.size();
    FOR(i, m) {
	string s;
	cin >> s;
	FOR(i, s.size()) {
	    if (s[i] == '/') {
		dir.insert(s.substr(0, i));
	    }
	}
	dir.insert(s);
	cin.getline(buf,sizeof buf);
    }
    cout << dir.size() - n << endl;
    //    FOREACH(it, dir) cout << *it << ' ';
    //    cout << endl;
  }
  return 0;
}
