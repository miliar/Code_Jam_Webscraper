#include <iostream>
#include <cstring>
#include <sstream>

using namespace std;

const int SIZE = 2000000;

bool vis[SIZE+1];

string toString(int x) {
  stringstream ss;
  ss << x;
  return ss.str();
}

int toInt(const string &x) {
  int ret = 0;
  for (int i = 0; i < (int)x.length(); i++)
    ret = 10 * ret + x[i] - '0';
  return ret;
}


string nextString(string x) {
  return x.substr(1) + x[0];
}

int main() {
  int T;
  cin >> T;
  
  for (int t = 0; t < T; t++) {
    memset(vis, 0, sizeof(vis));
    
    int A, B;
    cin >> A >> B;

    long long int ret = 0;
    for (int i = A; i <= B; i++) {
      if (vis[i])
	continue;
      long long int cnt = 0;
      
      string p0 = toString(i);
      string p = p0;
      for (;;) {
	if (p.length() != p0.length()) {
	  p = nextString(p);
	  continue;
	}
       	int q = toInt(p);
	if (vis[q])
	  break;
	vis[q] = true;
	if (A <= q && q <= B)
	  ++cnt;
	p = nextString(p);
      }
      ret += cnt * (cnt-1) / 2;
    }

    cout << "Case #" << t+1 << ": " << ret << endl;
  }

  return 0;
}
