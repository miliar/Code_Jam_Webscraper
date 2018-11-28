#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int INF = 0x7fffffff;
int a[1001][101];
vector<string> Q;
map<string, int> S;
int n, m;

void munch() {
  while(getchar() != '\n');
}

string read_str() {
  string r;
  for(int ch=getchar(); ch!='\n'; ch=getchar()) {
    r.push_back(ch);
  }
  return r;
}

int go2(int pos, int piece) {
  if (pos == m) {
    return 0;
  } else {
    int& r = a[pos][piece];
    if (r == -1) {
      if (S.find(Q[pos]) == S.end()) {
	r = go2(pos+1, piece);
      } else {
	int t = S[Q[pos]];
	if (t != piece) {
	  r = go2(pos+1, piece);
	} else {
	  r = INF;
	  for(int j=0; j<n; ++j) {
	    if (j != t) {
	      r <?= 1+go2(pos+1, j);
	    }
	  }
	}
      }
    }
    return r;
  }
}

int go() {
  int s; scanf("%d", &s); munch();
  n = s;
  S.clear();
  while(s--) {
    string str;
    S[str=read_str()] = s;
  }
  int q; scanf("%d", &q); munch();
  m = q;
  Q.clear();
  while(q--) {
    Q.push_back(read_str());
  }
  reverse(Q.begin(), Q.end());
  if (Q.size() == 0) {
    return 0;
  } else if (Q.size() == 1) {
    return 0;
  } else {
    memset(a, -1, sizeof(a));
    int mn = INF;
    for(int j=0; j<n; ++j) {
      mn <?= go2(0, j);
    }
    return mn;
  }
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    printf("Case #%d: %d\n", i, go());
  }
}
