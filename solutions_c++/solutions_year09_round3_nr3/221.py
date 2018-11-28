#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int P;
int a[100];
vector<int> b;
int Q;
int bribe() {
    memset(a, 0, sizeof(a));
    int c=0;
    for(int i=0;i<Q;i++) {
      for(int j=b[i]-2; j>=0 && a[j]==0; j--) c++;
      for(int j=b[i]; j<P && a[j]==0; j++) c++;
      a[b[i]-1]=1;
    }
    return c;
}
int main() {
  int T;
  cin>>T;
  for(int t=1;t<=T;t++) {
    cin>>P>>Q;
    b.clear();
    for(int i=0;i<Q;i++) { int tmp; cin>>tmp; b.push_back(tmp); }
    int c=bribe();
    while (next_permutation(b.begin(), b.end())) {
      c=min(c, bribe());
    }
    printf("Case #%d: %d\n", t, c);
  }
  return 0;
}
