// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cassert>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

int main() {
	int ile, c, d, n;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
    scanf("%d",&c);
    map<string, string> zmiana;
    set<string> usuwanie;
    REP(i, c) {
      char s[100];
      scanf("%s", s);
//      cout << "(" << s << ")" << endl;
      if (s[0] > s[1]) {
        swap(s[0], s[1]);
      }
      string kl = string(1, s[0]);
      kl+= s[1];
       
      string wr = string(1, s[2]);
      assert(zmiana.find(kl) == zmiana.end());
      zmiana[kl] = wr;
      swap(kl[0], kl[1]);
      zmiana[kl] = wr;

//      cout << kl << " --> " << wr << endl;
    }
    scanf("%d",&d);
    REP(i, d) {
      char s[2];
      scanf("%s", s);
      usuwanie.insert(string(1,s[0]) + s[1]);
      usuwanie.insert(string(1,s[1]) + s[0]);
      assert(s[0] != s[1]);
    }
    scanf("%d", &n);
    char slowo[200];
    vector<string> res;
    scanf("%s", slowo);
    string seq = slowo;
//    cout << seq << endl;
    REP(i, seq.size()) {
//      cout << ">>> chce dodac" << seq[i] << "<<< ("; REP(j, res.size()) cout << res[j]; cout << ")" << endl;
      if (res.size() == 0) {
        res.push_back(string(1, seq[i]));
      } else {
        string w1 = res.back();
        string w2 = string(1, seq[i]);
        if (w1 > w2) swap(w1, w2);
//        cout << "zmiana: " << w1+w2 << endl;
        if (zmiana.find(w1 + w2) != zmiana.end()) {
          res.pop_back();
          res.push_back(zmiana[w1 + w2]);
        } else {
          res.push_back(string(1, seq[i]));
          REP(i1, res.size()) {
            REP(i2, res.size()) {
//              cout << res[i1] + res[i2] << endl;
              if (usuwanie.find(res[i1] + res[i2]) != usuwanie.end()) {
                res.clear();
              }
            }
          }
        }
      }
    }
		printf("Case #%d: [",iile);
    REP(i, res.size()) {
      if (i == 0) {
        printf("%s", res[i].c_str());
      } else {
        printf(", %s", res[i].c_str());
      }
    }
    printf("]\n");
	}
	return 0;
}

