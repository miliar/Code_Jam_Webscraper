#include <cstdio>
#include <string>
using namespace std;

const int M = 50;
string a[M];
int n;

bool f(string s, int k) {
  int p=n-1;
  while(p>0 && s[p]=='0') --p;
  return p<=k;
}

int solve() {
  int ret=0;
  for(int i=0;i<n;++i) {
    int j=i;
    while(!f(a[j],i)) ++j;
    while(j!=i) swap(a[j],a[j-1]), --j, ++ret;
  } return ret;
}

char buf[1000];
int main() {
  int d;
  scanf("%d\n",&d);
  for(int j=1;j<=d;++j) {
    scanf("%d\n",&n);
    for(int i=0;i<n;++i) {
      scanf("%s\n",buf);
      a[i]=string(buf);
    }
    printf("Case #%d: %d\n",j,solve());
  }
  return 0;
}