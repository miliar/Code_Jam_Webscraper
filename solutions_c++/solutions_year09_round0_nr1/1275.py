#include <cstdio>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int M = 5001;

string a[M];
int D;

int L, N;

inline bool isletter(char x) {
  return x>='a' && x<='z';
}

map<char,bool> can[20];

char bufer[100];
int main() {
  scanf("%d %d %d\n", &L, &D, &N);
  for(int i=1; i<=D; ++i) {
    scanf("%s\n", bufer);
    a[i] = bufer;
  }
  for(int i=1; i<=N; ++i) {
    scanf("%s\n", bufer);
    for(int j=0;j<L;++j) can[j].clear();
    int p=0;
    for(int j=0; j<L; ++j) {
      if(isletter(bufer[p])) {
        can[j][bufer[p]]=true;
        ++p;
      } else {
        ++p;
        while(bufer[p]!=')') {
          can[j][bufer[p]]=true;
          ++p;
        }
        ++p;
      }
    }
    int ret=0;
    for(int k=1; k<=D; ++k) {
      bool good=true;
      for(int j=0;j<L;++j) {
        if(!can[j][a[k][j]]) {
          good=false;
          break;
        }
      }
      ret+=good;
    }
    printf("Case #%d: %d\n", i, ret);
  }
  return 0;
}
