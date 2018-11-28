#include <iostream>
#include <string>
using namespace std;
#define MAX 5010
string st[MAX];
int L,D,N;
bool pattern(const string &pat,const string & a) {
  int top = 0;
  for (int i = 0;i<L;++i) {
    if (pat[top]=='(') {
      bool flag = false;
      while (pat[top]!=')') {
        ++top;
        if (pat[top]==a[i]) flag = true;
      }
      if (!flag) return false;
      ++top;
    } else {
      if (pat[top]!=a[i]) return false;
      ++top;
    }
  }
  return true;
}
int main(void) {
  freopen("fdin.txt","r",stdin);
  freopen("fdin.out","w",stdout);
  scanf("%d%d%d",&L,&D,&N);
  for (int i = 0;i<D;++i)
    cin >> st[i];
  for (int i = 0;i<N;++i) {
    string tmp;
    cin >> tmp;
    int ans = 0;
    for (int j=0;j<D;++j)
      if (pattern(tmp,st[j])) ++ans;
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}