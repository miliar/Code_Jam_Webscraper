#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int caseCount;
int C, D, N;
string invokes;

char _trans[26][26];
char _oppose[26][26];

char trans(char a, char b) {
  return _trans[a-'A'][b-'A'];
}
void setTrans(char a, char b, char c) {
  _trans[a-'A'][b-'A'] = _trans[b-'A'][a-'A'] = c;
}

bool oppose(char a, char b) {
  return _oppose[a-'A'][b-'A'];
}
void setOppose(char a, char b) {
  _oppose[a-'A'][b-'A'] = _oppose[b-'A'][a-'A'] = true;
}

typedef vector<char> VC;
VC res;

void solve(int caseNum) {
  res.clear();
  REP(i, 0, 26) {
    REP(j, 0, 26) {
      _trans[i][j] = 0;
      _oppose[i][j] = false;
    }
  }
  cin>>C;
  REP(i, 0, C) {
    string buf;
    cin>>buf;
    assert(buf.size()==3);
    setTrans(buf[0], buf[1], buf[2]);
  }
  cin>>D;
  REP(i, 0, D) {
    string buf;
    cin>>buf;
    assert(buf.size()==2);
    setOppose(buf[0], buf[1]);
  }
  cin>>N;
  cin>>invokes;
  assert(invokes.size()==N);

  REP(i, 0, invokes.size()) {
    res.push_back(invokes[i]);


    while(true) {
      bool modified = false;
      // printf("== %d\n", res.size());

      if (res.size()>=2) {
        char b=res[res.size()-2];
        char c=res[res.size()-1];
        if (trans(b, c)) {
          res.pop_back();
          res.pop_back();
          res.push_back(trans(b, c));
          modified = true;
          continue;
        }
      }
      if (res.size()>=2) {
        REP(j, 0, res.size()) {
          char c = res[res.size()-1];
          char d = res[j];
          if (oppose(d, c)) {
            res.clear();
            modified = true;
            break;
          }
        }
      }

      if (!modified) break;
    }
  }

  printf("Case #%i: ", caseNum);
  printf("[");
  REP(i, 0, res.size()) {
    if (i!=0)
      printf(", ");
    printf("%c", res[i]);
  }
  printf("]\n");
  // cout<<invokes<<endl;
}

int main() {
  unittest();

  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
  assert(true);
}

