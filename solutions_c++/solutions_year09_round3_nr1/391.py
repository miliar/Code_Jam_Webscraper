#include <iostream>
#include <cmath>
#include <set>
#include <string>
using namespace std;
set<char> hash;
string ch;
int cnt;
void readin() {
  hash.clear();ch = "";cnt = 0;
  char tmp = getchar();
  while (tmp!='\n') {
    ch += tmp;
    if (hash.find(tmp)==hash.end()) {
      ++cnt;
      hash.insert(tmp);
    }
    tmp = getchar();
  }
}

void doit() {
  int len = ch.length();
  int vv = 1;
  bool flag = true;
  for (int i = 0;i<len;++i) {
    if (hash.find(ch[i])!=hash.end()) {
      char tmp = ch[i];
      if (vv==2 && flag) {
        flag = false;
        for (int j = 0;j<len;++j) {
          if (ch[j]==tmp) ch[j] = 0;
        }
      } else {
        for (int j = 0;j<len;++j) {
          if (ch[j]==tmp) ch[j] = vv;
        }
        ++vv;
      }
      hash.erase(ch[i]);
    }
  }
  long long ans = 0;
  if (cnt==1) cnt = 2;
  for (int i = 0;i<len;++i) {
    ans +=ch[i]*pow((double)cnt,(double)len-i-1);
  }
  printf("%I64d\n",ans);
}
int main(void) {
  int T;
  freopen("fdin.txt","r",stdin);
  freopen("fdout.txt","w",stdout);
  scanf("%d\n",&T);
  int cas = 1;
  while (T--) {
    printf("Case #%d: ",cas);
    readin();
    doit();
    ++cas;
  }
}