#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)

int N, S, Q, q, p, r;
string str;
map<string,int> m;
int bol[101];

void clr() {
  p=0;
  REP(i,S) bol[i]=0;
}

int main() {
  scanf ("%d\n", &N);
  for (int tc=1; tc<=N; ++tc) {
    r=0; m.clear();
    scanf ("%d\n", &S);
    REP(i,S) {
      getline (cin, str);
      m[str]=i;
    }
    scanf ("%d\n", &Q);
    clr();
    REP(i,Q) {
      getline (cin, str);
      q = m[str];
      if (!bol[q]) {
        ++p; bol[q]=1;
        if (p==S) {
          ++r; clr(); ++p; bol[q]=1;
        }
      }
    }
    cout << "Case #" << tc << ": " << r << endl;
  }
  return 0;
}
