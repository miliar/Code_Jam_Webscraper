#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int M = 30;
char s[M];
int n;

inline bool next() {
  int i=n-1;
  while(i>=1 && s[i]>=s[i+1]) --i;
  if(i<1) return false;
  int j=i+1;
  while(j<n && s[j+1]>s[i]) ++j;
  swap(s[i], s[j]);
  reverse(s+i+1, s+n+1);
  return true;
}


inline void transform() {
  int ile[11];
  for(int i=0; i<10; ++i) ile[i]=0;
  for(int i=1; i<=n; ++i) ile[s[i]-'0']++;
  ++ile[0];
  int i=1;
  while(ile[i]==0) ++i;
  -- ile[i];
  int len=0;
  s[++len]='0'+i;
  while(ile[0]) { s[++len]='0'; --ile[0]; }
  while(i<=9) {
    while(ile[i]) { s[++len]='0'+i; --ile[i]; }
    ++ i;
  }
  s[len+1]=0;
}

int main() {
  int zes;
  scanf("%d\n", &zes);
  for(int i=1; i<=zes; ++i) {
    scanf("%s\n", s+1);
    n = strlen(s+1);
    printf("Case #%d: ", i);
    if(next()) {
      printf("%s\n", s+1);
    } else {
      transform();
      printf("%s\n", s+1);
    }
  }
  return 0;
}